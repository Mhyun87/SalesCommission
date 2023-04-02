"""
calculate weekly pay for sales commision employees
"""
print("sales commission calculator")
print("")

# initialize totals to zero at the program
# initialize totalSales
totalSales = 0.0
# initialize totalWeeklyPay
totalWeeklyPay = 0.00

# prompt user for number of sales persons
# the input() function returns a string
# the int() function converts it to a whole number
nSalesPersons = int( input("Enter number of sales persons: ") )

# loop through all sales persons
# on each pass through the loop n will assume each successive value in the range
# for this case, n will start as 0 and end at nSalesPersons-1
# a total of nSalesPersons loop passes will be made, and then the loop will exit
# the : indicates the start of a block of code (the body of the loop)
# all statements in a block of code are indented
# the end of the indentation marks the end of the loop
for n in range(nSalesPersons):
  
    # prompt user for sales by this sales person
    # the input() function returns a string
    # the float() function converts it to a floating point number
    print("")
    sales = float( input("Enter sales in dollars for sales person %d: " % (n+1) ) )

    # calculate commission this sales person
    # the commission rate is 9%
    commission = 0.09 * sales

    # calculate weekly pay for this sales person
    # the weekly pay is the base pay of 200 plus the commission
    pay = 200 + commission

    # display weekly pay with 2 decimal digits
    print ("Weekly pay is $%.2f" % pay)

    # accumulate totals
    # update totalSales
    totalSales = totalSales + sales
    # update totalWeeklyPay
    totalWeeklyPay = totalWeeklyPay + pay 

# display totals with 2 decimal digits
print("")
# display totalSales
print("Total weekly sales: $%.2f" % totalSales)
# display totalWeeklyPay
print("Total weekly pay:   $%.2f" % totalWeeklyPay)

# hold window open to allow user to view output
print("")
input("Press ENTER to continue ")
