while True:
    print("F(x) = a(x - h)^2 + k")
    try:
        a = float(input("input a : \n"))
        h = float(input("input h : \n"))
        k = float(input("input k : \n"))
        print("vertex is : (" + str(h) + ", " + str(k) + ")")
        print("line of symetry : x = " + str(h))
        sum = ""
        if 0<abs(a)<1:
            sum+="the parabula is wider than parent function"
        elif a == 0:
            sum+="the line is straight"
        else:
            sum+="the parabula is narrower than parent function"

        if 0<a:
            sum+=" and facing up"
        elif 0 > a:
            sum+=" and facing down"
        else:
            sum +=", "


        if h<0:
            sum += " shifted left by " + str(abs(h)) + " units"
        elif h>0:
            sum += " shifted right by " + str(abs(h)) + " units"
        else:
            sum += " not shifted horizontaly"

        if k<0:
            sum += " shifted down by " + str(abs(k)) + " units"
        elif k>0:
            sum += " shifted up by " + str(abs(k)) + " units"
        else:
            sum += " not shifted vertacly"

        print(sum)
        print("F(x) = ("+str(a)+")(x - ("+str(h)+"))^2 + ("+str(k)+")")
    except:
        print("write something useful")