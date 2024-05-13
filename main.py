import requests
from colorama import init, Fore
import os

init()

# CONFIG SETTINGS
webhook_url = input(Fore.MAGENTA + "Enter the webhook URL: ")

# Function to send a message through the webhook
def send_message(message):
    data = {'content': message}
    requests.post(webhook_url, json=data)

# Function to spam a message through the webhook
def spam_message(message, times):
    for _ in range(times):
        send_message(message)

# Function to change the webhook avatar
def change_avatar(avatar_url):
    data = {'avatar_url': avatar_url}
    requests.patch(webhook_url, json=data)

# Function to change the webhook name
def change_name(name):
    data = {'name': name}
    requests.patch(webhook_url, json=data)

# BANNER
banner = """
tommyhook - webhook
enter webhook url in main.py

it for discord
so yeah

poopy


|==========================================|
    [1] - Send Message
    [2] - Spam Message (15)
    [3] - Change Avatar (Image URL)
    [4] - Change Name 
    [5] - Exit
|==========================================|
"""

print(Fore.MAGENTA + banner)

while True:
    choice = input(Fore.MAGENTA + "Enter Choice: ")

    if choice == "1":
        message = input("What do you want to say: ")
        send_message(message)
        print(Fore.GREEN + "[+] Message sent successfully!")

    elif choice == "2":
        message = input("What do you want to say: ")
        spam_message(message, 15)
        print(Fore.GREEN + "[+] Message sent successfully!")

    elif choice == "3":
        avatar_url = input("Image URL: ")
        change_avatar(avatar_url)
        print(Fore.GREEN + "[+] Avatar changed successfully!")

    elif choice == "4":
        name = input("Name: ")
        change_name(name)
        print(Fore.GREEN + "[+] Name changed successfully!")

    elif choice == "5":
        print("Logged out of webhook.")
    
        break

    else:
        print("Invalid choice. Please enter a valid option.")
