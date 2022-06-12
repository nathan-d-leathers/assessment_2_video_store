# Write your solution here!
from store import Store
# from customer import Customer

store = Store('Code Platoon Video') 

while True:
    mode = input("\n==Welcome To Code Platoon Video!==\n\n1. View Store Video Inventory\n2. View Customer Rented Videos\n3. Add a New Customer\n4. Rent a Video\n5. Return a Video\n6. Quit\n")
    if mode == '1':
        store.view_rental_list()
        # works, check output format
    if mode == '2':
        customer_id = input('Enter Customer id:')
        store.currently_rented(customer_id)
        # works:
        # possible problem with finding new members (check mdoe 3 first)
        # id 4 returns a double space response
    elif mode == '3':
        customer_data = {'id': 'new_id_num'}
        customer_data['account_type'] = input('Enter customer account type (sx,px,sf,pf):\n')
        customer_data['first_name'] = input('Enter customer first name:\n')
        customer_data['last_name'] = input('Enter customer last name:\n')
        customer_data['current_video_rentals'] = input('Enter customers first rentals seperated by slash mark /: \n')
        store.add_customer(customer_data)
        # works
        # doesnt store newly added member rentals correctly
        # doesnt return newly added member rentals(logic problem in looking for film)
        # slash mark wording on current rental data input statement
    elif mode == '4':
        user_id = input("Enter Your Customer ID:\n")
        title_search = input('Enter Movie Title:\n')
        store.rent_video(user_id,title_search)
        # basic functionality
        # will rent
        # need to add rules for 4 acct types
        # need to update inventory and user rental lists

    elif mode == '5':
        user_id = input("Enter Your Customer ID:\n")
        title_search = input('Enter Movie Title:\n')
        store.return_video(user_id,title_search)
        # working code, adds to inventory, removes from user
    elif mode == '6':
        break
        # works

# == Welcome to Code Platoon Video! ==
# 1. View store video inventory
# 2. View customer rented videos
# 3. Add new customer
# 4. Rent video
# 5. Return video
# 6. Exit

#  self,id,account_type,first_name,last_name,current_video_rentals
 
#Output 1:
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