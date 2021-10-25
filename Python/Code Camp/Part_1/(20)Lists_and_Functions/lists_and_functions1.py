#creating a function to take in numerous arguments

def greet_all(*people):   #The asterik infront of the parameter makes it possible for the function to recive numerous arguments
    for person in people:
        print("hELLO! ", person, ".")

greet_all("Mike","Bob","Jason")