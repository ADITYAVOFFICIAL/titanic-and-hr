'''
Importing libraries for reading csv file, 
Importing numpy for caluclations like min, max, variance
Importing seaborn library for boxplot
Importing matplot libraray to show the graph plot
'''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib. pyplot as plt

#Importing the CSV file given in the pdf
importcsvfile = pd.read_csv('/Users/aditya/Downloads/Employee_HR.csv')


#Filtering the data for hr and marketing dept
hrsal = importcsvfile[importcsvfile['Department'] == 'hr']['Salary_INR']
marksal = importcsvfile[importcsvfile['Department'] == 'marketing']['Salary_INR']

#Calculating variance, standard deviation, and IQR
hrvar = np.var(hrsal)
hrstdev = np.std(hrsal)
hriqr = np.percentile(hrsal, 75) - np.percentile(hrsal, 25)
markvar = np.var(marksal)
markstdev = np.std(marksal)
markiqr = np.percentile(marksal, 75) - np.percentile(marksal, 25)

#Finding the range of experience (max experience - min experience)
texp = importcsvfile["time_spent_company"][importcsvfile["Department"] == "IT"]
minexp = texp.min()
mexp = texp.max()
exp=mexp-minexp

#Using seaborn to make a boxplot with x axis showing all the dept and y showing the exp
sns.boxplot(x="Department",y="time_spent_company",data=importcsvfile)

# Identify the column with the highest standard deviation
numsdevcol = importcsvfile.select_dtypes(include=[np.number]).std()
hstdcol = numsdevcol.idxmax()
hstdval = numsdevcol.max()

#Printing all the results
print("\n\nHR Department : 🔻")
print(f"Variance : {hrvar}", hrvar)
print(f"Standard Deviation : {hrvar}")
print(f"IQR : {hriqr}\n")
print("Marketing Department 🔻 ")
print(f"Variance : {markvar}")
print(f"Standard Deviation : {markstdev}")
print(f"IQR : {markiqr}")

#Printing the boxplot and changing the x and y labels
plt.title("Range of Experience")
plt.ylabel("Experience in Years")
plt.xlabel("Departments")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Printing the range of exp in IT dept
print()
print(f"📈 The range of experience in IT department is: {exp}\n")

#Printing the highest std dev column and value
print(f"⚡️ The column with the highest standard deviation is {hstdcol} with a value of {hstdval:.2f}")

print("\n* THE END *\n")