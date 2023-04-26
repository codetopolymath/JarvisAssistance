import requests
from functions.online_ops import *
from functions.os_ops import *
from pprint import pprint
from speechEngine import *


if __name__ == '__main__':
    greetUser()
    while True:
        query = takeUserInput().lower()
        speak(f"this is your query {query}")
        
        
