
# import required package

import requests

# valid post-code or invalid - url of api address
url = "http://api.postcodes.io/postcodes/"

# store the data
postcode = "e147le"
url_arg = url + postcode

# display the outcome
print(type(url_arg))

# display url together with given postcode
response = requests.get(url_arg)

# check the type of data scrapped from the web - response
# convert data type if needed to iterate through the data and print requried information
# display longitude - latitue - postocde -etc

#print(f" status code of link is {response.status_code}")
#print(type(response.json()))
response_dict = response.json() # change into type of api
result_dict = response_dict ['result'] #resonse_dict = data

#print(result_dict)

# for key in result_dict.keys(): # change to indexing
#     if key == 'postcode' :
#         #print(f"please confirm this is your postcode is {result_dict.get('postcode')}")
#         print(f"please confirm this is your postcode is {result_dict[key]}")
#     elif key == 'longitude':
#         #print(f"your longitude is {result_dict.get('longitude')}")
#         print(f"your longitude is {result_dict[key]}")
#     elif key == 'latitude':
#         #print(f"your latitude is {result_dict.get('latitude')}")
#          print(f"your latitude is {result_dict[key]}")
#     else:
#         pass


# once completed - create a function to do return the required value - 1 function MUST only REtURN 1 VALUE

# def postcode():
#     for key in result_dict.keys():
#         if key == 'postcode':
#             return (f"please confirm this is your postcode {result_dict[key]}")
#
# print(postcode())
#
#
# def longitude():
#     for key in result_dict.keys():
#         if key == 'longitude':
#             return (f"your longitude is {result_dict[key]}")
#
# print(longitude())
#
# def latitude():
#     for key in result_dict.keys():
#         if key == 'latitude':
#             return (f"your latitude is {result_dict[key]}")
#
# print(latitude())



# Create a function that checks if the post code is valid - prompt the user to input the postcode

# create a class with all of these functions

class Address():
    def __init__(self):
        self.postcode  # result_dict.get('postcode')

    #def is_valid(self):
        #user_input = input('please enter your postcode ')
        #if user_input != self.postcode():
            #print("Try again as we dont recognise this")

    def postcode(self):
       for key in result_dict.keys():
            if key == 'postcode':
                return (f"please confirm this is your postcode {result_dict[key]}")

    def longitude(self):
        for key in self.result_dict.keys():
            if key == 'longitude':
                return (f"your longitude is {result_dict[key]}")

    def latitude(self):
        for key in result_dict.keys():
            if key == 'latitude':
                return (f"your latitude is {result_dict[key]}")

address_object = Address()

# print(address_object.is_valid())
# print(address_object.postcode())
# print(address_object.latitude())
# print(address_object.latitude())
