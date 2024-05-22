import pandas as pd
import plotly
import plotly.express as px

def make_histogram(dataframe):
    # Préparer les données : fusionner les colonnes pour les parts de marché françaises et américaines
    df_pdm = dataframe.melt(id_vars=['N° auto'], 
                            value_vars=['PdM en entrées des films français', 'PdM en entrées des films américains'],
                            var_name='Type de Film', value_name='Part de Marché')
    # Créer l'histogramme
    fig = px.histogram(df_pdm, x='Part de Marché', color='Type de Film',
                       barmode='overlay',  # Superpose les barres pour une comparaison directe
                       nbins=100,  # Nombre de divisions sur l'axe des X
                       title='Distribution des parts de marché des films français et américains',
                       labels={'Part de Marché': 'Part de marché (%)', 'Type de Film': 'Catégorie de Film'})

    # Améliorer la transparence pour que les superpositions soient visibles
    fig.update_traces(opacity=0.75)
    return fig


