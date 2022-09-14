from tabulate import tabulate
import pandas

data = {'Auteur': ["Marc Levy", "Laétitia Colombani", "Guillaume Musso"],
        'Titre': ["Et si c'était vrai...", "La tresse", "Central Park"],
        'Editeur': ["Flammarion", "Gallimard", "Milan"],
        'Prix': [10, 15, 20]
        }  

dataframe = pandas.DataFrame(data)
  
print(tabulate(dataframe, headers = 'keys', tablefmt = 'psql'))