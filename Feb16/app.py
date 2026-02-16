import sqlite3
import pandas as pd
import gradio as gr

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
WITH top_hitters as (SELECT nameFirst, nameLast FROM batting inner join people
on batting.playerID = people.playerID
Where teamID = "PHI"
Group by batting.playerID
Order by SUM(HR) DESC
LIMIT 10)

SELECT CONCAT (nameFirst, ' ', nameLast) as Player FROM top_hitters
ORDER by nameLast
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

players = []
for record in records:
    players.append(record[0])

print(players)

