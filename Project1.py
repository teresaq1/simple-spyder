# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 17:26:57 2020

@author: teresa
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


DemoDf = pd.read_csv("NhanesDemoAdapted.csv")
FoodDf = pd.read_csv("NhanesFoodAdapted.csv")


print(DemoDf)
DemoDf.describe
print(FoodDf)
FoodDf.describe

Menu=int(input("Please select one of the following options: 1. Household income per ethnicity, 2. Marital status, 3. Income and education level,4. Diet analysis, 5. Exit"))
if Menu==1:
    sortedEthnicity=DemoDf.sort_values(["Ethnicity"],ascending=["True"])
    print("The following ethnicities are represented")
    print(DemoDf["Ethnicity"].value_counts())
    print(sortedEthnicity)
    freqIncomeEth=DemoDf.sort_values(["HouseholdIncome","Ethnicity"]
                                     ,ascending=[True,False])
    print(freqIncomeEth)
    IE=sns.barplot(y="Ethnicity", x="HouseholdIncome",data=DemoDf,orient="h")
    IE.figure.set_size_inches(14,4)
    plt.show()
    
if Menu==2:
    freqMaritalStatus=DemoDf["Marital Status"].value_counts()
    freqMaritalAge=DemoDf[["Marital Status","Age"]][DemoDf["Age"]>20]
    print("The following is a list of marital status's")
    print(freqMaritalStatus)
    print("The following is a list of marital status's for adults"
          "over 20 years old")
    print(freqMaritalAge)
    AM1=sns.lineplot(data=DemoDf,x="Age",y="Marital Status")
    plt.show(AM1)
    AM2=sns.boxplot(data=DemoDf,y="Age",x="Marital Status",hue="Gender")
    AM2.figure.set_size_inches(14,4)
    plt.show(AM2)
    
    #insert line graph
if Menu==3:
    userchoice=(1)
    freqIncomeEdu=DemoDf.sort_values(["HouseholdIncome","IncomePovertyRatio"],
                                     ascending=[True,False])
    highIncomes=DemoDf.sort_values(["HouseholdIncome"]).head(10)
    print("The following is a list of 10 highest incomes")
    print(highIncomes)
    highPR=DemoDf.sort_values(["IncomePovertyRatio"]).head(10)
    print("The following is a list of 10 highest income Poverty Ratios")
    print(highPR)
    print(freqIncomeEdu)
    while userchoice==1 or userchoice==2:
        userchoice=int(input("Do you wish to examine correlation between"
                             "1.Education and Income Poverty ratio?,"
                             "or 2.Education and Household Income?"))
        if userchoice==1:
                EI=sns.barplot(y="Education", x="IncomePovertyRatio",
                               data=DemoDf,orient="h")
                EI.figure.set_size_inches(14,4)
                plt.show(EI)
        if userchoice==2:
                EH=sns.barplot(y="Education", x="HouseholdIncome",
                               data=DemoDf,orient="h")
                EH.figure.set_size_inches(14,4)
                plt.show(EH)
        else:
                print("invalid choice, please choose again")
       
if Menu==4:
    nutrientlist=(1)
    def Diet(DemoDf,FoodDf):
        
        #assuming this is what is meant by average food intake per meal per individual
        groupFoodDf=FoodDf.groupby("SEQN")
        print(groupFoodDf.count())
        #merging dataframes by seqn number
        left=pd.DemoDf({"SEQN"})
        right=pd.groupFoodDf({"SEQN"})
        print(left)
        print(right)
        QuainTeresa_merged= pd.merge(left,right, on="SEQN",how="inner")
        print(QuainTeresa_merged)
        studentName_merged.to_csv("QuainTeresa_merged.csv") #writing to file
    
studentName_merged = pd.read_csv("QuainTeresa_merged.csv")   
Diet(DemoDf,FoodDf)
print("The following nutrients are available")
print("1.dGRMS,\n2.dKCAL,\n3.dPROT,\n3.dPROT,\n4.dCARB,\n5.dSUGR,"
      "\n6.dFIBE,\n7.dTFAT,\n8.dSFAT,\n9.dCHOL,\n10.dVITC,"
      "\n11.dVITD,\n12.dCALC,\n13.dCAFF,\n14.dALCO")

nutrientlist=(int(input("Which category do you wish? (please enter num 1-14")))
#not asked to do anything with this choice

Merge1 = pd.read_csv("QuainTeresa_merged.csv") 

x=sns.boxplot(data=Merge1,y="Education",x="Ethnicity",hue="Gender")
x.figure.set_size_inches(14,8)
plt.show(x)

y=sns.scatterplot(data=Merge1, y="HouseholdIncome",x="Age")
y.figure.set_size_inches(14,8)
plt.show(y) 
     
if Menu==5:
    print("program exit. thanks and bye")    
    
else:
    print("invalid choice, please choose a number beteen 1 and 5")    
    
          

