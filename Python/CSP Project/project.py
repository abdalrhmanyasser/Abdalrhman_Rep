import time
# Recipe handbook

print("Welcome to your Recipe Book!\n")

Recipes = {}

def filterRecipes(IncludeList):
    filteredRecipes = {}

    # loop through the recipes to check each one
    for keyOfRecipe in list(Recipes.keys()):
        #loop through each filter
        for item in IncludeList:
            # check if the recipe includes the item and add it to the removed list
            if item in Recipes.get(keyOfRecipe):
                filteredRecipes[keyOfRecipe] = Recipes.get(keyOfRecipe)
    return filteredRecipes

def createRecipe():
    # make a list to contain the ingrediants
    newRecipe = []
    # set a counter for the print statment to display a number before each ingrediant, and a flag variable
    numofItems = 1
    print("Enter an Item or enter \"finish\" to finish\n")
    while True:
        inputItem = input(str(numofItems)+": ")
        
        # if it is "cancel", then cancel the operation and return "canceled"
        if inputItem.lower() == "cancel":
            print("The Recipe changes have been canceled")
            return []
        
        if inputItem.lower() == "finish":
            # if it is "finish" check the current number of ingrediants and turn on the flag variable
            if numofItems != 1:
                break
            else:
                # if the number of ingrediants is not valid and its finish redo the loop and inform the user
                print("you must enter at least 1 ingredient")
                continue
                
        # add new ingrediants
        newRecipe.append(inputItem)
        numofItems+=1
         
    # once it is finished return the recipe
    return newRecipe

def printRecipes(filters = [], onlyKeys = False) -> None:
    currentRecipes = {}
    # apply a check if there are no recipes to display, if there isn't exit the function and return nothing
    if Recipes == {}:
        print("\n\n\n\nThere are no recipes to display.")
        return
    # if there are recipes we wont exit and we will see if filters are applied
    print("Recipes : ")
    # check that filter are properly formated and that they exist
    if filters != []:
        # call the filterRecipes function and store the result in excludedRecipes variable
        currentRecipes = filterRecipes(filters)
    else:
        # if there are no filters display the original Recipes dictionary as it is
        currentRecipes = Recipes
        
    if currentRecipes == {}:
        print("There are no recipes that match your filter")
    else:
        # logic for displaying the dictionary and arrays in a neat way
        for i in range(len(currentRecipes)):
            print(str(i+1)+". "+ list(currentRecipes.keys())[i])
            if not onlyKeys :
                for j in currentRecipes[list(currentRecipes.keys())[i]]:
                    print("\t" + str(j))

# main loop of the program where input is taken and calls to other functions are made
while True:
    print("\n\nMain Menu")
    choice = input("please choose from the following options:\n\t1. Add a new recipe\n\t2. Delete a recipe\n\t3. Edit a recipe\n\t4. View recipes\n\t5. Exit\n\nYour Choice : ")
    # check each choice entered and do what each one needs
    if choice.isnumeric() and 0 < int(choice) <= 5:
        match choice:
            case "1":
                # intilize a flag variables
                newName = False
                # loop until a unique name is chosen
                while not newName:
                    nameOfRecipe = input("Enter the name of the recipe: ")
                    if nameOfRecipe not in list(Recipes.keys()):
                        newName = True
                newRecipe = createRecipe()
                # if its empty then do nothing
                if newRecipe != []:
                    # load the data into the list
                    Recipes[nameOfRecipe] = newRecipe
                
            # delete choice
            case "2":
                # check if there is something to delete
                if len(Recipes) == 0:
                    # if there are no recipes display the information to the user
                    print("\nthere are no recipes to be deleted\n")
                    continue
                # flag variable
                print("To delete a recipe please chose the number that it corrisponds to, here are the following options:")
                # display the available options
                printRecipes([], True)
                # loop until a choice is chosen or its canceled
                while True:
                    choice = input("Enter the number you would like to delete (if you want to cancel type \"cancel\"): ")
                    # check if the choice is logical
                    if choice.isnumeric() and 1 <= int(choice) <= len(Recipes):
                        Recipes.pop(list(Recipes.keys())[int(choice)-1])
                        break
                    
                    # if the choice is to cancel break out of the match case statement
                    if choice.lower() == "cancel":
                        break
                    # if the choice doesnt match any of the above statements the print invalid
                    print("you have entered an invalid answer please enter a number that is between 1 and " + str(len(Recipes)))
            # Edit Choice
            case "3":
                # check if there is something to edit
                if len(Recipes) == 0:
                    print("\nthere are no recipes to be edit\n")
                    continue
                print("To edit a recipe please chose the number that it corrisponds to, here are the following options:")
                # display the available options
                printRecipes([], True)
                # loop until finish the edit or canceled
                while True:
                    choice = input("Enter the number you would like to edit (if you want to cancel type \"cancel\"): ")
                    # check if the choice is logical
                    if choice.isnumeric() and 1 <= int(choice) <= len(Recipes):
                        newRecipe = createRecipe()
                        # check if the user canceled the recipe process otherwise make the changes
                        if newRecipe != []:
                            Recipes[list(Recipes.keys())[int(choice)-1]] = newRecipe
                        break
                    # if the choice is to cancel break out of the match case statement
                    if choice.lower() == "cancel":
                        break
                    # displaying the invalid message if the input is illogical
                    print("you have entered an invalid answer please enter a number that is between 1 and " + str(len(Recipes)))
                        
            # View Recipes Choice
            case "4":
                # take the filter if there are any
                inputfilters  = input("""Filters (ingrediants you want to be included) if you dont want to include any filter just press enter\nExample:\nMeat, Flour, Egg\n\nEnter here : """)
                # check the filters and pass them to the printRecipes function
                if inputfilters != "":
                    filters = inputfilters.split(", ")
                    printRecipes(filters)
                # if there are filter then print all available recipes
                else:
                    printRecipes()
            case "5":
                exit()
    else:
        print("please input a valid number between 1 and 5")


