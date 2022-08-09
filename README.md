# Python_API

![image](https://user-images.githubusercontent.com/104793540/183609561-eff415ca-4948-4b8e-9565-d4bad170c584.png)



- import requests
- An application programming interface is a way for two or more computer programs to communicate with each other
- practice APIs

## What is an API and how to use it with requests (python package)
When you use an application on your mobile phone, the application connects to the Internet and sends data to a server. The server then retrieves that data, interprets it, performs the necessary actions and sends it back to your phone. The application then interprets that data and presents you with the information you wanted in a readable way. This is what an API is - all of this happens via API.

### Benefits 
- saves alot of time 


resources postman - postcode anything you can find on google

scrap data from any website - store it in a file.csv or dict - iterate through the data and print all values - all keys - and be able to print any info as per the user requirement as and when needed


- pip install package_name `pip install requests`
- packaged downlaoded through package install in settings 

## First Iteration 
````python
import requests

response = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")
# APPI call to bbc to get response

# print(response)

print(f"The status code is {response.status_code}") # should give us status code only

# should give us the status code only - numbers 200 - 404 -501

if response.status_code == 200:
    print( f"The status code is {response.status_code} welcome to bbc")
    #print(type(response.content)) # get the content from the web-app/endpoint

    new_str =response.content.decode('utf-8')
    print(new_str)
    import json
    a = json.dumps(new_str)
    print(type(a))
    print(a)

else:
    print( f"website is down the status code is {response.status_code}")
````
## Second Iteration
`````python 

if response: # hidden abstraction
    print("success")
elif response:
    print("unsuccessfull")
else:
    print("oops something went wrong, please try later")
````