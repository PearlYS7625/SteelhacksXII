from datetime import datetime, timedelta

def analyze_data(data):
    # Prepare dates in descending order
    dates = sorted([datetime.strptime(d[0], "%Y-%m-%d").date() for d in data], reverse=True)
    
    streak = 0
    if dates:
        streak = 1
        for i in range(1, len(dates)):
            # if previous date is exactly 1 day before current
            if (dates[i-1] - dates[i]).days == 1:
                streak += 1
            else:
                break

    # Project totals
    project_totals = {}
    for entry in data:
        project = entry[2]
        words = entry[1]
        project_totals[project] = project_totals.get(project, 0) + words

    # Simple prediction
    if data:
        total_words = sum(entry[1] for entry in data)
        avg_per_day = total_words / len(data)
        prediction = int(avg_per_day * 7)
    else:
        prediction = 0

    return streak, project_totals, prediction

