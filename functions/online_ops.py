# online function to be executed 
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

def findMyIP():
    ip_address = request.get("https://api64.ipify.org/?format=json").json()
    return ip_address["ip"]

def serarchOnWikipedia(query):
    return wikipedia.summary(query, sentences=2)

def playOnYoutube():
    kit.playonyt(video)

def searchOnGoogle(query):
    kit.search(query)

def sendWhatsAppMessage(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def getRandomJoke():
    header = {
                "Accept" : "application/json"
            }
    response = request.get("https://icanhazdadjoke.com/", headers=header).json()
    return response["joke"]
