with open('C:\\Users\\abdal\\Downloads\\win10\\a.out', 'rb') as fp:
    counter = 0
    gen = (b for b in fp.read())
    while counter < 3:
        print(next(gen), end=", ")
        if int(next(gen)) == 00:
            counter+=1
        else:
            counter = 0