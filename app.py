from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
import analytics

app = Flask(__name__)
DB_NAME = "database.db"

# --- SETUP ---

# Make sure the database exists and has the right table
def init_db():
    conn = sqlite3.connect(DB_NAME)   # open the database
    c = conn.cursor()                 # write into the database
    c.execute('''
        CREATE TABLE IF NOT EXISTS writing_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,   -- a unique ID for each entry
            entry_date TEXT,                        -- when the writing was done
            word_count INTEGER,                     -- how many words were written
            project TEXT                            -- which project it belongs to
        )
    ''')
    conn.commit()    # save changes
    conn.close()     # close the database

# initalize the db
init_db()

@app.route("/", methods=["GET", "POST"])
@app.route("/add", methods=["GET", "POST"])
def home_page():
    """The form page where you add new writing entries."""
    if request.method == "POST":                     # If submit
        date = request.form["date"]                  # get the date
        words = int(request.form["word_count"])      # get the word count
        project = request.form["project"]            # get the project name

        # Save the entry
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute(
            "INSERT INTO writing_entries (entry_date, word_count, project) VALUES (?, ?, ?)",
            (date, words, project),
        )
        conn.commit()
        conn.close()

        # send entries to page
        return redirect(url_for("entries"))

    # return to page
    return render_template("home_page.html")


@app.route("/entries")
def entries():
    """Show all writing entries, grouped by date."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT entry_date, word_count, project FROM writing_entries ORDER BY entry_date DESC")
    rows = c.fetchall()
    conn.close()

    # Group entries by date so they are easy to read
    grouped = {}
    for date, words, project in rows:
        if date not in grouped:
            grouped[date] = []
        grouped[date].append({"word_count": words, "project": project})

    # Show them in the web page
    return render_template("entries.html", grouped=grouped)


@app.route("/stats")
def stats():
    """Show statistics like streaks and totals using analytics.py."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT entry_date, word_count, project FROM writing_entries ORDER BY entry_date")
    data = c.fetchall()
    conn.close()

    # Use the analytics file to calculate stats
    streak, project_totals, prediction = analytics.analyze_data(data)

    # Send the stats to the webpage
    return render_template(
        "stats.html",
        data=data,
        streak=streak,
        project_totals=project_totals,
        prediction=prediction,
    )


@app.route("/friends")
def friends():
    """Friends page (future feature)."""
    return render_template("friends.html")


# --- RUN THE APP ---

if __name__ == "__main__":
    app.run(debug=True)   # Start the website
