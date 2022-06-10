from customer import Customer

class SX(Customer):
    def __init__(self,id,account_type,first_name,last_name,current_video_rentals):
        super().__init__(id,account_type,first_name,last_name,current_video_rentals)

# def __init__(self, name):
#         parent_instance = super()
#         parent_instance.__init__(name)
        
#         self.is_premium = False
        
#     def add_post(self, post):
#         if self.post_count >= 2:
#             print('Post count limited to 2, upgrade to Premium to post more!\n')
#         else:
#             super().add_post(post)