# --------------
import pandas as pd 
import numpy as np
#step1:Let's check which variable is categorical and which one is numerical so that you will get a basic idea about the features of the bank dataset. The path for the dataset has been stored in a variable path.

#create a dataframe bank
bank= pd.read_csv(path, sep=',')
#To check all categories
categorical_var= bank.select_dtypes(include='object')
#print(categorical_var)
print(categorical_var.head(5))
#To check all numerical values in categories
numerical_var= bank.select_dtypes(include='number')
#print(numerical_var)
print(numerical_var.head(5))

#print(categorical_var.shape)
#print(numerical_var.shape)

#step 2: Sometimes customers forget to fill in all the details or they don't want to share other details. Because of that, some of the fields in the dataset will have missing values. Now you have to check which columns have missing values and also check the count of missing values each column has. If you get the columns that have missing values, try to fill them.

#dropping the column and store it in new dataframe
banks= bank.drop(columns='Loan_ID')
#check null values
print(banks.isnull().sum())
#calculate mode to see the missing values
bank_mode= banks.mode().iloc[0]
#fill missing values
banks.fillna(bank_mode,inplace=True)
#check missing values filled
print(banks.isnull().sum())
print(banks.shape)
#step 3: Now let's check the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'. This will give a basic idea of the average loan amount of a person.

#finding average loan amount usin pivot table
avg_loan_amount= banks.pivot_table(values=['LoanAmount'],index=['Gender','Married','Self_Employed'],aggfunc=np.mean)
print(avg_loan_amount)

#Step 4: Now let's check the percentage of loan approved based on a person's employment type.
#loan approved for self employed
loan_approved_se= banks.loc[(banks["Self_Employed"]=="Yes") & (banks["Loan_Status"]=="Y"),["Loan_Status"]].count()
print(loan_approved_se)
#loan approved for non self employed
loan_approved_nse= banks.loc[(banks["Self_Employed"]=="No") & (banks["Loan_Status"]=="Y"),["Loan_Status"]].count()
print(loan_approved_nse)
#percentage
percentage_se=(loan_approved_se*100/614)
percentage_nse=(loan_approved_nse*100/614)

print(percentage_se)
print(percentage_nse)

#step 5: A government audit is happening real soon! So the company wants to find out those applicants with long loan amount term.

#loan amount term
#apply function
loan_term= banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)
#Find the number of applicants having loan amount term greater than or equal to 25 years and store them in a variable called 'big_loan_term'.
#number of applicants having loan amount term greater than or equal to 25 years
big_loan_term= len(loan_term[loan_term>=25])
print(big_loan_term)

#step 6: Now let's check the average income of an applicant and the average loan given to a person based on their income.
#groupby function
loan_groupby= banks.groupby(['Loan_Status'])

#Subset 'loan_groupby' to include only ['ApplicantIncome', 'Credit_History']
columns_to_show= ['ApplicantIncome','Credit_History']
loan_groupby= loan_groupby[columns_to_show]

#check the mean value
mean_values=loan_groupby.agg([np.mean])
print(mean_values)









