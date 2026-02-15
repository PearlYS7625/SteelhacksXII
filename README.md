# SteelHackXII: *ScribeStats*
![ScribeStats](https://github.com/user-attachments/assets/b2852870-1479-468f-bf39-0041badd3389)

*By: Natalie Goldsworthy, Abby Koss, Pearl Singer, and Jessica Wagner*

### Table of Contents
- [Overview](#overview)
- [How It Works](#process)
- [Video Demonstration](#video-demonstration)
- [Devpost Submission](#devpost-submission)

## Overview
ScribeStats is designed to help writers track their daily progress, stay motivated, and achieve their writing goals. By combining habit tracking with data analytics, the website encourages consistent writing and provides insights into personal productivity.

## How It Works
<img width="666" height="398" alt="ScribeStatsFlowDiagram" src="https://github.com/user-attachments/assets/38f645ef-082a-4e16-931b-dcfda845fda3" />

The **index.html form** is displayed to the user, who enters the date, word count, and associated project for their writing entry. This data is then sent to **app.py**, which stores the entry in an **SQLite database** (creating **database.db** if it doesn’t already exist). The stored data is passed to **analytics.py**, where calculations are performed to determine the current writing streak, total words per project, and predictions for the upcoming week. The results from **analytics.py** are then returned to **app.py**, which renders them in **stats.html** for the user to view. Both **index.html** and **stats.html** use **style.css** for consistent styling.

## Video Demonstration
[https://youtu.be/2dxViQmwkp4](https://youtu.be/2dxViQmwkp4)

## Devpost Submission
[devpost.com](https://devpost.com/software/tbd-n8pl3m)

