change = eval(input("Enter the change"))
print("quarters :", change//.25)
change-=(change//.25)*.25
print("dimes :", change//.10)
change-=(change//.10)*.10
print("nickels :",change//.05)
change-=(change//.05)*.05
print("pennies :",1+(change//.01))
change-=(change//.01)*.01