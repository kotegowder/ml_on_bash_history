import os
from glob import glob

database = {}

users = glob("/home/*")
#print(users)

for user in users:
    try:
        with open(user+"/.bash_history", 'r') as user_bash_history:
            user_bash_details = []
            for command in user_bash_history:
                user_bash_details.append(command)
            database.update({user:user_bash_details})
    except IOError:
        print("No .bash_history found for user " + user)

def print_database():
    for user in database:
        print(user)
        print(database[user])
        print("\n")

print_database()
