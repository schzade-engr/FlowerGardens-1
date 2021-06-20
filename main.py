"""
Program: Flower Garden Inventory Management
Author: Stella
Description: This application is used to manage flower gardens and their inhabitants

In this flower garden application, the following functions are included:
1) queryGardens
2) queryFlowers
3) addFlower
4) removeFlower
5) sellGarden
6) addGarden
7) searchFlowersbyKey
x) exit
"""

from replit import db # import the replit.db module

def queryGardens(db):
	print("queryGardens")
	
	list = []
	newGarden = ""
	keyList = db.keys()
	print(len(keyList))
	if len(keyList) == 0:
		print("You currently have no gardens")
		newGarden = input("Please provide a name of your first garden: ")
		db[newGarden] = []

	print("Here is a list of all the current gardens: ")
	for key in db.keys():
		list.append(key)
	for x in range(len(list)):
		print(str(x) + ": " + list[x])

def sellGarden(db):
	print("sellGarden")
	queryGardens(db)
	flowerGarden = input("Enter which flower garden: ")
	sellGarden = input("Do you want to sell this garden? ")
	if (sellGarden.upper() == "YES"):
		if flowerGarden in db.keys():
			db[flowerGarden] = []
			del db[flowerGarden]
			print("Sold!")

#function addGarden takes in the database that contains the gardens
#the function then calls queryGardens which prints out the list of all
#of the current gardens. Then the user is prompted for a name for the
#new garden. A new garden is added to the database by creating an array,
# the new garden is returned to the caller.
def addGarden(db):
	print("addGarden")
	queryGardens(db)
	whichGarden = input("Please use a name currently not in use: ")
	db[whichGarden] = []
	return(db[whichGarden])
	

def printGarden(newGarden):
	print("printGarden")
	for x in range(len(newGarden)):
		flowerTemp = newGarden[x]
		print("")
		print("Flower " + str(x) + ":")
		for key, value in flowerTemp.items():
			print(key, " : " , value)
		

#This function addFlower takes in an array newGarden
# so it will add the new flower to that array. The function
# creates an empty dictionary item and prompts the User 
# to describe the flower's attributes. Those attributes 
# are updated in the dictionary item and added to the 
# array and prints out the updated garden.

def addFlower(newGarden):
	print("addFlower")
	
	flowerTemp = {}
	scent = input("Scent: ")
	typeF = input("What type of flower? ")
	size = input("What size flower? ")
	color = input("Color? ")
	flowerID = input("Flower ID: ")
	HMSun = input("How much sun does it need? ")
	flowerTemp["scent"] = scent
	flowerTemp["typeF"] = typeF
	flowerTemp["size"] = size
	flowerTemp["color"] = color
	flowerTemp["flowerID"] = flowerID
	flowerTemp["HMSun"] = HMSun
	newGarden.append(flowerTemp)
	printGarden(newGarden)
	return(newGarden)
	

def removeFlowerByID(newGarden, whichRemove):
	print("removeFlowerByID")
	
	flowerTemp = {}
	for x in range(len(newGarden)):
		flowerTemp = newGarden[x]
		if (flowerTemp.get("flowerID") == whichRemove):
			print("Found " + str(whichRemove))
			print()
			newGarden.pop(x)
			break
	return(newGarden)
	

def queryFlowers(newGarden):
	print("queryFlowers")
	flowerTemp = {}
	print("")
	for x in range(len(newGarden)):
		flowerTemp = newGarden[x]
		print("Flower " + str(x) + ":")
		for key, value in flowerTemp.items():
			print(key, " : " , value)
		print("")
	return()

#Def: searchCarsbyKey
#parameter1: newLot : array variable containing
#the carlot
#parameter2: myKey : string variable as provided 
#from user prompt with the key to be using for 
#the search
#parameter3: myValue : string variable as provided 
#from user prompt with the value to be using for 
#the search
#Descr: this function uses the key and value 
#provided by the user and returns the matching 
#dictionary if one was found.

def searchCarsbyKey(newLot, myKey, myValue):
	print("searchCarsbyKey")
	"""
	carTemp = {}
	cars = []
	printCar = 0
	
	for x in range(len(newLot)):
		printCar = 0
		carTemp = newLot[x]
		for key, value in carTemp.items():
			if((key == myKey) and (value == myValue)):
				printCar = 1
				cars.append(carTemp)
		if(printCar ==1):
			print("Car " + str(x) + ":")
			for key, value in carTemp.items():
				print(key, " : " , value)
		#stop here
		print("")
	#print(cars)
	return(cars)	
	"""

def printOne(thisCar, which):
	print("printOne")
	for key, value in thisCar.items():
		if(which == "key"):
			print(key)
		else:
			print(value)

# Initialize the car lot inventory by getting the values from the datastore

runProgram = "0"
newLot = []
print("Welcome to the Flower Garden Inventory")
queryGardens(db)
print("Here are your list of options\n")

while(runProgram.upper() != "X"):
	print("")
	print("To get a list of your gardens, enter 1")
	print("To get a list of flowers in a garden, enter 2")
	print("To add a flower to a garden, enter 3")
	print("To remove a flower from a garden by flower ID, enter 4")
	print("To sell a garden, enter 5")
	print("To add a new garden, enter 6")
	print("To search for a flower based on a key and value, enter 7")
	print("To exit this program, enter X")

	runProgram = input("What would you like to do? ")
	#print list of lots
	if(runProgram == "1"):
		queryGardens(db)
	#print cars in a lot
	elif(runProgram == "2"):
		whichGarden = input("Which garden would you like to look at? ")
		queryFlowers(db[whichGarden])
	#add car to a lot
	elif(runProgram == "3"):
		whichGarden = input("Which garden would you like to add the flower to? ")
		if (whichGarden not in db.keys() ):
			print("This car lot doesn't exist")
		else:
			addFlower(db[whichGarden])
	#remove a car from a lot based on its car ID
	elif(runProgram == "4"):
		rmFlowerID = input("Provide the flower ID that you want to remove ")
		whichLot = input("Which garden would you like to remove the flower from? ")
		newGarden = removeFlowerByID(db[whichGarden], rmFlowerID)
		db[whichGarden] = newGarden

	#remove a lot
	elif(runProgram == "5"):
		sellGarden(db)
	#add a lot
	elif(runProgram == "6"):
		addGarden(db)
	#exit the program
	elif(runProgram == "7"):
		whichLot = input("Which lot would you like to look at? ")
		thisLot = db[whichLot]
		printOne(thisLot[0], "key")
		myKey = input("Enter search key: ")
		#printOne(thisLot[0], "value")
		myValue = input("Enter compare value: ")
		searchCarsbyKey(db[whichLot], myKey, myValue )
	elif(runProgram.upper() == "X"):
		print("Goodbye")
		break
	else:
		print("That value is not supported, choose another value")
