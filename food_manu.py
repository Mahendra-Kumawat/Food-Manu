
 # food manu project
welcome = "  hello welcome! to Taj Hotel"
print(welcome.center(100, "@"))
print("JAIPUR".center(100," "))
print("Please! order")
print("1 = breckfast")
print("2 = lunch")
print("3 = Dinner")
print("Please! Enter the choice")
# here code start for breckfast
meal = input()
if meal == "1":
    print("breckfast main kya lena chahenge")
    print("1 = puha")
    print("2 = badam kheer")
    print("3 = shandwich")
    meal1 = input("please! choose your choice")
    if meal1 == "1":
            print("     half plate prize = 20 rupees")
            print("     full plate plate prize = 35 rupees")
            print("please! choose your choice half plate or full plate")
            print("1 = half plate")
            print("2 = full plate")
            prize = input()
            if prize == "1":
                print("How many plate need you")
                plate = int(input())
                if plate == "1" or "2" or "3" or "4" or "5":
                    print("ok")
                    print("your total amount is", 20*plate,"Rupees")
            elif prize == "2":
                print("How many plate need you")
                plate = int(input())
                if plate == "1" or "2" or "3" or "4" or "5":
                    print("ok")
                    print("the total amount is", 35*plate, "Rupees")
       
    elif meal1 == "2":
            print("     half plate prize = 40 rupees")
            print("     full plate plate prize = 70 rupees")
            print("please! choose your choice half plate or full plate")
            print("1 = half plate")
            print("2 = full plate")
            prize = input()
            if prize == "1":
                print("How many plate need you")
                plate = int(input())
                if plate == "1" or "2" or "3" or "4" or "5":
                    print("ok")
                    print("your total amount is", 40*plate,"Rupees")
            elif prize == "2":
                print("How many plate need you")
                plate = int(input())
                if plate == "1" or "2" or "3" or "4" or "5":
                    print("ok")
                    print("the total amount is", 70*plate, "Rupees")
    elif meal1 == "3":
        print("     half plate prize = 25 rupees")
        print("     full plate plate prize = 45 rupees")
        print("please! choose your choice half plate and full plate")
        print("1 = half plate")
        print("2 = full plate")
        prize = input()
        if prize == "1":
            print("How many plate need you")
            plate = int(input())
            if plate == "1" or "2" or "3" or "4" or "5":
                print('ok')
                print("your total amount is",25*plate,"rupees")
        elif prize  == "2":
            print("How many plate need you")
            plate = int(input())
            if plate == "1" or "2" or "3" or "4" or "5":
                print('ok')
                print("your total amount is",45*plate,"rupees")

#here code start for lunch 

elif meal == "2": 
    print("lunch main kya lena chahenge")
    print("1 = paneer + 2 Roti")
    print("2 = aalu ki sabji + 2 tanduri roti")
    print("3 = gahar ka halwa + 1 glass milk ")
    meal1 = input("please! choose your choice")       
    if meal1 == "1":
            print("     paneer + 2 Roti for half plate prize = 70 rupees")
            print("     paneer + 2 Roti for full plate plate prize = 120 rupees")
            print("please! choose your choice half plate or full plate")
            print("1 = half plate")
            print("2 = full plate")
            prize = input()
            if prize == "1":
                print("How many plate need you")
                plate = int(input())
                if plate == "1" or "2" or "3" or "4" or "5":
                    print("ok")
                    print("your total amount is", 70*plate,"Rupees")
            elif prize == "2":
                print("How many plate need you")
                plate = int(input())
                if plate == "1" or "2" or "3":
                    print("ok")
                    print("the total amount is", 120*plate, "Rupees")
       
    elif meal1 == "2":
            print("     aalu ki sabji + 2 tanduri roti for half plate prize = 60 rupees")
            print("     aalu ki sabji + 2 tanduri roti for full plate plate prize = 100 rupees")
            print("please! choose your choice half plate or full plate")
            print("1 = half plate")
            print("2 = full plate")
            prize = input()
            if prize == "1":
                print("How many plate need you")
                plate = int(input())
                if plate == "1" or "2" or "3" or "4" or "5":
                    print("ok")
                    print("your total amount is", 60*plate,"Rupees")
            elif prize == "2":
                print("How many plate need you")
                plate = int(input())
                if plate == "1" or "2" or "3" or "4" or "5":
                    print("ok")
                    print("the total amount is", 100*plate, "Rupees")
    elif meal1 == "3":
        print("     gahar ka halwa + 1 glass milk for half plate prize = 90 rupees")
        print("     gahar ka halwa + 1 glass milk for full plate plate prize = 160 rupees")
        print("please! choose your choice half plate and full plate")
        print("1 = half plate")
        print("2 = full plate")
        prize = input()
        if prize == "1":
            print("How many plate need you")
            plate = int(input())
            if plate == "1" or "2" or "3" or "4" or "5":
                print('ok')
                print("your total amount is",90*plate,"rupees")
        elif prize  == "2":
            print("How many plate need you")
            plate = int(input())
            if plate == "1" or "2" or "3" or "4" or "5":
                print('ok')
                print("your total amount is", 160*plate,"rupees")

# here code start for dinner 

elif meal == "3": 
    print("dinner main kya lena chahenge")
    print("1 = aalo + chole mix + 4 roti")
    print("2 = gahar ki sabji  + 4 tanduri roti")
    print("3 = halwa + bhugiya  + 1 glass milk for night ")
    meal1 = input("please! choose your choice")       
    if meal1 == "1":
            print("     aalo + chole mix + 4 roti for  half plate prize = 80 rupees")
            print("     aalo + chole mix + 4 roti for full plate plate prize = 140 rupees")
            print("please! choose your choice half plate or full plate")
            print("1 = half plate")
            print("2 = full plate")
            prize = input()
            if prize == "1":
                print("How many plate need you")
                plate = int(input())
                if plate == "1" or "2" or "3" or "4" or "5":
                    print("ok")
                    print("your total amount is", 80*plate,"Rupees")
            elif prize == "2":
                print("How many plate need you")
                plate = int(input())
                if plate == "2" or "2" or "3" or "4" or "5":
                    print("ok")
                    print("the total amount is", 140*plate, "Rupees")
       
    elif meal1 == "2":
            print("     gahar ki sabji  + 4 tanduri roti for half plate prize = 120 rupees")
            print("     gahar ki sabji  + 4 tanduri roti for full plate plate prize = 210 rupees")
            print("please! choose your choice half plate or full plate")
            print("1 = half plate")
            print("2 = full plate")
            prize = input()
            if prize == "1":
                print("How many plate need you")
                plate = int(input())
                if plate == "1" or "2" or "3" or "4" or "5":
                    print("ok")
                    print("your total amount is", 120*plate,"Rupees")
            elif prize == "2":
                print("How many plate need you")
                plate = int(input())
                if plate == "1" or "2" or "3" or "4" or "5":
                    print("ok")
                    print("the total amount is", 210*plate, "Rupees")
    elif meal1 == "3":
        print("     halwa bhugiya for half plate prize = 160 rupees" + "1 glass milk in night at 8:00pm")
        print("     halwa bhujiya  for full plate plate prize = 300 rupees" + "1 glass milk in night at 8:00pm ")
        print("please! choose your choice half plate and full plate")
        print("1 = half plate")
        print("2 = full plate")
        prize = input()
        if prize == "1":
            print("How many plate need you")
            plate = int(input())
            if plate == "1" or "2" or "3" or "4" or "5":
                print('ok')
                print("your total amount is",160*plate,"rupees")
        elif prize  == "2":
            print("How many plate need you")
            plate = int(input())
            if plate == "1" or "2" or "3" or "4" or "5":
                print('ok')
                print("your total amount is", 300*plate,"rupees")
else:
    print("please! Enter the right option ")   