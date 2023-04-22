# Introduction to Class

from multiprocessing import Value


class Phone:
    "Simple Class for test" # This can be done to define the class idea USED in LINE 19.
    
    phone_version = "M31"
    brand_name = "Samsung"
    user_name = ""

    model = "M31s"


    # When we need data from the class getter helps in the task
    def get_model(self):
        # return self.model
        return "M31s"
    
    # When we set data in the class setter helps 
    def set_model(self, val):
        self.model = "M31s," + val


    # Constructor
    def __init__(self, user_name):
        self.user_name = user_name

    def BootLogo(self):
        print(self.user_name,"\nSAMSUNG", self.phone_version)
    
Sandy = Phone("Sandy's Phone")
Sandy.BootLogo()

print(Sandy.__doc__)  # This is used to print the above description in : LINE 4.

# When we want to know how the data gets in the class and gets out of the class we use the getters and seters

Sandy.set_model("iPhone")
print(Sandy.get_model())


        