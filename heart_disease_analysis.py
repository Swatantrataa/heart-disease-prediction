
import pandas as pd
import matplotlib.pyplot as pl
df1=pd.read_csv("C:\\Users\\swata\\Desktop\\heart_disease_prediction.csv")

pd.set_option("display.max_rows",100)
pd.set_option("display.max_columns",14)
print(df1)
print(" ")
 
print("ABOUT DF1")
print(15*"=")
print(df1.info())
print(df1.describe())

#0-female
#1-male
print(" ")
print("Sex of the patients in our dataset")
print(30*"=")

print(df1['Sex'].value_counts())
print("WHERE 0=FEMALE and 1= MALE")
print(" ")

print("Health Details of patients who suffer from HEART DISEASE")
print(df1.loc[df1["Heart Disease"]=="Presence"])
print(" ")


print(" ><><><><><><><><><><><><><GRAPH AND CHARTS><><><><><><><><><><><><><><><><>")
print("===================================================================================")

#Graph Showing the gender composition of patients 
pl.title("Graph Showing the gender composition of patients")
label='Male','Female'
sizes=[183,87]
pl.pie(sizes,labels=label,shadow=True,autopct="%1.1f%%",startangle=180)
pl.show()


pl.title("Avg of cholesterol by age")
pl.bar(df1['Age'],df1['Cholesterol'],color="magenta")
pl.xlabel("Age")
pl.ylabel("Cholesterol")
pl.show()

pl.title(" Average of Cholesterol by Sex")
pl.bar(df1['Sex'],df1["Cholesterol"],color="orange")
pl.xlabel("Male                              Female")
pl.ylabel("cholesterol")
pl.show()

#Creating different dataframe for male and female
dfmale=df1[df1["Sex"]==1]

dffemale=df1[df1["Sex"]==0]

pl.title("Relation  between BP, Age and Sex ")
pl.bar(dfmale["Age"],dfmale["BP"],color="blue",label="Male")
pl.bar(dffemale["Age"],dffemale["BP"],color="orange",label="Female")
pl.xlabel("AGE")
pl.ylabel("Blood Pressure")
pl.legend()
pl.show()

