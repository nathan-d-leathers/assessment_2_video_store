import csv 
import os.path
from video import Video

class Video_Inventory(Video):
    
    def __init__(self,id,title,rating,release_year,copies_available):
        super().__init__(id,title,rating,release_year,copies_available)


    @classmethod
    def objects(cls):
        inventory = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                inventory.append(Video_Inventory(**dict(row)))
        return inventory


# for x in Video_Inventory.objects():
#     print(x.__dict__)

# output:
# {'id': '1', 'title': 'Toy Story', 'rating': 'G', 'release_year': '1995', 'copies_available': '0'}
# {'id': '2', 'title': 'WALL-E', 'rating': 'G', 'release_year': '2008', 'copies_available': '2'}
# {'id': '3', 'title': 'Up', 'rating': 'G', 'release_year': '2009', 'copies_available': '5'}
# {'id': '4', 'title': 'Inside Out', 'rating': 'PG', 'release_year': '2015', 'copies_available': '1'}
# {'id': '5', 'title': 'The Prestige', 'rating': 'PG-13', 'release_year': '2006', 'copies_available': '2'}
# {'id': '6', 'title': 'The Dark Knight', 'rating': 'PG-13', 'release_year': '2008', 'copies_available': '3'}
# {'id': '7', 'title': 'Inception', 'rating': 'PG-13', 'release_year': '2010', 'copies_available': '4'}
# {'id': '8', 'title': 'Intersteller', 'rating': 'PG-13', 'release_year': '2014', 'copies_available': '2'}
# {'id': '9', 'title': 'Deadpool', 'rating': 'R', 'release_year': '2016', 'copies_available': '3'}
# {'id': '10', 'title': 'The Godfather', 'rating': 'R', 'release_year': '1972', 'copies_available': '0'}

# Idea: Full_Inventory copy to not maniuplate when renting