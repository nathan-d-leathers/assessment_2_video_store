from logging import exception
from video_inventory import Video_Inventory
from customer import Customer

class Store:
    def __init__(self,name):
        self.name = name
        self.rentals_inventory = Video_Inventory.objects()
        self.rental_members = Customer.objects()
    # working code

    def view_rental_list(self):
        print('\n')
        for vid in self.rentals_inventory:
            print(f"{vid.__dict__}")
    # working code, check formatting

    def currently_rented(self,customer_id):
        for rental in self.rental_members:
            if customer_id == rental.id:
                film_list = ", ".join(rental.current_video_rentals)
                if film_list == '':
                    print("\nNo Current Rentals Under This Account")
                else:
                    print(f"\n{film_list}")
                    break
                print(f"\n{film_list}")
                break
            elif customer_id != rental.id and rental is self.rental_members[-1]:
                print("\nMember Rental ID Not On File")
    # working code, formatted correctly

    def add_customer(self,customer_data):
        new_customer = Customer(**customer_data)
        new_id = len(self.rental_members) + 1
        new_customer.id = new_id
        first_rentals = new_customer.current_video_rentals
        self.rental_members.append(new_customer)
        print(f"\nNew Customer:\n{new_customer.first_name} {new_customer.last_name}\nID Number: {new_customer.id}\nwas sucessfully added to the system.")
        if first_rentals[0] == '':
            print("\nNo Current Rentals Under This Account")
        else:
            for film in first_rentals:
                # print(film)
                for stock in self.rentals_inventory:
                    # print(stock.title)
                    # only prints once here
                    if film == stock.title:
                        print('working here!')
                        copies = int(stock.copies_available)
                        print(copies)
                        copies -= 1
                        stock.copies_available = copies
                        print(stock.copies_available)
                        break
                    break
            first_rentals_list = ", ".join(first_rentals)
            print(f"\nCurrent Rentals under this Account:\n{first_rentals_list}")
    # working code, formatted correctly
    # doesnt seem to remember new member in rental_members



    def rent_video(self,user_id,title_search):
            # maybe need to check if its in inventory before we check copies available
            last_film = self.rentals_inventory[-1]
            last_title = last_film.title.lower()
            for film in self.rentals_inventory:
                if film.title.lower() == title_search.lower() and int(film.copies_available) < 1:
                        print(f"All Copies of {film.title} are Currently Rented.")
                        break
                elif film.title.lower() == title_search.lower() and int(film.copies_available) >= 1:
                    for member in self.rental_members:
                        if member.id == user_id:
                            # at this point we have a designated film and designated member
                            current_rentals = member.current_video_rentals
                            if member.account_type == 'sx' and current_rentals[0] == '':
                                print(f"Your account type is: {member.account_type}")
                                print(f"Current Rental List: \n{member.current_video_rentals}")
                                print(f"Copies Available to Rent: \n{film.copies_available}")
                                member.current_video_rentals.append(film.title)
                                film.copies_available = int(film.copies_available) -1
                                print(f"New Rental List: \n{member.current_video_rentals}")
                                print(f"Copies Available to Rent: \n{film.copies_available}")
                                if len(current_rentals) == 2 and current_rentals[0] == '':
                                    current_rentals.remove('')
                                    print(current_rentals)
                                else:
                                    pass
                                print("Enjoy the Movie!")
                                break
                else:
                    pass
    # code is working up to this point, i have many things to do:
    # 1. make a return statement for if no title was found (maybe first step?)
    # 2. implemnt account classes somehow(static method, if elif else chain?)
    # sx functaionity removes title from inevntory 

    def return_video(self,user_id,title_search):
        proper_title = title_search.lower().title()
        for renter in self.rental_members:
            if user_id == renter.id:
                print('working here')
                rented_out = renter.current_video_rentals
                rented_out.remove(proper_title)
                print(rented_out)
                for vid in self.rentals_inventory:
                    if proper_title == vid.title:
                        print('working here too!')
                        num_copies = int(vid.copies_available)
                        print((num_copies))
                        num_copies += 1
                        vid.copies_available = num_copies
                        print(vid.copies_available)
        
# 
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-

# 4
# Enter Your Customer ID:
# 4
# Enter Movie Title:
# up
# Your account type is: sx
# Current Rental List: 
# ['']
# Copies Available to Rent: 
# 5
# New Rental List: 
# ['', 'Up']
# Copies Available to Rent: 
# 4
# ['Up']
# Enjoy the Movie!

# need to implemtn somehow
# break
# elif film.title.lower() != title_search.lower() and film.title.lower() == last_title:
#     print(f"{title_search} not available to rent at this time")
#     break

#   -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
    # # @staticmethod      
    # def check_account(user_id):
    #     for member in self.rental_members:
    #         if member.id == user_id
    #             # print(f"{film.title},{member.id},{member.account_type}")
    #             if member.account_type == 'sx':
    #                 print('this user has an standard single account')
    #                 break
    #             if member.account_type == 'px':
    #                 print('this user has an premium single account')
    #                 break
    #             elif member.account_type == 'sf':
    #                 print('this user has an standard family account')
    #                 break
    #             elif member.account_type == 'pf':
    #                 print('this user has an premium family account')
    #                 break
    #             else:
    #                 print('User does not have an activate rental account') 
    #                 break   


# bills_store = Store('81||s V1D305')
# checked = bills_store.check_account('6')
# 1. this user has an standard single account
# 2. this user has an standard single account
# 3. this user has an premium family account
# 4. this user has an standard single account
# 5. this user has an standard family account
# 6. this user has an premium single account

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# if film.title not in self.rentals_inventory: print("Film not available to rent at this time")

            # output:
            # ['WALL-E']
            # 0
            # Enjoy the Movie!
            # ['WALL-E', 'Toy Story']
            # -1
            # Film not available to rent at this time
        
            # elif film.title == title_search:
            #     # work til here
            #     for member in self.rental_members:
            #         if member.id == user_id:
            #             if member.account_type.lower() == 'sx':
            #                 print("\nthis line working1")
            #             elif member.account_type.lower() == 'px':
            #                 print("\nthis line working2")
            #             elif member.account_type.lower() == 'sf':
            #                 print("\nthis line working3")
            #             elif member.account_type.lower() == 'px':
            #                 print("\nthis line working4")
            #         else:
            #             print("No video membership on file")
                        


# for key,value in my_dict.items():
#     if value==9:


        # print('were still working onthis feature')
        # find video id
        # check int(num 0f copies) 
        # if more than 1, num -= 1
        # if 0, return unable to rent statement.
        # push it to customer rental list
        # pass

    # def return_video(self):
    #     print('were still working onthis feature')
        # find customer id
        # look for video id in customer list
        # pop it from customer rental list,
        # update num of copies in inventory
        # pass

# bobs_store = Store('Bobs Stowre')
# bobs_rentals = bobs_store.rental_members
# cust_id = 6
# # for x in bobs_rentals:
#     print(x.id)
# 1
# 2
# 3
# 4
# 5
# 6

# for x in bobs_rentals:
    # if int(x.id) == cust_id:
    #     rented_vids = x.current_video_rentals
    #     print(rented_vids)
    # print(x.id)




# Traceback (most recent call last):
#   File "/Users/nathanleathers/Desktop/git challenges/assessment-2/classes/runner.py", line 9, in <module>
#     store.view_rental_list()
#   File "/Users/nathanleathers/Desktop/git challenges/assessment-2/classes/store.py", line 11, in view_rental_list
#     for vid in enumerate(rentals_inventory):
# NameError: name 'rentals_inventory' is not defined


# -=--=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# this is a working chunk of code:

#    def rent_video(self,user_id,title_search):
#         # maybe need to check if its in inventory before we check copies available
#         last_film = self.rentals_inventory[-1]
#         last_title = last_film.title.lower()
#         for film in self.rentals_inventory:
#             if film.title.lower() == title_search.lower() and int(film.copies_available) < 1:
#                     print(f"All Copies of {film.title} are Currently Rented.")
#                     break
#             elif film.title.lower() == title_search.lower() and int(film.copies_available) >= 1:
#                 for member in self.rental_members:
#                     if member.id == user_id:
#                         print(f"Current Rental List: \n{member.current_video_rentals}")
#                         print(f"Copies Available to Rent: \n{film.copies_available}")
#                         member.current_video_rentals.append(film.title)
#                         film.copies_available = int(film.copies_available) -1
#                         print(f"New Rental List: \n{member.current_video_rentals}")
#                         print(f"Copies Available to Rent: \n{film.copies_available}")
#                         print("Enjoy the Movie!")
#                         break
#                 break
#             elif film.title.lower() != title_search.lower() and film.title.lower() == last_title:
#                 print(f"{title_search} not available to rent at this time")
#                 break

# -==-=---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# still workign on logic
#  print(member.account_type)
#                             print(len(current_rentals))
#                             print(f"Your account type is: {member.account_type}")
#                             print(f"Current Rental List: \n{member.current_video_rentals}")
#                             print(f"Copies Available to Rent: \n{film.copies_available}")
#                             member.current_video_rentals.append(film.title)
#                             film.copies_available = int(film.copies_available) -1
#                             print(f"New Rental List: \n{member.current_video_rentals}")
#                             print(f"Copies Available to Rent: \n{film.copies_available}")
#                             print(len(current_rentals))
#                             print("Enjoy the Movie!")
#                         elif member.account_type == 'sf' and len(current_rentals) == 1 and current_rentals[0] == '' and film.rating != 'R':
#                             print(f"Your account type is: {member.account_type}")
#                             print(f"Current Rental List: \n{member.current_video_rentals}")
#                             print(f"Copies Available to Rent: \n{film.copies_available}")
#                             member.current_video_rentals.append(film.title)
#                             film.copies_available = int(film.copies_available) -1
#                             print(f"New Rental List: \n{member.current_video_rentals}")
#                             print(f"Copies Available to Rent: \n{film.copies_available}")
#                             if len(current_rentals) == 2 and current_rentals[0] == '':
#                                 current_rentals.remove('')
#                                 print(current_rentals)
#                             print("Enjoy the Movie!")
#                         elif member.account_type == 'pf' and (len(current_rentals) < 3) and film.rating != 'R':
#                             print(f"Your account type is: {member.account_type}")
#                             print(f"Current Rental List: \n{member.current_video_rentals}")
#                             print(f"Copies Available to Rent: \n{film.copies_available}")
#                             member.current_video_rentals.append(film.title)
#                             film.copies_available = int(film.copies_available) -1
#                             print(f"New Rental List: \n{member.current_video_rentals}")
#                             print(f"Copies Available to Rent: \n{film.copies_available}")
#                           
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# def rent_video(self,user_id,title_search):
#         # maybe need to check if its in inventory before we check copies available
#         last_film = self.rentals_inventory[-1]
#         last_title = last_film.title.lower()
#         for film in self.rentals_inventory:
#             if film.title.lower() == title_search.lower() and int(film.copies_available) < 1:
#                     print(f"All Copies of {film.title} are Currently Rented.")
#                     break
#             elif film.title.lower() == title_search.lower() and int(film.copies_available) >= 1:
#                 for member in self.rental_members:
#                     if member.id == user_id:
#                         # at this point we have a designated film and designated member
#                         current_rentals = member.current_video_rentals
#                         if member.account_type == 'sx' and current_rentals[0] == '':
#                             print(f"Your account type is: {member.account_type}")
#                             print(f"Current Rental List: \n{member.current_video_rentals}")
#                             print(f"Copies Available to Rent: \n{film.copies_available}")
#                             member.current_video_rentals.append(film.title)
#                             film.copies_available = int(film.copies_available) -1
#                             print(f"New Rental List: \n{member.current_video_rentals}")
#                             print(f"Copies Available to Rent: \n{film.copies_available}")
#                             if len(current_rentals) == 2 and current_rentals[0] == '':
#                                 current_rentals.remove('')
#                                 print(current_rentals)
#                             else:
#                                 pass
#                             print("Enjoy the Movie!")
                            # this code works and gives us the upgrade statement when called again without returning

# -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-