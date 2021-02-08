while True:
    print("F(x) = ax^2 + bx + c")
    try:
        a = float(input("input a : \n"))
        b = float(input("input b : \n"))
        c = float(input("input c : \n"))
        x=-b/(2*a)
        print("line of symetry : x = " + str(x))
        print("vertex is : (" + str(x) + ", " + str((a*x)+(b*x)+c) + ")")
        sum = ""
        if 0<abs(a)<1:
            sum+="the parabula is wider than parent function"
        elif a == 0:
            sum+="the line is straight"
        elif a == 1:
            sum+="the parabula is normal"
        else:
            sum+="the parabula is narrower than parent function"

        if 0<a:
            sum+=" and facing up"
        elif 0 > a:
            sum+=" and facing down"
        else:
            sum +=", "


        if c<0:
            sum += " shifted left by " + str(abs(c)) + " units"
        elif c>0:
            sum += " shifted right by " + str(abs(c)) + " units"
        else:
            sum += " not shifted horizontaly"

        if b<0:
            sum += " shifted down by " + str(abs(b)) + " units"
        elif b>0:
            sum += " shifted up by " + str(abs(b)) + " units"
        else:
            sum += " not shifted vertacly"

        print(sum)
        print("F(x) = ("+str(a)+")(x - ("+str(c)+"))^2 + ("+str(b)+")")
    except:
        print("write something useful")