# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 08:55:24 2023

@author: bschick
"""
# create the main function
def main():
    #Plan 1 calls and returns
    print("Plan one")
    intRate=eval(input("Enter interest rate:"))
    year=eval(input("Enter year: "))
    (x,y)=plan1(intRate,year)
    print("The total cost Plan 1 is: ${0:,.2f}." .format(x))
    print("The Plan 1 plant desalinates: {0:,.0f} gallons of water." .format(y))
    # Plan 2 calls and returns
    print("Plan two")
    intRate=eval(input("Enter interest rate:"))
    year=eval(input("Enter year: "))
    (i,j)=plan2(intRate,year)
    print("The total cost Plan 2 is: ${0:,.2f}." .format(i))
    print("The Plan 2 plant desalinates: {0:,.0f} gallons of water." .format(j))
    #Plan 3 calls and returns
    print("Plan three")
    intRate=eval(input("Enter interest rate:"))
    year=eval(input("Enter year: "))
    (a,b)=plan3(intRate,year)
    print("The total cost Plan 3 is: ${0:,.2f}." .format(a))
    print("The Plan 3 plant desalinates: {0:,.0f} gallons of water." .format(b))
    return  
# Functions for plan 1 - takes interest rate and year as inputs
#initial cost = 59.1mil, operating cost= 5.31 mil and increases 10,000 annually
# desalinates 500 gallons of water per day

# defines the main function
def plan1(intRate,year):
    #Defines your givens
    cost=59100000 #initial cost
    operating = 5310000 #operating cost in year one
    opInc=10000 #increase in operating cost after year one
    desalYr=500*365*year #number of gallons delasinated per year
    
    #Code to find present values
    realCost= cost/((1+intRate)**-year)
    realOp=0
    for i in range (year):
        # dont think necessary- realInitial=cost/((1+intRate)**-i)  
        realOp+=(operating+(opInc*i))/((1+intRate)**-i)
    totalCost=realOp+realCost#Dont think necesssary-realInitial
    return(totalCost,desalYr)
                    
# Functions for plan 2, takes interest rate and year as inputs  
def plan2(intRate,year):
    #defines initial cost values
    initialCost=41000000 #implementation cost for first 10 years
    secondStage=25000000 #implementation cost after 10 years
    #defines operating cost values
    initialOp=3300000
    secondOp=5500000
    #operating cost at year = 0
    op1=0
    op2=op1
    for i in range(year):
        if i <11: #calculates the real cost for Plan 2 for first 10 years when the operating cost is $3.3 million per year
            real1st= initialCost/((1+intRate)**-i)
            op1+=(initialOp)/((1+intRate)**-i)
            desal1=300*i*365
        else: # calculates the real cost for Plan 2 after the 10th year when the operating cost is $5.5 million per year
            real2nd=real1st+(secondStage/((1+intRate)**-i))
            op2+=((secondOp)/((1+intRate)**-i))
            desal2=desal1+(450*i*365)
    totalCost=real2nd+op2+op1
    return(totalCost,desal2)
# Functions for plan 3, takes interest rate and year as inputs
def plan3(intRate,year):
    initialCost=34000000 #initial cost when purchasing the old plant and converting it 
    secondCost=20000000 #initial cost when adding an additional building after 5 years
    # defines operating cost values
    initialOp=3500000 #operating cost for first 5 years
    secondOp=6000000 #operating cost in the 6th year
    opInc=5000 #the increase in operating cost per year after the 6th year
    op1=0  #operating cost at year = 0
    op2=op1
    #calculate real cost
    for i in range(year):
        if i<6: #calculates the real cost for Plan 3 for first 5 years
            real1st=initialCost/((1+intRate)**-i)
            op1+=(initialOp)/((1+intRate)**-i)
            desal1=250*i*365
        else: #calculates the real cost for Plan 3 after the 5th year
            real2nd=real1st+(secondCost/((1+intRate)**-i))
            op2+=((secondOp+(opInc*i))/((1+intRate)**-i))
            desal2=desal1+(450*i*365)
    totalCost=real2nd+op1+op2
    return(totalCost,desal2)
main()

