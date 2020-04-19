import pyinputplus as pyip
import time
Bread = ["Wheat", "White", "Sourdough"]
Bread_Prices = {"Wheat": 0.50, "White": 0.45, "Sourdough":0.75}
Protein = ["Chicken", "Turkey", "Ham", "Tofu"]
Protein_Prices = {"Chicken":1.25, "Turkey": 1.5, "Ham": 1.20, "Tofu": 1}
Cheeses = ["Mozzarella", "Cheddar", "Swiss"]
Cheeses_Prices = {"Mozzarella": 0.25, "Cheddar": 0.2, "Swiss":0.3}
other_Prices = {"Mayo": 0.05, "Tomato": 0.05, "Lettuce":0.15, "Mustard": 0.05}

Total_Price = 0

print("What type of bread would you like? ")
chosen_bread = pyip.inputMenu(Bread)
time.sleep(1)

print("What type of protein would you like? ")
chosen_protein = pyip.inputMenu(Protein)
time.sleep(1)

Ycheese = pyip.inputYesNo("Do you want cheese? (Y/N)\n")
time.sleep(1)
if Ycheese == "yes":
    print("Which cheese type?")
    chosen_cheese = pyip.inputMenu(Cheeses)
    Total_Price += Cheeses_Prices[chosen_cheese]
    time.sleep(1)



Mayo = pyip.inputYesNo("Do you want Mayo? (Y/N) \n")
time.sleep(0.5)
if Mayo == "yes":
    Total_Price += other_Prices["Mayo"]
Mustard = pyip.inputYesNo("Do you want Mustard? (Y/N) \n")
time.sleep(0.5)
if Mustard == "yes":
    Total_Price += other_Prices["Mustard"]
Lettuce = pyip.inputYesNo("Do you want Lettuce? (Y/N) \n")
time.sleep(0.5)
if Lettuce == "yes":
    Total_Price += other_Prices["Lettuce"]
Tomato = pyip.inputYesNo("Do you want Tomato? (Y/N) \n")
time.sleep(0.5)
if Tomato == "yes":
    Total_Price += other_Prices["Tomato"]

Total_Price += Bread_Prices[chosen_bread] + Protein_Prices[chosen_protein]

quantity = pyip.inputInt("How many Sandwiches would you like? ", min=1)
Total_Price *= quantity

print("Your Total Order Cost is: £ %s" % (Total_Price))