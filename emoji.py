"""
#for loop

for x in range (5, 10):
    print(x)  #this print all number between 5 to 10


for x in range (5,20,3):
    print (x) # this print all numbers with different of 3 between 5 and 20



prices = [10, 20,30]
total = 0
for price in prices:
    total += price
print(f"total is {total}")




for x in range(4):
    for y in range(3):
        print (f"({x}, {y})")




number= [5, 2, 5, 2, 2]
for x_count in number:
    output = ""
    for count in range(x_count):
       output += 'x'
    print(output)


    x = 2
print(x)  



#LIST
#find the largest number in this list

numb = [20,12,56,87,23]
max = numb[0]

for num in numb:
    if num > max:
        max = num
    
print(max)



# sum all item in the list
numb = [20,12,56,87,23]
total = 0
for num in numb:
    total += num
print(total)

#or
total= sum(numb)
print(total)



#2d list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][2])  # [1]-> is the second list, [2]-> is the index 2 odf the second list

matrix [2][1] = 20
print(matrix)  # it will replace item in list 3 index 1 which is 8 by 20. [[1, 2, 3], [4, 5, 6], [7, 20, 9]]

# print all items in the above matrix with nested loop
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for item in row:
        print(item)



#list operation
num = [1,2,3,4,5,6,7,8,9]
num.append(20)
print(num)

num.insert(3,15)
print(num)
#or
num[3]=15
print(num)

num.remove(2) 
print(num)

num.clear() #to clar all items in a list
print(num)

num = [1,2,3,4,5,6,7,8,9]
num.pop() 
print(num)

print(num.index(6))  # this print the value in index 6
print(50 in num) #to check the existence of a particular number in the list
print(4 in num)
num.append(50 )
print(num.count(5))

num2 = num.copy() #this copy the original list, into anew list called num2
print(num2)

num.append(27)
print(num)
num2.append(29)
print(num2)


# remove all the duplicate in the list
duplicate = [20,12,20,65,78,12]
unique=[]
for items in duplicate:
    if items not in unique:
        unique.append(items)
print(unique)


#UNPACKING
cord = (20,12,20)
x ,y,z =cord
print(x,y,z)



#DICTIONARY

customer = {
    "name" : "john smith",
    "age" : 30,
    "verified" : True
}
print(customer["name"])
print(customer["age"])
print(customer["verified"])
print(customer.get("verified"))
 #to update value of a key


customer["name"] = "jack smott"
print(customer["name"])

#TO ADD A NEW KEY:VALUE TO THE DICTIONARY

customer["birthdate"] =" jan 1st 1980"
print(customer)



#PRINT THE INPUT NUMBER IN WORD
phone = input("phone: ")
num = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}
output = ""
for ch in phone:
    output = output + num.get(ch, "!") + " "
print(output)
"""

# EMOJI CONVERTER

message = input("> ")
word = message.split(" ")
emojis = {":)": "$", ":(": "#"}
output = ""
for word in message:
    output += emojis.get(message, word) + " "
print(output)
