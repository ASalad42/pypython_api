
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

for key in result_dict.keys(): # change to indexing
    if key == 'postcode' :
        #print(f"please confirm this is your postcode is {result_dict.get('postcode')}")
        print(f"please confirm this is your postcode is {result_dict[key]}")
    elif key == 'longitude':
        #print(f"your longitude is {result_dict.get('longitude')}")
        print(f"your longitude is {result_dict[key]}")
    elif key == 'latitude':
        #print(f"your latitude is {result_dict.get('latitude')}")
         print(f"your latitude is {result_dict[key]}")
    else:
        pass


# once completed - create a function to do return the required value - 1 function MUST only REtURN 1 VALUE

def postcode():
    for key in result_dict.keys():
        if key == 'postcode':
            return (f"please confirm this is your postcode {result_dict[key]}")

print(postcode())


def longitude():
    for key in result_dict.keys():
        if key == 'longitude':
            return (f"your longitude is {result_dict[key]}")

print(longitude())

def latitude():
    for key in result_dict.keys():
        if key == 'latitude':
            return (f"your latitude is {result_dict[key]}")

print(latitude())



# Create a function that checks if the post code is valid - prompt the user to input the postcode

# create a class with all of these functions

class Address():

# create a file called postcode_checker.py
# import this file and class
# call these functions in postcode_check.py
