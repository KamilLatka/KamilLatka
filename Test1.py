import os  
os.system('cls')
Weight = float(input("Weight: "))
conversion = input("KG or L: ")
lbs = 2.2

if conversion.upper() == "KG":
    print("Weightin KG:" + str(Weight))
else:
  #  conversion.upper() == "L":
    print("Weight in lbs:" + str(Weight*lbs))
print("done")    
