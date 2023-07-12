class User:
    def __init__(self, first_name, last_name, email, age) :
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    # Display method
    def display_info (self):
        print(f"FN :{self.first_name}\nLN :{self.last_name}\nEmail :{self.email}\nAge :{self.age}\nReward Member :{self.is_rewards_member}\nGold Card Points: {self.gold_card_points}")
        return self

    # enroll
    def enroll(self):
        if self.is_rewards_member == True :
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self
    
    # Spend points
    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("Insufficient points. Cannot spend more than available.")
        return self
    
user_test1 = User("1-Melek", "kheder","blable@bla.tn", 33)
user_test2 = User("2-Anjy", "lolo", "blabaaa@zzz", 27)
user_test3 = User("3-ranim", "lulu", "haha@gigi", 30)


user_test1.spend_points(50)
user_test2.enroll()
user_test2.spend_points(80)
user_test1.display_info()
user_test2.display_info()
user_test3.display_info()