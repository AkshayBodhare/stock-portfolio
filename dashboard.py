import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from get_data import get_intraday_data
from datetime import datetime as dt

app = dash.Dash('Hello World')

app.layout = html.Div([
    dcc.Input(id='my-id', value='API_KEY', type='text'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '500'})

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')
                                                    ('my-id', 'value')])
def update_graph(selected_dropdown_value, input_value):
    API_KEY = input_value
    df = get_intraday_data(API_KEY, selected_dropdown_value, '1min')
    return {
        'data': [{
            'x': df['date'],
            'y': df['4. close']
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server()