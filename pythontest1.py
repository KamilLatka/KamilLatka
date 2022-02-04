# '''
# str1 = 'James'
# print("Original String is", str1)

# # Get first character
# res = str1[0]

# # Get string size
# l = len(str1)
# # Get middle index number
# mi = int(l / 2)
# # Get middle character and add it to result
# res = res + str1[mi]

# # Get last character and add it to result
# res = res + str1[l - 1]

# print("New String:", res)
# _____________________________________________________________________________

# str1 = 'JhonDipPeta'
# str2 = 'JaSonAy'
# print("Original String is", str1)
# print("Original String is", str2)
# ## Get first character
# '''
# """
    
# # Get string size
# l = len(str1)
# # Get middle index number
# mi = int(l / 2)
# # Get middle character and add it to result
# res = str1[mi]

# # Get last character and add it to result
# res = str1[mi - 1] +res + str1[mi + 1]
# print("New String for str1:", res)
# p = len(str2)
# pi= int(p/2)
# cet=str2[pi]
# cet=str2[pi-1]+cet +str2[pi+1]
# print("new String for str2: ", cet)

# def get_middle_three_chars(str1):
#     print("Original String is", str1)

#     # first get middle index number
#     mi = int(len(str1) / 2)

#     # use string slicing to get result characters
#     res = str1[mi - 1:mi + 2]
#     print("Middle three chars are:", res)

# get_middle_three_chars("JhonDipPeta")
# get_middle_three_chars("JaSonAy")
#  """   
   

def Put_in_the_middle(s1, s2):
    print("Original String is", s1)
    
     # first get middle index number
    mi = int(len(s1) / 2)
    # get character from 0 to the middle index number from s1
    x = s1[:mi:]
    # concatenate s2 to it
    x = x + s2
    # append remaining character from s1
    x = x + s1[mi:]
    
    print("Middle three chars are:", x)

Put_in_the_middle("Ault","Kelly")

#Zadanie nr3

def some_strange_shiet(b1,b2):
    print("Original Strings are", b1, b2)
    # Get first characters
    litera1 = b1[0]+ b2[0]
    print(litera1)
    # Get last character
    literalast =b1[-1]+b2[-1]
    print(literalast)
    # first get middle index number
    l=len(b2)
    mi1 = int(len(b1) / 2)
    mi2 = int(len(b2) / 2)
    print("To jest b2 srodek",b2[mi2])
    print("To jest b1 srodek",b1[mi1])
    
    srodki= b2[mi2]+b1[mi1]
    print("to sa srodki razem",srodki)
    x =litera1+ srodki+literalast
    # append remaining character from s1
    print("Polaczone:", x)
           
some_strange_shiet("America", "Japan")

#Zadanie nr4

str1 = "PyNaTive"
print(str1)
i=str.islower(str1)
print(str.islower(str1))

while i == True:
    print("gawno")
    i=i+1

##i = 1
#while i < 10: 
#    print (i*'*')
#    i=i+1
