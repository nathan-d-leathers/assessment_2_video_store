from video_inventory import Video_Inventory
from customer import Customer

class Store:

    current_video_inventory = []
    active_member_list = []
    def __init__(self,name):
        self.name = name
        self.rentals_inventory = Video_Inventory.objects()
        self.rental_members = Customer.objects()
        for x in self.rentals_inventory:
            Store.current_video_inventory.append(x.title)
        for y in range(len(Store.current_video_inventory)):
            Store.current_video_inventory[y] = Store.current_video_inventory[y].lower()       
        for z in self.rental_members:
            Store.active_member_list.append(z.id)

    def view_rental_list(self):
        print('\nFull Store Video Inventory:\n')
        for vid in self.rentals_inventory:
                print(f"{vid.title}")
        print("\n\nMovies Currently Available to Rent:\n")
        for vid in self.rentals_inventory:
            if int(vid.copies_available) > 0:
                print(f"{vid.title}")
                print(f"Copies Available: {vid.copies_available}\n")
    
    def view_member_list(self):
        print('\n')
        for mem in self.rental_members:
            print(f"{mem.__dict__}")

    def currently_rented(self,customer_id):
        if str(customer_id) in Store.active_member_list:
            for rental in self.rental_members:
                if customer_id == rental.id:
                    film_list = ", ".join(rental.current_video_rentals)
                    if film_list == '': 
                        print("\nNo Current Rentals Under This Account\n")
                    else:
                        print(f"\nCurrent Rentals Under This Account:\n\n{film_list}")
                        break
            return self.rental_members
        else:
            print(f"\nMember ID: {customer_id} is not valid.\n\nPlease create a new account to rent videos.")

    def add_customer(self,customer_data):
        new_customer = Customer(**customer_data)
        new_id = len(self.rental_members) + 1
        new_customer.id = str(new_id)
        self.rental_members.append(new_customer)
        Store.active_member_list.append(new_customer.id)
        print(f"\nNew Customer:\n{new_customer.first_name} {new_customer.last_name}\nID Number: {new_customer.id}\nwas sucessfully added to the system.\n")
    
    def rent_video(self,user_id,title_search):
        if str(user_id) in Store.active_member_list and title_search.lower() in Store.current_video_inventory:
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
                                rental_string = ', '.join(current_rentals)
                                print(f"\nCurrent Rentals under this Account:\n{rental_string}")
                                print("\nEnjoy the Movie!\n")
                                break
                            elif member.account_type == 'px' and len(current_rentals) < 3:
                                member.current_video_rentals.append(film.title)
                                film.copies_available = int(film.copies_available) -1
                                rental_string = ', '.join(current_rentals)
                                print(f"\nCurrent Rentals under this Account:\n{rental_string}")
                                print("\nEnjoy the Movie!\n")
                                break
                            elif member.account_type == 'sf' and film.rating != 'R' and current_rentals[0] == '' or len(current_rentals) == 0:
                                member.current_video_rentals.append(film.title)
                                film.copies_available = int(film.copies_available) -1
                                if current_rentals[0] == '':
                                    current_rentals.remove('')
                                rental_string = ', '.join(current_rentals)
                                print(f"\nCurrent Rentals under this Account:\n{rental_string}")
                                print("\nEnjoy the Movie!\n")
                                break
                            elif member.account_type == 'pf' and film.rating != 'R' and len(current_rentals) < 3:
                                member.current_video_rentals.append(film.title)
                                film.copies_available = int(film.copies_available) -1
                                rental_string = ', '.join(current_rentals)
                                print(f"\nCurrent Rentals under this Account:\n{rental_string}")
                                print("\nEnjoy the Movie!\n")
                                break
                            else:
                                if film.rating == 'R' and member.account_type == 'sf' or member.account_type == 'pf':
                                    print("\n'R' Rated Movies Cannot be Rented Under a Family Plan Account")
                                    print("\nUpgrade Account to Rent This Movie\n")
                                else:
                                    print("\nYour Account Has Movie Rentals Outstanding.\n\nUpgrade Account or Return Previous Rentals to Rent This Movie\n")
        elif str(user_id) not in Store.active_member_list:
            print(f"\nMember ID: {user_id} is not valid.\nPlease create a new account to rent videos.")
        elif title_search.lower() not in Store.current_video_inventory:
            cap_title = title_search.lower().title()
            print(f'\n"{cap_title}"" is not currently available at this location.\nPlease enter another movie title')

    def return_video(self,user_id,title_search):
        if str(user_id) in Store.active_member_list and title_search.lower() in Store.current_video_inventory:
            proper_title = title_search.lower().title()
            for renter in self.rental_members:
                if user_id == renter.id:
                    for m in range(len(renter.current_video_rentals)):
                        renter.current_video_rentals[m] = renter.current_video_rentals[m].lower().title()
                    if title_search.lower().title() not in renter.current_video_rentals:
                        print("\nYou don't have a copy of this film to return!\n")
                        break
                    for film_title in renter.current_video_rentals:
                        if title_search.lower() == film_title.lower():
                            renter.current_video_rentals.remove(film_title)
                            for vid in self.rentals_inventory:
                                if proper_title == vid.title:
                                    num_copies = int(vid.copies_available)
                                    num_copies += 1
                                    vid.copies_available = num_copies
                                    break
                            print(f'\nYour copy of "{proper_title}" has been returned.\n\nThank you for renting with Code Platoon Video!\n')
                            break
        elif str(user_id) not in Store.active_member_list:
            print(f"\nMember ID: {user_id} is not valid.\nPlease create a new account to rent videos.\n")
        elif title_search.lower() not in Store.current_video_inventory:
            cap_title = title_search.lower().title()
            print(f'\n"{cap_title}" was not rented from this location\n')
