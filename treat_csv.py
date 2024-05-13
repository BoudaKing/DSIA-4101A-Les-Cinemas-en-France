import pandas as pd

def treat_csv(csv_path):
    data = pd.read_csv(csv_path)
    
    ## SUPPRIMER LES COLONNES INUTILES

    irrelevant_fields = ['régionCNC','adresse','N°UU','unité urbaine','population unité urbaine', 'évolution entrées', 'tranche d\'entrées', 'AE', 'catégorie Art et Essai', 'label Art et Essai', 'genre', 'multiplexe', 'zone de la commune', 'films Art et Essai', 'geolocalisation']
    # Region CNC : On a deja le nom de la region, et c'est plus commun de referer a une region par son nom que par son code de region (qui est specifique au CNC)
    # N°UU : on s'en fout de l'unité urbaine, c'est plus précis de parler de commune
    # population UU : pareil, on a deja la population de la commune
    # evolution entrees : redondant, on a deja les entrees en 2021 et 2022
    # tranche d'entrees : on a deja les entrees 2021 et 2022 + le format est chiant à traiter
    # categorie art et essai : on choisit de ne pas se servir de ces données (ça concerne trop peu de cinémas)
    # AE : pareil
    # label art et essai : pareil
    # genre : pareil
    # multiplexe : pareil
    # zone de la commune : format de donnée pas exploitable
    # films art et essai : on sait pas ce que c'est, y'a pas de documentation
    # geolocalisation : redondant, on a deja latitude et longitude

    data.drop(columns=irrelevant_fields, inplace=True)

    #On supprime les lignes où des champs ne sont pas renseignés. Cela arrive dans les colunnes 'entrées 2021' et 'Pdm arts et essai'.
    data.dropna(subset=['entrées 2021','PdM en entrées des films Art et Essai'],inplace=True)

    data[['écrans', 'fauteuils', 'semaines d\'activité', 'séances', 'entrées 2021', 'entrées 2022', 'nombre de films programmés', 'nombre de films inédits', 'nombre de films en semaine 1']] = data[['écrans', 'fauteuils', 'semaines d\'activité', 'séances', 'entrées 2021', 'entrées 2022', 'nombre de films programmés', 'nombre de films inédits', 'nombre de films en semaine 1']].astype(int)

    data.loc[data['programmateur'].isna(), 'programmateur'] = 'AUCUN'

    return data
