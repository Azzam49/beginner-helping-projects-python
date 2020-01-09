#! python3
'''
Create a text-based version of the program below, Ask the user to
input how many of each item are being transported across the border.
Calculate the total fine for each passenger. If they bring an item into
the country, output the action.

At Border Security, the officers are given the task of checking imported
goods and generating fines if required. The table for fines is listed below:

Item    Fine    Action
Vegetables    $40 per vegetable
fruit    $55 per fruit
Medicine    $100 per pill    Destroy
Bugs/insects    $20 per bug    Destroy
Drugs    $5000    Arrest passenger
'''

# Steps:
# 1. View the list of forbiden items to the user (print it as a table using a list with for loop)
# 2. Genearte random number of passengers with random names (use random_words module to get random names)
# 3. Allow the user to input number of items passengers having,(save the passengers on a dictonary)
# then randomly assign this items to the passengers. ( assign the items to passengers randomly)
# 4. View the fines needed to be paid by the passenger and
# take an action on the passenger if required. (calculate the fine to the passenger with fines be paid)

from random_words import RandomNicknames
import random
from pprint import pprint #Not used
import time

Items = ["Vegetables","fruit","Medicine","Bugs","Drugs"]
Fine = ["$40","$55","$100","$20","$5000"]
Action = ["None","None","Destroy","Destroy","Arrest passenger"]

rn = RandomNicknames()
Count = random.randint(10,15)
Passengers = rn.random_nicks(count=Count)

print('''
=======Welcome to Border Officer Program==
Type List to view items table~~~~~
Type Passengers to view passengers~~~~~
Type insert to input the found items~~~~~
==========================================
''')

while True:
    command = input("Your Command is : ")

    if command.lower() == "list":
        for item,fine,action in zip(Items,Fine,Action):
            print(f"Item : {item} |Fine : {fine}| Action : {action}")
        print("")


    elif command.lower() == "passengers":
        for number,passenger in enumerate(Passengers,1):
            print(f"{number}) {passenger}")
        print("")

    elif command.lower() == "insert":
        print("How many was found of each item ?")
        vegatables = input("Vegatables Found : ")
        if vegatables == "" or vegatables.isdecimal() == False:
            vegatables = "0"
            
        fruits = input("Fruits Found : ")
        if fruits == "" or fruits.isdecimal() == False:
            fruits = "0"
            
        medicines = input("Medicines Found : ")
        if medicines == "" or medicines.isdecimal() == False:
            medicines = "0"
            
        bugs = input("Bugs Found : ")
        if bugs == "" or bugs.isdecimal() == False:
            bugs = "0"
            
        drugs = input("Drugs Found : ")
        if drugs == "" or drugs.isdecimal() == False:
            drugs = "0"
        
            
        
        #Items = ["Vegetables","fruit","Medicine","Bugs","Drugs"]
        Found = [int(vegatables),int(fruits),int(medicines),int(bugs),int(drugs)]
        print("\nCreating Table ...\n")
        time.sleep(2)

        # Creating passengers+items in a Dictonary
        AssignItems = {}
        for i in range(len(Passengers)):
            AssignItems[f"{Passengers[i]}"] = [0,0,0,0,0]

        #======================================================
        # Randoming Vegatables
        VegatablesCount = Found[0]
        for i in range(VegatablesCount):
            x = random.randint(0,len(Passengers)-1)
            AssignItems[f"{Passengers[x]}"][0] += 1
            
        # Randoming Fruits
        FruitsCount = Found[1]
        for i2 in range(FruitsCount):
            x2 = random.randint(0,len(Passengers)-1)
            AssignItems[f"{Passengers[x2]}"][1] += 1
            
        # Randoming Medicines
        MedicinesCount = Found[2]
        for i3 in range(MedicinesCount):
            x3 = random.randint(0,len(Passengers)-1)
            AssignItems[f"{Passengers[x3]}"][2] += 1
            
        # Randoming Bugs
        BugsCount = Found[3]
        for i4 in range(BugsCount):
            x4 = random.randint(0,len(Passengers)-1)
            AssignItems[f"{Passengers[x4]}"][3] += 1

        # Randoming Drugs
        DrugsCount = Found[4]
        for i5 in range(DrugsCount):
            x5 = random.randint(0,len(Passengers)-1)
            AssignItems[f"{Passengers[x5]}"][4] += 1    
        #======================================================
            
        # Viewing Dictonary as a table
        print('============================================================================')
        for i in range(len(Passengers)):
            veg = AssignItems[f"{Passengers[i]}"][0]
            fru = AssignItems[f"{Passengers[i]}"][1]
            med = AssignItems[f"{Passengers[i]}"][2]
            bug = AssignItems[f"{Passengers[i]}"][3]
            dru = AssignItems[f"{Passengers[i]}"][4]
            
            print(f"{Passengers[i]}" + "\t\t\t" + f"-- V:{veg}" + f" -- F:{fru}" + f" -- M:{med}" + f" -- B:{bug}" + f" -- D:{dru}")
        print('============================================================================')
        print("Vegatables Found : " + str(VegatablesCount))
        print("Fruits : " + str(FruitsCount))
        print("Medicines : " + str(MedicinesCount))
        print("Bugs : " + str(BugsCount))
        print("Drugs : " + str(DrugsCount))
        print('============================================================================')
        print("")
        
        print("Actions to be taken! ...\n")
        time.sleep(2)

        # Gettings Fines from Passengers and taking actions
        for i in range(len(Passengers)):
            person = Passengers[i]
            vegFine = AssignItems[person][0] * 40
            fruFine = AssignItems[person][1] * 55
            medFine = AssignItems[person][2] * 100
            bugFine = AssignItems[person][3] * 20
            druFine = AssignItems[person][4] * 5000
            totalFine = vegFine + fruFine + medFine + bugFine + druFine
            print(f"Profile {person}")
            print("-----------------------")
            print("Total fine be paid for found items : {0}$".format(totalFine))

            if vegFine != 0:
                print(f"Vegatables Action : {Action[0]}")
            if fruFine != 0:
                print(f"Fruits Action : {Action[1]}")
            if medFine != 0:
                print(f"Medicines Action : {Action[2]}")
            if bugFine != 0:
                print(f"Bugs Action : {Action[3]}")
            if druFine != 0:
                print(f"Drugs Action : {Action[4]}")
            print("==========================================\n")
            time.sleep(2)

        print("")
        print("Thanks!.........Program ends here :)")
        break
    else:
        print("Invalid entry!, Try again... \n")
        continue









