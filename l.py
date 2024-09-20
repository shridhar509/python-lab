mark1 = int(input("Enter marks 1: "))
mark2 = int(input("Enter marks 2: "))
mark3 = int(input("Enter marks 3: "))

if mark1 > mark2 and mark1 > mark3:
    if mark2 > mark3:
        print(f"{mark1} and {mark2} are the biggest")
        print("The average of both is", (mark1 + mark2) / 2)
    else:
        print(f"{mark1} and {mark3} are the biggest")
        print("The average of both is", (mark1 + mark3) / 2)
elif mark2 > mark1 and mark2 > mark3:
    if mark1 > mark3:
        print(f"{mark2} and {mark1} are the biggest")
        print("The average of both is", (mark2 + mark1) / 2)
    else:
        print(f"{mark2} and {mark3} are the biggest")
        print("The average of both is", (mark2 + mark3) / 2)
else:
    if mark1 > mark2:
        print(f"{mark3} and {mark1} are the biggest")
        print("The average of both is", (mark3 + mark1) / 2)
    else:
        print(f"{mark3} and {mark2} are the biggest")
        print("The average of both is", (mark3 + mark2) / 2)
