age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You've not been born yet")
elif age > 80:
    print("you re to old to signed up")
else:
    print("You msut be 18+ to signed up")
