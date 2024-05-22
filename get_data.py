import os

file_name = 'etablissements-cinematographiques.csv'
directory = './data'
url = 'https://data.culture.gouv.fr/api/explore/v2.1/catalog/datasets/etablissements-cinematographiques/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B'

path = os.path.join(directory,file_name)

os.system(f'curl -L "{url}" -o "{path}"')