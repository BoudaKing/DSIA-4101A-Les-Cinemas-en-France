# DSIA-4101A-Les-Cinemas-en-France

# 1° Déploiement 

Pour dépolyer le projet, il faut d'abord cloner sur la machine en utilisant la commande suivante : 
```
git clone git@github.com:BoudaKing/DSIA-4101A-Les-Cinemas-en-France.git
```
Exécuter la commande d’installation en tant que « Administrateur » pour les utilisateurs Windows ou « SuperUser » pour les utilsateurs Linux

Une fois cela fait, il faut installer les dépendances nécessaires à l'exécution, à l'aide de la commande: 
```
python -m pip install -r requirements.txt
```

Par la suite, il sera nécessaire de télécharger les données requises, un processus qui assurera le bon fonctionnement de l'application, via la commande:
```
python get_data.py
```
Pour démarrer l'application, il faudra utiliser la commande suivante:  
```
python main.py
```

Enfin, ouvrer un navigateur web et accédez à l'URL suivante: 
```
http://127.0.0.1:8050/  afin de vous connecter au dashboard. 
```

NB: Je me sers de curl pour faire une requete http et récupérer le fichier.

# 2° Les données 

Les données proviennent du site https://data.culture.gouv.fr/explore/dataset/etablissements-cinematographiques/information/

Pour telecharger le fichier csv, faire la commande 

```
cd ./data
```

puis 

```
curl -L -O -J https://data.culture.gouv.fr/api/explore/v2.1/catalog/datasets/etablissements-cinematographiques/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B

```


Ce jeu de données exploité dans mon projet est une compilation exhaustive des informations concernant les établissements cinématographiques en France. Ces données incluent diverses caractéristiques telles que le nom de l'établissement, sa localisation, la programmation, les parts de marchés par catégortie de films...

Au lancement de l'application, 3 graphiques sont visibles:
Ces trois types de visualisations, pour analyser les données sur les cinémas en France sont: un histogramme, un scatterplot et une carte interactive. À noter que pour tous les graphiques, on peut filtrer l'affichage des données en cliquant dessus.

    Premier graphique:
Comme on peut voir sur cet histogramme, on constate deux catégories distinguées par leurs couleurs; représentant chacune la part de marché des films américains et des films français. 
L'analyse de l'histogramme révèle une distinction claire entre les films français et américains en termes de parts de marché. Les films français tendent généralement à avoir une part de marché plus large dans la plupart des cinémas, ce qui est cohérent avec l'obligation du respect d'un certain quota de distritbution de films français. On peut voir l'exemple d'une extrémité où la part de marché des films français est à 100%, montrant ainsi la volonté de valoriser les films français.

Par ailleurs, les films américain montrent une présence significative, soulignant leur importance dans l'industrie cinématographique  et leur appréciation par le public local. Cette distribution reflète non seulement les préférences culturelles mais aussi les stratégies de programmation des cinémas qui équilibrent entre attirer le grand public et soutenir le cinéma national français.

Toutefois, on peut voir un chevauchement des Parts de Marché : La superposition des parts représentés dans l'histogramme montre des zones où les parts de marché des films français et américains se chevauchent, suggérant que certains cinémas réussissent à équilibrer la programmation des deux catégories de films, répondant ainsi à une diversité de préférences du public.

    Deuxième graphique: 
Ici, on a un scatterplot où on peut sélectionner la situation géographique des cinémas, dans le but de pouvoir étudier la distribution géographique de ces derniers et de leur fréquentation, ce qui est essentielle pour comprendre les dynamiques de marché et les comportements des consommateurs dans différents contextes régionaux. On remarque que la majorité des villes qui ont moins de 20 mille habitants et hors I.D.F, présentent un ensemble plutôt agglutiné, et qu'ils ont une majorité de cinémas qui ne font pas beaucoup d'entrées (car ce sont des cinémas de proximité). Cependant, il y a parfois des anomalies, comme le cinéma MEGA qui fait beaucoup d'entrées malgré le fait qu'il soit dans une petite ville. Cela s'explique par le fait qu'il se market comme étant un cinéma à Rennes, et profite de sa situation en périphérie ce qui veut dire en d'autres termes, qu'il attire la population de Rennes. 

De plus, on a un phénomène similaire pour la petite couronne (départements 92,93,94) et les autre communes et unités urbaines, qui ont des graphes qui se supperposent presque, avec un autre exemple d'anomalie qui est le cinéma pathé à Belle Epine, qui est un centre commercial, donc qui n'attire pas que la population de Thiais. Cela offre des perspectives sur comment des facteurs comme le placement dans des zones à forte fréquentation commerciale peuvent influencer le succès, ce qui est crucial pour les décideurs dans le domaine du cinéma et de l'urbanisme.
On remarque ici que la majorité

    Troisième graphique: 

"J'ai d'abord essayé à l'échelle logarithmique mais le résultat n'était pas visible à l'oeil nu."

La repésentation des cinémas en France basée sur les données de fréquentation de 2022 est ici visible sur la carte. On réussi à identifier les zones de forte et de faible affluence, une étude qui peut également servir à planifier des stratégies de marketing ciblées ou à prendre des décisions concernant l'ouverture de nouveaux cinémas ou la fermeture de ceux sous-performants. 

On peut s'apercevoir ici, que par exemple, dans les zones rurales ou moins peuplées comme les vosges, le nombre d'entrées enregistré est très faible un phénomène qui peut être attribué à son positionnement dans ce que l'on appelle la diagonale du vide, ce qui rend le cinéma très mal desservi. Les cinémas avec les plus grandes entrées sont dans les métropoles, comme on peut voir pour Paris, Toulon, Marseille etc...
Chaque point nous fournit le nom, le département et les entrées de l'année 2022 du cinéma en question.

# 3° Developper guide 

Le projet se structure autour de plusieurs fichiers et répertoires à la racine : un fichier principal main.py contenant le script d'analyse, un dossier data avec les fichiers CSV nécessaires, un fichier requirements.txt qui répertorie les librairies externes nécessaires pour exécuter le script, un fichier README.md pour les instructions générales.

Le script en lui-même est divisé en plusieurs segments clés. La première partie s'occupe du chargement des données à partir d'un fichier CSV et de leur nettoyage initial, incluant la suppression des colonnes inutiles et la gestion des valeurs manquantes. Cette étape est cruciale pour assurer la qualité des analyses ultérieures.

La seconde partie du script est dédiée aux fonctions de visualisation. Utilisant des bibliothèques comme folium pour la cartographie, le script permet de créer des visualisations riches et informatives. Ces outils offrent des insights dynamiques sur des variables telles que les parts de marché des films ou la géolocalisation des cinémas, avec des marqueurs colorés indiquant le volume des entrées.






 