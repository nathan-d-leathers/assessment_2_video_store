from video import Video
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
        if str(customer_id) in Store.active_member_list:
            for rental in self.rental_members:
                if customer_id == rental.id:
                    film_list = ", ".join(rental.current_video_rentals)
                    if film_list == '':
                        print("\nNo Current Rentals Under This Account\n")
                    else:
                        print(f"\nCurrent Rentals under this Account:\n{film_list}\n")
                        break
            return self.rental_members
        else:
            print(f"\nMember ID: {customer_id} is not valid.\nPlease create a new account to rent videos.")
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
        Store.active_member_list.append(new_customer.id)
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
        elif str(user_id) not in Store.active_member_list:
            print(f"\nMember ID: {user_id} is not valid.\nPlease create a new account to rent videos.")
        elif title_search.lower() not in Store.current_video_inventory:
            cap_title = title_search.lower().title()
            print(f'\n"{cap_title}"" is not currently available at this location.\nPlease enter another movie title')
    # working code
    # make a return statement for if no title was found (maybe before?)


    def return_video(self,user_id,title_search):
        if str(user_id) in Store.active_member_list and title_search.lower() in Store.current_video_inventory:
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
        elif str(user_id) not in Store.active_member_list:
            print(f"\nMember ID: {user_id} is not valid.\nPlease create a new account to rent videos.")
        elif title_search.lower() not in Store.current_video_inventory:
            cap_title = title_search.lower().title()
            print(f'\n"{cap_title}" was not rented from this location')
        # working code 
        # should add condtion if film not on file




# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# bobs_store = Store('bo bo\'s film emporium')
# print(bobs_store.current_video_inventory)
# ['Toy Story', 'WALL-E', 'Up', 'Inside Out', 'The Prestige', 'The Dark Knight', 'Inception', 'Intersteller', 'Deadpool', 'The Godfather']
# print(bobs_store.active_member_list)
# ['1', '2', '3', '4', '5', '6']
