import folium
from branca.colormap import linear

def creer_carte_cinemas(dataframe):
    # Définir les valeurs min et max pour l'échelle de couleurs
    min_entrees = dataframe['entrées 2022'].min()
    max_entrees = dataframe['entrées 2022'].max()

    # Créer une échelle de couleurs linéaire de jaune à rouge
    colormap = linear.Blues_09.scale(min_entrees, max_entrees)
    colormap.caption = 'Nombre d\'entrées en 2022'

    # Créer la carte centrée sur la moyenne des latitudes et longitudes
    m = folium.Map(location=[dataframe['latitude'].mean(), dataframe['longitude'].mean()], zoom_start=6)

    # Ajout de markers avec popup pour chaque cinéma
    for _, row in dataframe.iterrows():
        popup_text = f"<strong>Nom:</strong> {row['nom']}<br>"\
                     f"<strong>Département:</strong> {row['DEP']}<br>"\
                     f"<strong>Entrées 2022:</strong> {int(row['entrées 2022'])}"
        popup = folium.Popup(popup_text, max_width=300)
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5,  # Taille du cercle
            color=colormap(row['entrées 2022']),  # Couleur dépendante du nombre d'entrées
            popup=popup,  # Ajout du popup
            fill=True,
            fill_opacity=0.7
        ).add_to(m)

    # Ajout de la légende de couleur à la carte
    colormap.add_to(m)

    return m