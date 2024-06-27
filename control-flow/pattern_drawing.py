pattern = int(input("Enter the size of the pattern:"))
x=0
while x < pattern:
    for i in range(1,pattern ):
        print("*" * pattern , end="")
        x+=1
        print()

