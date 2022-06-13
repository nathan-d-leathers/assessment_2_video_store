import csv 
import os.path

class Customer:
   
    def __init__(self,id,account_type,first_name,last_name,current_video_rentals):
        self.id = id
        self.account_type = account_type
        self.first_name = first_name.lower().capitalize()
        self.last_name = last_name.lower().capitalize()
        self.current_video_rentals = current_video_rentals.split('/')
    
    @classmethod
    def objects(cls):
        id_num = 0
        current_customers = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                current_customers.append(Customer(**dict(row)))
                id_num +=1
        return current_customers  

