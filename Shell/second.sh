computer_solution = 2
echo  "Welcome to the math examiner.\n What is your name?"  #the "-e" makes it possible for us to use the new line charcter
read user_name
read -p "By solving the equation a = 20 - 9a, the value of a will be: " user_solution
#computer_solution = 2
if [$user_soution == $computer_solution]
	echo'Nice Job!'
else
	echo"That is wrong."
fi
 
