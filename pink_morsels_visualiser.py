# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from datetime import datetime

app = Dash()

data = pd.read_csv("data_formatted.csv").sort_values(by="date")
fig = px.line(data, x="date", y="sales", color="region", title="Pink Morsel Visualiser")
# Converting datetime to UNIX time to highlight the price change date
price_change_date = datetime(2021, 1, 15)
unix_price_change_date = int(price_change_date.timestamp()) * 1000
fig.add_vline(
    x=unix_price_change_date,
    line=dict(color="red", width=3, dash="dot"),
    annotation_text=f"Price change",
    annotation_position="top left"
)
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Visualisation', id="header"),
    html.Div(children='''
        Easily visualise the impact of Pink Morsel price change on sales!
    ''', id="description"),

    dcc.Graph(
        id='visualiser',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run()
