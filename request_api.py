

import requests

response = requests.get("https://www.bbc.co.uk/iplayer/live/bbcne")
# APPI call to bbc to get response

# print(response)

print(f"The status code is {response.status_code}") # should give us status code only

# should give us the status code only - numbers 200 - 404 -501

if response.status_code == 200:
    #print( f"The status code is {response.status_code} welcome to bbc")
    #print(type(response.content)) # get the content from the web-app/endpoint

    new_str =response.content.decode('utf-8')
    #print(new_str)
    import json
    a = json.dumps(new_str)
    print(type(a))
    #print(a)

#else:
    #print( f"website is down the status code is {response.status_code}")



# second iteration
#if response: # hidden abstraction
    #print("success")
#elif response:
    #print("unsuccessfull")
#else:
   # print("oops something went wrong, please try later")



# Third Iteration

# create a function that returns status code with appropiate message
# use control flow to make the right decision
# USE RETURN not print inside your function

def message():

    if response: # my condition is True when correct so stops here, if false goes to next condition
        return "success"
    elif response.status_code == 404: # next condition checked, if not met finally gone to else
        return "unsuccessfull"
    else:
        return "oops something went wrong, please try later"

# message() - is me calling the function which has returned something (in this example a response) and print just shows me this - (otherwise its excecuted in the background)
print(message())


# none = function not returning the return