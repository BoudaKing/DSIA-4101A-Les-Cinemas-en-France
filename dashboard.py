import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import treat_csv as tc
import make_graphs
import make_map
import utils

def launch_app(name):
    df = tc.treat_csv('./data/etablissements-cinematographiques.csv')
    
    #Generation de l'histogramme
    histogram = make_graphs.make_histogram(df)

    #Generation du scatterplot
    options_scatterplot = utils.get_options_scatterplot(df)
    scatterplot = make_graphs.make_scatter_entrees(df)

   #Generation de la carte, puis enregistrement
    carte_cinemas = make_map.creer_carte_cinemas(df)

    carte_cinemas.save('./maps/map.html')

    app = dash.Dash(name)

    app.layout = html.Div(children=[

        #HISTOGRAMME
        html.H1(children=f'Histogramme',
            style={'textAlign': 'center', 'color': '#7FDBFF'}), 
        
        dcc.Graph(
            id='histogram',
            figure=histogram
        ),

        html.Div(children=f'''
            Ceci est un histogramme blablabla'''),

        #SCATTERPLOT
        html.H1(children=f'Scatterplot',
            style={'textAlign': 'center', 'color': '#7FDBFF'}), 

        dcc.Dropdown(
            id='dropdown-situation-geo',
            options=options_scatterplot,
            value='Tous'
        ),

        dcc.Graph(
            id='scatterplot',
            figure=scatterplot
        ),

        #CARTE
        html.H1("Folium Map Integration in Dash",
            style={'textAlign': 'center', 'color': '#7FDBFF'}),
        html.Iframe(
            srcDoc=open('./maps/map.html', 'r').read(),
            width='100%',
            height='600'
        )
        
    ])

    @app.callback(
        Output(component_id='scatterplot', component_property='figure'),
        [Input(component_id='dropdown-situation-geo', component_property='value')]
    )
    def update_scatterplot(value):
        return make_graphs.make_scatter_entrees(df,value)

    return app