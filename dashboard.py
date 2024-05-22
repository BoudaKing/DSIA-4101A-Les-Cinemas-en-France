import dash
from dash import dcc
from dash import html

import treat_csv as tc
import make_graphs
import make_map

def launch_app(name):
    df = tc.treat_csv('./data/etablissements-cinematographiques.csv')
    
    histogram = make_graphs.make_histogram(df)
    carte_cinemas = make_map.creer_carte_cinemas(df)

    carte_cinemas.save('./maps/map.html')

    app = dash.Dash(name)

    app.layout = html.Div(children=[

        html.H1(children=f'Histogramme',
            style={'textAlign': 'center', 'color': '#7FDBFF'}), 
        
        dcc.Graph(
            id='graph1',
            figure=histogram
        ),

        html.Div(children=f'''
            Ceci est un histogramme blablabla'''),

        html.H1("Folium Map Integration in Dash"),
        html.Iframe(
            srcDoc=open('./maps/map.html', 'r').read(),
            width='100%',
            height='600'
        )
        
    ])

    return app