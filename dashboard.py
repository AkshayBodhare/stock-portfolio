import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from get_data import get_intraday_data
from datetime import datetime as dt

app = dash.Dash('stock-tickers')

app.layout = html.Div([
    html.Div([
        dcc.Input(id='my-id', value='API_KEY', type='text'),
        html.Div(id='intermediate-value', style={'display': 'none'}),
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'Coke', 'value': 'COKE'},
                {'label': 'Tesla', 'value': 'TSLA'},
                {'label': 'Apple', 'value': 'AAPL'}
            ],
            value='COKE'
        ),
        dcc.Dropdown(
            id='my-dropdown1',
            options=[
                {'label': '1 minute', 'value': '1min'},
                {'label': '5 minutes', 'value': '5min'},
                {'label': '15 minutes', 'value': '15min'},
                {'label': '30 minutes', 'value': '30min'},
                {'label': '60 minutes', 'value': '60min'},
            ],
            value='60min'
        )
    ], style={'columnCount': 3}),
    dcc.Graph(id='my-graph')
], style={'rowCount': 2}) 

@app.callback(Output('intermediate-value', 'children'), [Input('my-id', 'value')])
def update_output_div(input_value):
    API_KEY = input_value
    return API_KEY

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value'),
                                    Input('intermediate-value', 'children'),
                                    Input('my-dropdown1', 'value')])
def update_graph(selected_dropdown_value, input_key, interval):
    API_KEY = input_key
    df = get_intraday_data(API_KEY, selected_dropdown_value, interval)
    return {
        'data': [{
            'x': list(df.index),
            'y': df['4. close']
        }],
        'layout': {'margin': {'l': 40, 'r': 10, 't': 20, 'b': 30},
                   'title': '{} data of {}'.format(interval,
                                                    selected_dropdown_value)}
    }

if __name__ == '__main__':
    app.run_server()