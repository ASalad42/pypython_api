# create a file called postcode_checker.py
# import this file and class
# call these functions in postcode_check.py

from post_code_api import  Address

class Post(Address):
    def __init__(self):
        super().__init__()

    def hi(self):
        return "hi"

checker_object = Post()
print(checker_object.hi())
print(checker_object.postcode()) 
