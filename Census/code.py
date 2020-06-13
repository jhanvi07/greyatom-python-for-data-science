# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))

#Code starts here
census= np.concatenate((new_record,data))
print("census: \n\n", census)
print(data.shape)
print(census.shape)

#We often associate the potential of a country based on the age distribution of the people residing there. We too want to do a simple analysis of the age distribution.

age= (census[:,0])
max_age= max(age)
min_age= min(age)
age_mean= np.mean(age)
age_std= np.std(age)
print(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)

#The constitution of the country tries it's best to ensure that people of all races are able to live harmoniously. Let's check the country's race distribution to identify the minorities so that the government can help them.

race_0= census[census[:,2]==0]
race_1= census[census[:,2]==1]
race_2= census[census[:,2]==2]
race_3= census[census[:,2]==3]
race_4= census[census[:,2]==4]
len_0= len(race_0)
len_1= len(race_1)
len_2= len(race_2)
len_3= len(race_3)
len_4= len(race_4)

race_list=[len_0,len_1,len_2,len_3,len_4]

minority_race=race_list.index(min(race_list))
print(minority_race)

#As per the new govt. policy, all citizens above age 60 should not be made to work more than 25 hours per week. Let us look at the data and see if that policy is followed.

senior_citizens= census[census[:,0]>60]
working_hours_sum= senior_citizens.sum(axis=0)[6]
print(working_hours_sum)

senior_citizens_len= len(senior_citizens)
print(senior_citizens_len)
avg_working_hours= working_hours_sum/senior_citizens_len
print(avg_working_hours)

#Our parents have repeatedly told us that we need to study well in order to get a good(read: higher-paying) job. Let's see whether the higher educated people have better pay in general.

high= census[census[:,1]>10]
low= census[census[:,1]<=10]
print(high)
print(low)

avg_pay_high= high[:,7].mean()
avg_pay_low= low[:,7].mean()

print(avg_pay_high)
print(avg_pay_low)



