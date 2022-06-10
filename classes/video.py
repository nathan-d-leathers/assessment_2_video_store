class Video:
    # full_inventory = []
    def __init__(self,id,title,rating,release_year,copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available
        # Video.full_inventory.append(self)


# Fury_Road = Video(12,'Mad Max: Fury Road', 'R', 2015, 5)
# print(Fury_Road.__dict__)
# output:
# {'id': 12, 'title': 'Mad Max: Fury Road', 'rating': 'R', 'release_year': 2015, 'copies_available': 5}

# Mad_Max = Video(13,'Mad Max', 'PG-13', 1981, 2)
# Mad_Max_2 = Video(14,'Mad Max 2', 'PG-13', 1985, 4)
# Mad_Max_3 = Video(15,'Mad Max 3', 'PG-13', 1988, 3)
# for vid in Video.full_inventory:
#     print(vid.__dict__)
# output:
# {'id': 13, 'title': 'Mad Max', 'rating': 'PG-13', 'release_year': 1981, 'copies_available': 2}
# {'id': 14, 'title': 'Mad Max 2', 'rating': 'PG-13', 'release_year': 1985, 'copies_available': 4}
# {'id': 15, 'title': 'Mad Max 3', 'rating': 'PG-13', 'release_year': 1988, 'copies_available': 3}