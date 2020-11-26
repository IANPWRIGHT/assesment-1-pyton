arm = int(input("Enter mumber of Armchair(s) you would like to order :"))
print(arm)


sof = int(input("Enter mumber of sofa(s) you would like to order:"))
print(sof)

print("costs")
print("")
print(arm, "Armchir(s) cost ",arm*250)
print("")
print(sof, "sofa(s) cost ",sof*500)
print("")
print("delivery charge 50")
print ("")
print("total cost of delivery ", (arm*250)+(sof*500)+50)