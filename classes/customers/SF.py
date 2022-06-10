from customer import Customer

class SX(Customer):
    def __init__(self,id,account_type,first_name,last_name,current_video_rentals):
        super().__init__(id,account_type,first_name,last_name,current_video_rentals)