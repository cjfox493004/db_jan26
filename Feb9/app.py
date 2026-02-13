import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()

query = """
    SELECT batting.yearID, name, batting.HR from batting inner join teams
    on batting.teamID = teams.teamID and batting.yearID = teams.yearID
    Where playerID = 'ruthba01'
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records)
print(records_df)