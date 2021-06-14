# hey dany. i hope this helps
#^^^ also you can use this as the string it asks you for
# or this one :
# 1234567890
# so you can understand what happens to the order much better

#strings

string = input("Enter your string has to contain a so it doesnt give error: ")

print(string.capitalize())

print("")

print(string.upper())

print("")

print(string.lower())

if string.isdigit():
    print("the string is comprised of digits only with no symbol nor alpha")
elif string.isalpha():
    print("the string may contain only alphabetic letter with no numbers nor symbol")
elif string.isalnum():
    print("the string may contain both alphabetic letter and numbers")
else:
    print("the string contains symbol too!")
print("")

#first element only
print(string[0])

print("")

#between the first and 5 element
print(string[:5])

print("")

#if you want to skip elements put the step after the 2 colon
#also you can leave the first and second colon with nothing
print(string[::2])

print("")

#revrse the string
#notice how the step is -1 which basically means it starts going down rather than up
print(string[::-1])

print("")

#you can find the index of a certin charecter in a string by :
print("first occurance of \"a\" happens at", string.index("a")) # if there is no "a" inside the string then python will show an error

print("")

# if no a is there the function  wont remove anything
print(string.replace("a", "b"))

print("")

#also you see the length of most variable whether they are strings lists or anything:
print(len(string))

print("")

#also looping over the string
for i in range(len(string)):
    print(string[i])

#there are way more function related to strings but we didnt take them
#if you want to learn on your own you can go to this site for more answers
#https://www.w3schools.com/python/python_strings.asp


#lists

# ["abdalrhman", "dany", "ahmed", "laith", "mohammad", "saif"]
#^^^ also you can use this as the string it asks you for
# or this one :
# ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# so you can understand what happens to the order much better


#we put eval so that python treats this as a list rather than a string
listofstudents = eval(input("enter your list in this format\n[\"first element\", \"second...\"]\n"))

print("")

#this turns the list into a string where inbetween the different elements it will have whatever is inside the string
print("***".join(listofstudents))

print("")

#you can also create a list from a string by spliting it everytime it finds a charecter that you give
print("Dany Fawaz".split(" ")) # in this example the result will be ["Dany", "Fawaz"]

print("")

#indexing works the same as strings
#first element only
print(listofstudents[0])

print("")

#between the first and 3 element
print(listofstudents[:3])

print("")

#if you want to skip elements put the step after the 2 colon
#also you can leave the first and second colon with nothing
print(listofstudents[::2])

print("")

#revrse the list
#notice how the step is -1 which basically means it starts going down rather than up
print(listofstudents[::-1])

print("")

#ofc you can access the list at any index and change it
listofstudents[1] = "changed!!"
print(listofstudents)

print("")

#inserts            index    value
#                     ↓        ↓
listofstudents.insert(2, "i am inserted at two")
print(listofstudents)

print("")

#append
listofstudents.append("iam added to the end")
print(listofstudents)

print("")

#removing the last element
listofstudents.pop()
print(listofstudents)

print("")

# and the 4 element
listofstudents.pop(3)
print(listofstudents)

print("")

#removing the element we added with insert
listofstudents.remove("i am inserted at two")
print(listofstudents)

print("")

#ofc as before we can use del
#del listsofstudents[5]

# looping over the list
for i in range(len(listofstudents)):
    print(listofstudents[i], end=" ")

print("\n")

# if we want to print the list many times we can do so like this
print(listofstudents*2)

print("")

# sorting a list
listofnums = [1, 3, 6, 2, 4, 1, 2 ,4]
print(listofnums)
listofnums.sort()
print("")
print(listofnums)
print("")
print("")
# reverse sorting a list
listofnums = [1, 3, 6, 2, 4, 1, 2 ,4]
print(listofnums)
listofnums.sort()
listofnums.reverse()
print("")
print(listofnums)

#there are way more function related to lists but we didnt take them
#if you want to learn on your own you can go to this site for more answers
# https://www.w3schools.com/python/python_lists_methods.asp

