# -*- coding: utf-8 -*-

import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd

df = pd.read_json('https://isod.ee.pw.edu.pl/isod-portal/wapi?q=dissertations_offers&orgunit=ISEP&fromrow=10&maxrows=4&active=true&format=json&lang=en&datefrom=23.02.2010', orient="records")

print(df)
for i in df.iloc[0].loc['list'].keys():
    df[i] = 5
    for j in range(4):
        df.at[j,i] = j
app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='datatable-paging',
    columns=[
        {"name": i, "id": i} for i in sorted(df.columns)
    ],
    page_current=0,
    page_size=1,
    page_action='custom'
)

@app.callback(
    Output('datatable-paging', 'data'),
    Input('datatable-paging', "page_current"),
    Input('datatable-paging', "page_size"))

def update_table(page_current,page_size):
    return df.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')

if __name__ == '__main__':
    app.run_server()



