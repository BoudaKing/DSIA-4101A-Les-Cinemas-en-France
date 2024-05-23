# DSIA-4101A-Les-Cinemas-en-France

# 1° Déploiement 

Pour dépolyer le projet, il faut d'abord cloner sur la machine en utilisant la commande suivante : git clone git@github.com:BoudaKing/DSIA-4101A-Les-Cinemas-en-France.git

Une fois cela fait, il faut installer les dépendances nécessaires à l'exécution, à l'aide de la commande: python -m pip install -r requirements.txt

Par la suite, il sera nécessaire de télécharger les données requises, un processus qui assurera le bon fonctionnement de l'application, via la commande: python get_data.py

Pour démarrer l'application, il faudra utiliser la commande suivante:  python main.py

Enfin, ouvrer un navigateur web et accédez à l'URL suivante: http://127.0.0.1:8050/  afin de vous connecter au dashboard. 



# 2° Les données 

Au lancement de l'application, 3 graphiques sont visibles:
Ces trois types de visualisations, pour analyser les données sur les cinémas en France sont: un histogramme, un scatterplot et une carte interactive. À noter que pour tous les graphiques, on peut filtrer l'affichage des données en cliquant dessus.

Premier graphique:
Comme on peut voir sur cet histogramme, on constate deux catégories distinguées par leurs couleurs; représentant chacune la part de marché des films américains et des films français 



Deuxième graphique:


On remarque ici que la majorité





Les données proviennent du site https://data.culture.gouv.fr/explore/dataset/etablissements-cinematographiques/information/

Pour telecharger le fichier csv, faire la commande 

```
cd ./data
```

puis 

```
curl -L -O -J https://data.culture.gouv.fr/api/explore/v2.1/catalog/datasets/etablissements-cinematographiques/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B```


hbthvth hyt thtg
 bgbyjj
 