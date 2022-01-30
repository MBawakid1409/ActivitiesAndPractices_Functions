# Activities & Practices

# 01 "Tenth Power"
# Let’s create some functions which can help us solve math problems! For this first function, we are going to take the tenth power of a number. In order to do this we need to do three things:

# 1. Set up the function header for [tenth_power] which accepts one parameter
# 2. Take the tenth power of the input value
# 3. Return the result

# Write a function named [tenth_power()] that has one parameter named [num].
# The function should return [num] raised to the 10th power.

print("'Tenth Power' challenge")
def tenth_power(num):
  return num ** 10

# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah

# 02 "Square Root"
# Another useful function for solving math problems is the square root function. We can create this using similar steps from the last problem. The code will look very similar. We need to:

# 1. Set up the function header for [square_root] which accepts one parameter
# 2. Take the square root of the input value
# 3. Return the result

# Write a function named [square_root()] that has one parameter named num.
# Use exponents ([**]) to return the square root of [num].

print("'Square Root' challenge")
def square_root(num):
  return num ** 0.5

# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah

# 03 "Win Percentage"
# Next, we will create a function which calculates the percentage of games won. In order to do this, we will need to know how many total games there were and divide the number of wins by the total number of games. For this function, there will be two input parameters, the number of wins and the number of losses. We also need to make sure that we return the result as a percentage (in the range of 0 to 100). In order to create this method we need the following steps:

# 1. Define the function header with two parameters, wins and losses
# 2. Calculate the total number of games using the number of wins and losses
# 3. Get the ratio of winning using the number of wins out of the total number of games.
# 4. Convert the ratio to a percentage
# 5. Return the percentage

# Create a function called [win_percentage()] that takes two parameters named [wins] and [losses].
# This function should return out the total percentage of games won by a team based on these two numbers.

print("'Win Percentage' challenge")
def win_percentage(wins, losses):
  total_percentage = int(wins / (wins+losses) * 100) #+ "%"
  return total_percentage

print(win_percentage(5, 5))  

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah

# 04 "Average"
# Let’s create a function which takes the average of two numbers. These two numbers will be the input of the function and the output will be the average of the two. In order to do this, we need to do a few steps:

# 1. Define the function with two input parameters, [num1] and [num2]
# 2. Calculate the sum of the two numbers
# 3. Divide the sum by the number of inputs to the function
# 4. Return the answer

# Write a function named [average()] that has two parameters named [num1] and [num2].
# The function should return the average of these two numbers.

print("'Average' challenge")
def average(num1, num2):
  average_result = (num1 + num2) / 2
  return average_result

# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah

# 05 "Remainder"
# For the final challenge in this group, we are going to take the remainder of two numbers while performing other mathematical operations on them. We are going to multiply the numerator by 2 and divide the denominator by 2. After the two values have been modified, we will divide them and return the remainder. In order to do this we will need to:

# 1. Define the function to accept two parameters
# 2. Multiply the first input value by 2
# 3. Divide the second input value by 2
# 4. Calculate the remainder of the modified first input value divided by the modified second input value (using modulus)
# 5. Return the answer

# Write a function named [remainder()] that has two parameters named [num1] and [num2].
# The function should return the remainder of twice [num1] divided by half of [num2].

print("'Remainder' challenge")
def remainder(num1, num2):
  remainder_result = (num1 * 2) % (num2 / 2)
  return remainder_result
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah

