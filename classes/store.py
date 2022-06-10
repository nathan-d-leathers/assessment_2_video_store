from video_inventory import Video_Inventory
from customer import Customer

class Store:
    def __init__(self,name):
        self.name = name
        self.rentals_inventory = Video_Inventory.objects()
        self.rental_members = Customer.objects()
        # add customers

    def view_rental_list(self):
        print('\n')
        for vid in self.rentals_inventory:
            print(f"{vid.__dict__}")
            # working code

    def currently_rented(self,customer_id):
        for rental in self.rental_members:
            if customer_id == self.rental_members.id:
                return rental.current_video_rentals.split('/')
                # not working code

    def add_customer(self,customer_data):
        new_customer = Customer(**customer_data)
        new_id = len(self.rental_members) + 1
        new_customer.id = new_id
        self.rental_members.append(new_customer)
        print(f"\nNew Customer:\n{new_customer.first_name} {new_customer.last_name}\nID Number: {new_customer.id}\nwas sucessfully added to the system.")
        # working code!



# popupvideo = Store('Pop Up Video')
# popupvideo.currently_rented('1')

    # def rent_video(self):
        # find video id
        # push it to customer rental list
        # pass

    # def return_video(self):
        # find customer id
        # look for video id in customer list
        # pop it from customer rental list,
        # update inevntory or num of copies
        # pass

# bobs_store = Store('Bobs Stowre')
# bobs_rentals = Store.rental_list()


# Traceback (most recent call last):
#   File "/Users/nathanleathers/Desktop/git challenges/assessment-2/classes/runner.py", line 9, in <module>
#     store.view_rental_list()
#   File "/Users/nathanleathers/Desktop/git challenges/assessment-2/classes/store.py", line 11, in view_rental_list
#     for vid in enumerate(rentals_inventory):
# NameError: name 'rentals_inventory' is not defined