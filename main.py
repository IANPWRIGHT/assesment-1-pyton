print("Armchair Cost £350 each   Minimum = 1   Maximum = 5")
print("")
print("Sofa Cost £500 each   Minimum = 0   Maximum = 3")
print("")
print("delivery cost £50")
print("")


arm = int(input("Enter number of Armchair(s) you would like to order :"))
while arm <1:
  print ("a minimum order of 1 armchar is required")
  arm = int(input("Enter number of Armchair(s) you would like to order :"))
while arm >5:
  print ("a maximum of 5 armchaires orderdat a time")
  arm = int(input("Enter number of Armchair(s) you would like to order :"))


sof = int(input("Enter mumber of sofa(s) you would like to order:"))
while sof >3:
  print ("a maximum of 3 sofas orderd at a time")
  arm = int(input("Enter number of sofa(s) you would like to order :"))


print("costs")
print("")
print(arm, "Armchir(s) cost ",arm*250)
print("")
print(sof, "sofa(s) cost ",sof*500)
print("")
print("delivery charge 50")
print ("")
print("total cost of delivery ", (arm*250)+(sof*500)+50)