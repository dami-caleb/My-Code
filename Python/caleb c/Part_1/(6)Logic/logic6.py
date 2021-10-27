#logical operator
#"and" = they both have to be true
subscribed = True
points= 40

print("Have you subscribed? True or False")
reply = input()

print("How many points do you have:")
points = int(input())

if (reply=="True" and points>=40):
    print("Welcome")
    subtracted_points = points-9
    print("You have " + str(subtracted_points) + " left.")
if (reply!="True"):
    print("Go and subscribe!")
if(points<40):
    print("Go and get more points!")