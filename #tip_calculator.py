# Tip_calulator
# 1) In the line below I will add variables that will prompt user inputs.
# 2) Everything is a float because dividing ints. may lead to decimal places so floats work best for both.
num_people = float(input("Welcome, how many people ate with you?:  "))
cost_of_meals = float(input("How much did it all cost?:  "))
# 3) The line below is showing those who use the app, what each person would owe splitting the bill evenly.
if num_people >= 1:
        print(f"The cost person should be {cost_of_meals / num_people} person before tip and taxes.")
        
# Thus creating another variable that has the values of the cost before taxes and tip bellow will hold the same value stated above.

sum_per_person = cost_of_meals / num_people
# We will also set that variable so that it will not exceed 2 decimal places over making calculations easier.
round(sum_per_person, 2)

# New variable showing 'taxes' will show what tax would be for each person splitting the bill.
# Where total will equal each persons true total 


tax = sum_per_person * 0.1
total = tax + sum_per_person
# Rounding the total to 2 decimal places to ensure easier calculations when it comes to tips.
round(total, 2)
print(f"After taxes the total is {total}$ per person.")

# The line below will run how much each person is willing to tip depending on how many people are inputed.
# The 'total_cost_each' variable carries what each person will want to tip and add it to how much the bill costs each of the individuals that were inputed.
for tip in range(int(num_people)) :
       tip = input("How much would you each like to tip? (Please insert a decimal equivalent of percentage.): ")
       total_cost_each = (total * float(tip)) + total
       print(f"{round(total_cost_each, 2)}$ is how much you owe!")


        
