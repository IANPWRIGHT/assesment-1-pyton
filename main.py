#Programming Assessment One
#written by Ian P Wright on 26/11//2020
#asks the user wow many sofas and armchairs they want to open
#validates the impurs then reports the coft for each product devivery and total

#displays the cost for the armchair, sofa and the min and max for each item
print("Armchair Cost £350 each   Minimum = 1   Maximum = 5")
print("")
print("Sofa Cost £500 each   Minimum = 0   Maximum = 3")
print("")
#displays the delivery cost
print("delivery cost £50")
print("")

#asks the user for the amount of armchairs and validates that the number is greater than 0 and less than 6
arm = int(input("Enter number of Armchair(s) you would like to order :"))
while arm <1:
  print ("a minimum order of 1 armchar is required")
  arm = int(input("Enter number of Armchair(s) you would like to order :"))
while arm >5:
  print ("a maximum of 5 armchaires orderdat a time")
  arm = int(input("Enter number of Armchair(s) you would like to order :"))

#asks the user for the amount of sofas and validates that less than 4
sof = int(input("Enter mumber of sofa(s) you would like to order:"))
while sof >3:
  print ("a maximum of 3 sofas orderd at a time")
  arm = int(input("Enter number of sofa(s) you would like to order :"))

#reports the a cost breakdown and the total price
print("costs")
print("")
print(arm, "Armchir(s) cost ",arm*250)
print("")
print(sof, "sofa(s) cost ",sof*500)
print("")
print("delivery charge 50")
print ("")
print("total cost of delivery ", (arm*250)+(sof*500)+50)