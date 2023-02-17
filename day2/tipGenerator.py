# fstring
# f"your score is {score}, your subject is {subject}"
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people =int(input("How many people split the bill? "))
total = bill + tip*bill/100
#pp = round(total/people, 2)
pp = "{:.2f}".format(total/people)
print(f"Each person should pay: ${pp} ")