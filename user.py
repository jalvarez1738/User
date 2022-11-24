from email.policy import default


class User:
    default1 = "is_rewards_member"
    default2 = "gold_card_points"

    default1 = False
    default2 = 0
    
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.ago = age

display_info(self)
enroll(self)
spend_points(self, amount)