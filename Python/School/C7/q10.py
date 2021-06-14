# Question 10: Write a program that rotates the elements of a list so that the element at the first index
# moves to the second index, the element in the second index moves to the third index, etc., and the
# element in the last index moves to the first index.
L = eval(input("give me your list : "))
new = []
for i in range(len(L)):
    new.append(L[i-1])
print(L, new)