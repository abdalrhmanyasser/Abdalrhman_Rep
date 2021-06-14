def findweight(formula : str):
    input("press enter to continue")
    s=open("C:\\Users\\abdal\Desktop\\Abdalrhman Yasser\\Visual Code\\Python\\periodic Table.txt").read()
    dictionary_of_elements = {}
    for i in s.splitlines():
        new_i = i.split("\t")
        dictionary_of_elements[new_i[2]] = {"Molecular Weight" : new_i[3], "Element Name" : new_i[1], "Atomic Symbol" : new_i[2]}
    WeightOfFormulaInGrams = 0
    additions = []
    for i in formula.split(" "):
        if i.isalpha():
            if i in dictionary_of_elements:
                print("Molecular Weight of " + dictionary_of_elements[i]["Element Name"] + "(" + dictionary_of_elements[i]["Atomic Symbol"] + ") is " + dictionary_of_elements[i]["Molecular Weight"])
                WeightOfFormulaInGrams += float(dictionary_of_elements[i]["Molecular Weight"])
                additions.append(float(dictionary_of_elements[i]["Molecular Weight"]))
            else :
                raise KeyError("the element you chose is not part of the data set")
        else:
            Element = ""
            num = ""
            for j in i:
                if j.isalpha():
                    Element+=j
                elif j.isnumeric():
                    num+=j
            if Element in dictionary_of_elements:
                print("Molecular Weight of " + dictionary_of_elements[Element]["Element Name"] + "(" + dictionary_of_elements[Element]["Atomic Symbol"] + ") is " + dictionary_of_elements[Element]["Molecular Weight"] + " times " + num + " = " + str(float(dictionary_of_elements[Element]["Molecular Weight"]) * float(num)))
                WeightOfFormulaInGrams+=float(dictionary_of_elements[Element]["Molecular Weight"]) * float(num)
                additions.append(float(dictionary_of_elements[Element]["Molecular Weight"]) * float(num))
            else :
                raise KeyError("the element you chose is not part of the data set")
    if len(additions) != 1:
        input("press enter to continue")
        for i in range(len(additions)):
            if i != len(additions) - 1:
                print(str(additions[i]) + " + ", end="")
            else:
                print(str(additions[i]) + " = ", end="")
        print(WeightOfFormulaInGrams)
def convertToEmpirical(formula : str):
    input("press enter to continue")
    nums = {}
    for i in formula.split(" "):
        if i.isalpha():
            print("the formula is already in emprical form")
            break
        else:
            Element = ""
            num = ""
            for j in i:
                if j.isalpha():
                    Element+=j
                elif j.isnumeric():
                    num+=j
            nums[Element] = num
    min_found = float("inf")
    for i in nums.keys():
        print(i, nums[i])
        if float(nums[i]) < float(min_found):
            min_found = float(nums[i])
    input("press enter to continue")
    print("all devide by " + str(min_found))
    final = ""
    for i in nums.keys():
        if float(nums[i])/min_found != 1:
            final+=i+str(int(float(nums[i])/min_found))
            print(nums[i] + " / " + str(min_found) + " = " + str(int(float(nums[i])/min_found)))
        else:
            final+=i
            print(nums[i] + " / " + str(min_found) + " = " + str(int(float(nums[i])/min_found)))
    input("press enter to continue")
    print(final)
        

if __name__ == "__main__":
    convertToEmpirical(input("Enter the formula to be translated into the empirical formula you want\nLike this : Na2 Cl4 O6 C14\nEnter your formula here : "))
    print("\n\n\n")
    findweight(input("Enter the formula for the weight you want\nLike this : Na3 As O16 H24\nEnter your formula here : "))