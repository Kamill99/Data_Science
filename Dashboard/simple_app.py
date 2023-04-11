import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H2(children='Hello Dash!'),
    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x=['2021', '2022', '2023'],
                y=[150, 180, 220],
                name='Lokalnie'
            ),
            go.Bar(
                x=['2021', '2022', '2023'],
                y=[200, 250, 234],
                name='Online'
            )
        ]
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
