# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
from datetime import datetime

app = Dash()

df = pd.read_csv("data_formatted.csv").sort_values(by="date")
fig = px.line(df, x="date", y="sales", color="region", title="Pink Morsel Visualiser")
# Converting datetime to UNIX time to highlight the price change date
price_change_date = datetime(2021, 1, 15)
unix_price_change_date = int(price_change_date.timestamp()) * 1000
fig.add_vline(
    x=unix_price_change_date,
    line=dict(color="red", width=3, dash="dot"),
    annotation_text=f"Price change",
    annotation_position="top left"
)

regions = ["all"] + df["region"].unique().tolist()

color_map = {
    "north": "#1f77b4",  # blue
    "south": "#2ca02c",  # green
    "east":  "#d62728",   # red
    "west":  "#9e00ff"   # purple 
}

@app.callback(
    Output("visualiser", "figure"),
    Input("region-selector", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]
    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        color="region",
        title=f"Sales of Pink Morsels over time - region: {selected_region}",
        color_discrete_map=color_map
    )
    # fig = px.line(data, x="date", y="sales", color="region", title="Pink Morsel Visualiser")
    price_change_date = datetime(2021, 1, 15)
    unix_price_change_date = int(price_change_date.timestamp()) * 1000
    fig.add_vline(
        x=unix_price_change_date,
        line=dict(color="red", width=3, dash="dot"),
        annotation_text=f"Price change",
        annotation_position="top left"
    )
    return fig


app.layout = html.Div(
    children=[
        html.H1(
            "Pink Morsel Visualisation",
            id="header",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "10px"
            }
        ),

        html.Div(
            "Easily visualise the impact of Pink Morsel price change on sales!",
            id="description",
            style={
                "textAlign": "center",
                "color": "#7f8c8d",
                "fontSize": "18px",
                "marginBottom": "30px"
            }
        ),
        html.Div(
            children=[
                html.H2("Select Region", style={"textAlign": "right"}),
                dcc.RadioItems(
                    id="region-selector",
                    options=[{"label": r, "value": r} for r in regions],
                    value=regions[0],
                    inline=True,
                    style={
                        "display": "flex",
                        "justifyContent": "flex-end"}
                )
            ],
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "10px",
                "boxShadow": "0 2px 6px rgba(0,0,0,0.1)",
                "width": "90%",
                "margin": "auto",
                "marginBottom": "15px"
            }
        ),
        html.Div(
            dcc.Graph(id="visualiser"),
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "10px",
                "boxShadow": "0 2px 6px rgba(0,0,0,0.1)",
                "width": "90%",
                "margin": "auto"
            }
        )
    ],
    style={
        "backgroundColor": "#f4f6f7",
        "fontFamily": "Arial, sans-serif",
        "padding": "30px 0"
    }
)


if __name__ == '__main__':
    app.run()
