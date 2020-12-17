import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import json

df = pd.read_json('link', orient="records")
print(df)
print(df.head())

s = df.iloc[0]
print(s[0])

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in s[0].keys()])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][0][col]) for col in s[0].keys()
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='TITLE'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)