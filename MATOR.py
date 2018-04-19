#!/usr/bin/python3
import random

#The Characters List
Characters = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[];',./ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

print("MATOR Password Generator")
print("")
print("-r   Generate a Random Password List")
print("-p   Generate a Password List based on Questions about the X")
print("-i   Download a Password List from our Database")
print("     Example [mator -r abc 5 -v]")
print("")

#Password Generator
Length = input("Password Length > ")
Length = int(Length)

PasswordNumber = input("Number of Passwords > ")
PasswordNumber = int(PasswordNumber)

f= open("PasswordList.txt","w+")

for p in range(PasswordNumber):
    Password = ""
    for i in range(Length):
        Password += random.choice(Characters)
    print(Password)
    f.write(Password + "\n")

f.close()

Terminal = input("> ")