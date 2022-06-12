# from logging import exception
from video import Video
from video_inventory import Video_Inventory
from customer import Customer

class Store2:
    def __init__(self,name):
        self.name = name
        self.rentals_inventory = Video_Inventory.objects()
        self.rental_members = Customer.objects()
    # working code

    def view_rental_list(self):
        print('\n')
        for vid in self.rentals_inventory:
            print(f"{vid.__dict__}")
    # working code
    

    def view_member_list(self):
        print('\n')
        for mem in self.rental_members:
            print(f"{mem.__dict__}")
    # working code

    def currently_rented(self,customer_id):
        for rental in self.rental_members:
            if customer_id == rental.id:
                film_list = ", ".join(rental.current_video_rentals)
                if film_list == '':
                    print("\nNo Current Rentals Under This Account\n")
                else:
                    print(f"\nCurrent Rentals under this Account:\n{film_list}\n")
                    break
        return self.rental_members
    # working code
    # Still need "ID Not On File" condtion

    def add_customer(self,customer_data):
        new_customer = Customer(**customer_data)
        new_id = len(self.rental_members) + 1
        new_customer.id = str(new_id)
        first_rentals = new_customer.current_video_rentals
        for i in range(len(first_rentals)):
            first_rentals[i] = first_rentals[i].lower().title()
        new_customer.current_video_rentals = first_rentals
        self.rental_members.append(new_customer)
        print(f"\nNew Customer:\n{new_customer.first_name} {new_customer.last_name}\nID Number: {new_customer.id}\nwas sucessfully added to the system.\n")
        if first_rentals[0] == '':
            print("\nNo Current Rentals Under This Account\n")
        else:
            for film in first_rentals:
                for stock in self.rentals_inventory:
                    if film == stock.title:
                        copies = int(stock.copies_available)
                        copies -= 1
                        stock.copies_available = copies
            first_rental_string = ", ".join(first_rentals)
            print(f"\nCurrent Rentals under this Account:\n{first_rental_string}\n")
        return self.rental_members
        # working code!
        # check if movie is in list before adding to rental list
    
    def rent_video(self,user_id,title_search):
            for film in self.rentals_inventory:
                if film.title.lower() == title_search.lower() and int(film.copies_available) < 1:
                        print(f"\nAll Copies of {film.title} are Currently Rented.\n")
                        break
                elif film.title.lower() == title_search.lower() and int(film.copies_available) >= 1:
                    for member in self.rental_members:
                        if member.id == user_id:
                            current_rentals = member.current_video_rentals
                            if member.account_type == 'sx' and current_rentals[0] == '' or len(current_rentals) == 0:
                                member.current_video_rentals.append(film.title)
                                film.copies_available = int(film.copies_available) -1
                                if current_rentals[0] == '':
                                    current_rentals.remove('')
                                print("\nEnjoy the Movie!\n")
                                break
                            elif member.account_type == 'px' and len(current_rentals) < 3:
                                member.current_video_rentals.append(film.title)
                                film.copies_available = int(film.copies_available) -1
                                print("\nEnjoy the Movie!\n")
                                break
                            elif member.account_type == 'sf' and film.rating != 'R' and current_rentals[0] == '' or len(current_rentals) == 0:
                                member.current_video_rentals.append(film.title)
                                film.copies_available = int(film.copies_available) -1
                                if current_rentals[0] == '':
                                    current_rentals.remove('')
                                print("\nEnjoy the Movie!\n")
                                break
                            elif member.account_type == 'pf' and film.rating != 'R' and len(current_rentals) < 3:
                                member.current_video_rentals.append(film.title)
                                film.copies_available = int(film.copies_available) -1
                                print("\nEnjoy the Movie!\n")
                                break
                            else:
                                print("\nUpgrade Account to Rent This Movie\n")
            # this is where condtion will go
    # working code
    # make a return statement for if no title was found (maybe before?)


    def return_video(self,user_id,title_search):
        proper_title = title_search.lower().title()
        for renter in self.rental_members:
            if user_id == renter.id:
                rented_out = renter.current_video_rentals
                for rented_movie in rented_out:
                    proper_rented_title = rented_movie.lower().title()
                    if proper_title == proper_rented_title:
                        rented_out.remove(rented_movie)
                for vid in self.rentals_inventory:
                    if proper_title == vid.title:
                        num_copies = int(vid.copies_available)
                        num_copies += 1
                        vid.copies_available = num_copies
        print(f'Your copy of "{proper_title}" has been returned. Thank you for renting with Code Platoon Video!')
        # working code       

bobs_store = Store2("Bobby's Crazy Video Shack")
bobs_store.currently_rented('5')
bobs_store.return_video('5','wall-e')
bobs_store.currently_rented('5')
print(bobs_store.rental_members[4].__dict__)
bobs_store.rent_video('5','up')
bobs_store.currently_rented('5')
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# ***

# code working as of Sunday Morning at 10:00
# copy in case things stop working

# from video import Video
# from video_inventory import Video_Inventory
# from customer import Customer

# class Store2:
#     def __init__(self,name):
#         self.name = name
#         self.rentals_inventory = Video_Inventory.objects()
#         self.rental_members = Customer.objects()
#     # working code

#     def view_rental_list(self):
#         print('\n')
#         for vid in self.rentals_inventory:
#             print(f"{vid.__dict__}")
#     # working code
    

#     def view_member_list(self):
#         print('\n')
#         for mem in self.rental_members:
#             print(f"{mem.__dict__}")
#     # working code

#     def currently_rented(self,customer_id):
#         for rental in self.rental_members:
#             if customer_id == rental.id:
#                 film_list = ", ".join(rental.current_video_rentals)
#                 if film_list == '':
#                     print("\nNo Current Rentals Under This Account\n")
#                 else:
#                     print(f"\nCurrent Rentals under this Account:\n{film_list}\n")
#                     break
#             # elif customer_id != rental.id and rental is self.rental_members[-1]:
#             #     print("\nMember Rental ID Not On File")
#         return self.rental_members
#     # working code
#     # still need to print a statement for 4. ''

#     def add_customer(self,customer_data):
#         new_customer = Customer(**customer_data)
#         new_id = len(self.rental_members) + 1
#         new_customer.id = str(new_id)
#         first_rentals = new_customer.current_video_rentals
#         self.rental_members.append(new_customer)
#         print(f"\nNew Customer:\n{new_customer.first_name} {new_customer.last_name}\nID Number: {new_customer.id}\nwas sucessfully added to the system.\n")
#         if first_rentals[0] == '':
#             print("\nNo Current Rentals Under This Account\n")
#         else:
#             for film in first_rentals:
#                 for stock in self.rentals_inventory:
#                     if film == stock.title:
#                         copies = int(stock.copies_available)
#                         copies -= 1
#                         stock.copies_available = copies
#             first_rentals_list = ", ".join(first_rentals)
#             print(f"\nCurrent Rentals under this Account:\n{first_rentals_list}\n")
#         return self.rental_members
#         # working code!
#         # need to remove from availabel inventory movies added to new cust current rental list
#         # str() added to id count!
    
#     def rent_video(self,user_id,title_search):
#             # maybe need to check if its in inventory before we check copies available
#             last_film = self.rentals_inventory[-1]
#             last_title = last_film.title.lower()
#             for film in self.rentals_inventory:
#                 if film.title.lower() == title_search.lower() and int(film.copies_available) < 1:
#                         print(f"\nAll Copies of {film.title} are Currently Rented.\n")
#                         break
#                 elif film.title.lower() == title_search.lower() and int(film.copies_available) >= 1:
#                     for member in self.rental_members:
#                         if member.id == user_id:
#                             # at this point we have a designated film and designated member
#                             current_rentals = member.current_video_rentals
#                             if member.account_type == 'sx' and current_rentals[0] == '':
#                                 print(f"Your account type is: {member.account_type}")
#                                 print(f"Current Rental List: \n{member.current_video_rentals}")
#                                 print(f"Copies Available to Rent: \n{film.copies_available}")
#                                 member.current_video_rentals.append(film.title)
#                                 film.copies_available = int(film.copies_available) -1
#                                 print(f"New Rental List: \n{member.current_video_rentals}")
#                                 print(f"Copies Available to Rent: \n{film.copies_available}")
#                                 if len(current_rentals) == 2 and current_rentals[0] == '':
#                                     current_rentals.remove('')
#                                     print(current_rentals)
#                                 else:
#                                     pass
#                                 print("\nEnjoy the Movie!\n")
#                                 break
#                 else:
#                     pass
#     # code is working up to this point, i have many things to do:
#     # 1. make a return statement for if no title was found (maybe first step?)
#     # 2. implemnt account classes somehow(static method, if elif else chain?)


#     def return_video(self,user_id,title_search):
#         proper_title = title_search.lower().title()
#         for renter in self.rental_members:
#             if user_id == renter.id:
#                 print('working here')
#                 rented_out = renter.current_video_rentals
#                 rented_out.remove(proper_title)
#                 print(rented_out)
#                 for vid in self.rentals_inventory:
#                     if proper_title == vid.title:
#                         print('working here too!')
#                         num_copies = int(vid.copies_available)
#                         print((num_copies))
#                         num_copies += 1
#                         vid.copies_available = num_copies
#                         print(vid.copies_available)




# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# bobs_store = Store2("Bobby's Crazy Video Shack")
# bobs_store.view_member_list()
# bobs_store.view_rental_list()
# customer_data = {'id': '7', 'account_type': 'px', 'first_name': 'Nate', 'last_name': 'Leathers', 'current_video_rentals': 'up/deadpool'}
# bobs_store.add_customer(customer_data)
# bobs_store.view_member_list()
# bobs_store.view_rental_list()
# bobs_store.currently_rented('2')
# bobs_store.currently_rented('4')
# bobs_store.currently_rented('7')
# bobs_store.rent_video('4','Deadpool')
# bobs_store.currently_rented('4')
# bobs_store.view_rental_list()
# bobs_store.return_video('4','Deadpool')
# bobs_store.currently_rented('4')
# bobs_store.view_rental_list()

# output:

# -member list before new customer added-

# {'id': '1', 'account_type': 'sx', 'first_name': 'Monica', 'last_name': 'Gellar', 'current_video_rentals': ['The Godfather']}
# {'id': '2', 'account_type': 'px', 'first_name': 'Chandler', 'last_name': 'Bing', 'current_video_rentals': ['The Dark Knight', 'Inception', 'The Prestige']}
# {'id': '3', 'account_type': 'pf', 'first_name': 'Rachel', 'last_name': 'Green', 'current_video_rentals': ['Inside Out', 'WALL-E', 'The Prestige']}
# {'id': '4', 'account_type': 'sx', 'first_name': 'Ross', 'last_name': 'Gellar', 'current_video_rentals': ['']}
# {'id': '5', 'account_type': 'sf', 'first_name': 'Phoebe', 'last_name': 'Buffay', 'current_video_rentals': ['WALL-E']}
# {'id': '6', 'account_type': 'px', 'first_name': 'Joey', 'last_name': 'Tribbiani', 'current_video_rentals': ['Deadpool', 'The Godfather']}



# -current rental inventory-

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

# Note: 
# Up, copies: 5
# Deadpool, copies: 3



# -Newly added customer-

# New Customer:
# Nate Leathers
# ID Number: 7
# was sucessfully added to the system.

# Current Rentals under this Account:
# Up, Deadpool



# -updated member list-

# {'id': '1', 'account_type': 'sx', 'first_name': 'Monica', 'last_name': 'Gellar', 'current_video_rentals': ['The Godfather']}
# {'id': '2', 'account_type': 'px', 'first_name': 'Chandler', 'last_name': 'Bing', 'current_video_rentals': ['The Dark Knight', 'Inception', 'The Prestige']}
# {'id': '3', 'account_type': 'pf', 'first_name': 'Rachel', 'last_name': 'Green', 'current_video_rentals': ['Inside Out', 'WALL-E', 'The Prestige']}
# {'id': '4', 'account_type': 'sx', 'first_name': 'Ross', 'last_name': 'Gellar', 'current_video_rentals': ['']}
# {'id': '5', 'account_type': 'sf', 'first_name': 'Phoebe', 'last_name': 'Buffay', 'current_video_rentals': ['WALL-E']}
# {'id': '6', 'account_type': 'px', 'first_name': 'Joey', 'last_name': 'Tribbiani', 'current_video_rentals': ['Deadpool', 'The Godfather']}
# {'id': 7, 'account_type': 'px', 'first_name': 'Nate', 'last_name': 'Leathers', 'current_video_rentals': ['Up', 'Deadpool']}

# note: new customer data added and retrieved



# -new rental inventory list-

# {'id': '1', 'title': 'Toy Story', 'rating': 'G', 'release_year': '1995', 'copies_available': '0'}
# {'id': '2', 'title': 'WALL-E', 'rating': 'G', 'release_year': '2008', 'copies_available': '2'}
# {'id': '3', 'title': 'Up', 'rating': 'G', 'release_year': '2009', 'copies_available': 4}
# {'id': '4', 'title': 'Inside Out', 'rating': 'PG', 'release_year': '2015', 'copies_available': '1'}
# {'id': '5', 'title': 'The Prestige', 'rating': 'PG-13', 'release_year': '2006', 'copies_available': '2'}
# {'id': '6', 'title': 'The Dark Knight', 'rating': 'PG-13', 'release_year': '2008', 'copies_available': '3'}
# {'id': '7', 'title': 'Inception', 'rating': 'PG-13', 'release_year': '2010', 'copies_available': '4'}
# {'id': '8', 'title': 'Intersteller', 'rating': 'PG-13', 'release_year': '2014', 'copies_available': '2'}
# {'id': '9', 'title': 'Deadpool', 'rating': 'R', 'release_year': '2016', 'copies_available': 2}
# {'id': '10', 'title': 'The Godfather', 'rating': 'R', 'release_year': '1972', 'copies_available': '0'}

# Note: 
# Up, copies: 4
# Deadpool, copies: 2


# -currently rented videos for member 2-
# Current Rentals under this Account:
# The Dark Knight, Inception, The Prestige

# -currently rented videos for member 4-
# No Current Rentals Under This Account

# -currently rented videos for member 7-
# Current Rentals under this Account:
# Up, Deadpool



# -renting a movie under account 4-
# rented Deadpool and subtracted avilable copies



# -checking current rentals under account 4-
# Current Rentals under this Account:
# Deadpool



# -checking rental list ineventory-
# {'id': '9', 'title': 'Deadpool', 'rating': 'R', 'release_year': '2016', 'copies_available': 1}
# sucessfully subtracted coppy from inventory
# deadpool copies: 1


# -return a video under account 4-
# No Current Rentals Under This Account

# -checking inventory after returning Video-
# {'id': '9', 'title': 'Deadpool', 'rating': 'R', 'release_year': '2016', 'copies_available': 2}
# sucessfully added copy back to inventory

# ***
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=