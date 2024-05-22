# DSIA-4101A-Les-Cinemas-en-France

Les données proviennent du site https://data.culture.gouv.fr/explore/dataset/etablissements-cinematographiques/information/

Pour telecharger le fichier csv, faire la commande 

```
cd ./data
```

puis 

```
curl -L -O -J https://data.culture.gouv.fr/api/explore/v2.1/catalog/datasets/etablissements-cinematographiques/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B```