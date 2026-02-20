import sqlite3
import pandas as pd
import gradio as gr

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
WITH top_hitters as (SELECT nameFirst, nameLast, batting.playerID FROM batting inner join people
on batting.playerID = people.playerID
Where teamID = "PHI"
Group by batting.playerID
Order by SUM(HR) DESC
LIMIT 10)

SELECT CONCAT (nameFirst, ' ', nameLast) as Player, playerID FROM top_hitters
ORDER by nameLast
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

def f(playerID):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """ SELECT CAST (yearID AS text), HR FROM batting
    where TeamID = 'PHI' and playerID = ?
    """
    cursor.execute(query, [playerID])
    records = cursor.fetchall()
    conn.close()
    df = pd.DataFrame(records, columns=["Year", "Home Runs"])
    return df


with gr.Blocks() as iface:
    playerDrop = gr.Dropdown(records, interactive=True)
    plot = gr.LinePlot(x = "Year", y = "Home Runs")
    playerDrop.change(fn = f, inputs = [playerDrop], outputs = [plot])

iface.launch()



#print(records)