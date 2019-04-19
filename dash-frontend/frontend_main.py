#!/usr/bin/python
# coding=utf-8
from flask import Flask

import sqlalchemy
import psycopg2
import sys
import os
import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def connect():
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    host = os.environ['POSTGRES_HOST']
    db = os.environ['POSTGRES_DB']
    port = 5432
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect()
highest_dens_df = pd.read_sql_query('SELECT nativecountry AS "Accent", languagerecorded as "Language Recorded", COUNT(*) as "Number of Files", max(processingdatetime) as "Most Recent Record" FROM "test2" GROUP BY nativecountry, languagerecorded ORDER BY COUNT(*) DESC LIMIT 10', con)
lowest_dens_df = pd.read_sql_query('SELECT nativecountry AS "Accent", languagerecorded as "Language Recorded", COUNT(*) as "Number of Files", max(processingdatetime) as "Most Recent Record" FROM "test2" GROUP BY nativecountry, languagerecorded ORDER BY COUNT(*) ASC LIMIT 10', con)
top_df = pd.read_sql_query('select * from "test2" ORDER BY processingdatetime DESC LIMIT 10',con)

app.layout = html.Div(children=[
	html.H1(children='Listen Up'),
	html.P(children='Accented speech processing for machine learning models'),

	html.Div(style={'margin' : '20px 15%'},children=[
		html.Div(children=html.H5(children='''
                	Highest Density Data
        	''')),

        	dash_table.DataTable(
                	id='table',
                	style_data={'whiteSpace': 'normal'},
                	css=[{
                        	'selector': '.dash-cell div.dash-cell-value',
                        	'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
                	}],
                	columns=[{"name": i, "id": i} for i in highest_dens_df.columns],
                	data=highest_dens_df.to_dict("rows"),
        	),
		html.Div(children=html.H5(children='''
                        Lowest Density Data
                ''')),

                dash_table.DataTable(
                        id='table',
                        style_data={'whiteSpace': 'normal'},
                        css=[{
                                'selector': '.dash-cell div.dash-cell-value',
                                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
                        }],
                        columns=[{"name": i, "id": i} for i in lowest_dens_df.columns],
                        data=lowest_dens_df.to_dict("rows"),
                ),
	]),

	html.Div(children=html.H5(children='''
		Most Recent Records
	''')),

	dash_table.DataTable(
		id='table',
		style_data={'whiteSpace': 'normal'},
		css=[{
        		'selector': '.dash-cell div.dash-cell-value',
        		'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
    		}],
		columns=[{"name": i, "id": i} for i in top_df.columns],
		data=top_df.to_dict("rows"),
	)
])

# run the Dash app.
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='5000')
