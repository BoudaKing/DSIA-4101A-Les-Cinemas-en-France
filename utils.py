def get_options_scatterplot(df):
    #Fonction pour obtenir la liste des situations géographiques et la formatter pour la mettre dans un dcc.Dropdown
    option_list = list(df['situation géographique'].unique())
    options = [{'label': o[3:], 'value': o} for o in option_list] 
    options = [{'label': 'Tous', 'value': 'Tous'}] + options #On rajoute une option pour sélectionner toutes les situations géographiques

    return options
