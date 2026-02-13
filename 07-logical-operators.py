temp = 4
is_raining = False
is_sunny = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

if temp >= 28 and is_sunny:
    print("It is HOT outside ")
elif temp <= 5 and not is_sunny:
    print("Its too cold outside")
else:
    print("Lets go out")
