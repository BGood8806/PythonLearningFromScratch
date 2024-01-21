#Write your welcome message for the tip calculator
print("Welcome to the tip calculator!\n")

#Write the input for the total bill
total_bill = float(input ("What was the total bill? $\n"))

#Write the input for the tip percentage
tip_percentage = float(input ("What percent tip are you leaving? 10, 12, or 15?\n"))

#Write the input for how many people split the bill
split_bill = float(input ("How many people split the bill?\n"))

#Formula for finding out how much each person should pay
tip_as_percent = tip_percentage / 100
total_tip_amount = total_bill * tip_as_percent
bill = total_bill + total_tip_amount
individual_bill = bill / split_bill
round(individual_bill,2)

#How to format the answer to have two decimal places
final_amount = "{:.2f}".format(individual_bill)


#Print the input for how much each person should pay?
print(f"Each person should pay: ${final_amount}")







            

                