from store import Store

store = Store('Code Platoon Video') 

while True:
    mode = input("\n\n==Welcome To Code Platoon Video==\n\n====Please Select Your Option====\n\n1. View Store Video Inventory\n2. View Customer Rented Videos\n3. Add a New Customer\n4. Rent a Video\n5. Return a Video\n6. Quit\n")
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
        customer_data['current_video_rentals'] = ''
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
        print("\n==Thank You For Renting At Code Platoon Video==\n")
        print("=============Have a Great Day!=================\n")
        break

