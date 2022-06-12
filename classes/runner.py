# Write your solution here!
from store import Store

store = Store('Code Platoon Video') 

while True:
    mode = input("\n==Welcome To Code Platoon Video!==\n\n1. View Store Video Inventory\n2. View Customer Rented Videos\n3. Add a New Customer\n4. Rent a Video\n5. Return a Video\n6. Quit\n")
    if mode == '1':
        store.view_rental_list()
    if mode == '2':
        customer_id = input('Enter Customer id:')
        store.currently_rented(customer_id)
    elif mode == '3':
        customer_data = {'id': 'new_id_num'}
        customer_data['account_type'] = input('Enter customer account type (sx,px,sf,pf):\n')
        customer_data['first_name'] = input('Enter customer first name:\n')
        customer_data['last_name'] = input('Enter customer last name:\n')
        customer_data['current_video_rentals'] = input('Enter customers first video rentals seperated by the slash mark /: \n')
        store.add_customer(customer_data)
    elif mode == '4':
        user_id = input("Enter Your Customer ID:\n")
        title_search = input('Enter Movie Title:\n')
        store.rent_video(user_id,title_search)
    elif mode == '5':
        user_id = input("Enter Your Customer ID:\n")
        title_search = input('Enter Movie Title:\n')
        store.return_video(user_id,title_search)
    elif mode == '6':
        break

# == Welcome to Code Platoon Video! ==
# 1. View store video inventory
# 2. View customer rented videos
# 3. Add new customer
# 4. Rent video
# 5. Return video
# 6. Exit

# notes:

# -still need to add condtion for '2' if id is not on file
# -still need to add condtion for 4,5 if video is not on file
# -still need to check film inventory before asigning new rentals
# -double check formating and correct output vs sylabus and grading sheet