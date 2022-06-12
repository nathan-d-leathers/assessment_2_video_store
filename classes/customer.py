import csv 
import os.path

from video_inventory import Video_Inventory

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

    # def check_account_type(self):
    # pass

        # Customer.my_rentals.append(current_video_rentals)

        # id,account_type,first_name,last_name,current_video_rentals
    
# bobby = Customer(1,'sx','Monica','Gellar','The Godfather/Shawshank/TMNT')
# print(bobby.__dict__)
# output:
# {'id': 1, 'acount_type': ('sx',), 'first_name': 'Monica', 'last_name': 'Gellar', 'current_video_rentals': 'The Godfather'}
# billy = Customer(5,"Pf",'Billy','Six-String','Tank Girl/The Godfather/Shawshank/TMNT')

# print(billy.current_video_rentals)
# ['Tank Girl', 'The Godfather', 'Shawshank', 'TMNT']

# should put rental fucntionality on this page

# might be able to just use if/else statements for account type


# customer account type (sx/px/sf/pf)
# "sx" = standard account: max 1 rental out at a time
# "px" = premium account: max 3 rentals out at a time
# "sf" = standard family account: max 1 rental out at a time AND can not rent any "R" rated movies
# "pf" = premium family account: max 3 rentals out at a time AND can not rent any "R" rated movies

# for x in Customer.objects():
#     print(x.__dict__)
# # 
# output:
# {'id': '1', 'acount_type': ('sx',), 'first_name': 'Monica', 'last_name': 'Gellar', 'current_video_rentals': ['The Godfather']}
# {'id': '2', 'acount_type': ('px',), 'first_name': 'Chandler', 'last_name': 'Bing', 'current_video_rentals': ['The Dark Knight', 'Inception', 'The Prestige']}
# {'id': '3', 'acount_type': ('pf',), 'first_name': 'Rachel', 'last_name': 'Green', 'current_video_rentals': ['Inside Out', 'WALL-E', 'The Prestige']}
# {'id': '4', 'acount_type': ('sx',), 'first_name': 'Ross', 'last_name': 'Gellar', 'current_video_rentals': ['']}
# {'id': '5', 'acount_type': ('sf',), 'first_name': 'Phoebe', 'last_name': 'Buffay', 'current_video_rentals': ['WALL-E']}
# {'id': '6', 'acount_type': ('px',), 'first_name': 'Joey', 'last_name': 'Tribbiani', 'current_video_rentals': ['Deadpool', 'The Godfather']}

# len of x.customer_video_rentals:
# 1
# 3
# 3
# 1
# 1
# 2
# have to check if the split is best in the main init or not
