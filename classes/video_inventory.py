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
