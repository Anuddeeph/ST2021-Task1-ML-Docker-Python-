import pandas 
import numpy as np
dataset = pandas.read_csv('Salary_Data.csv')

X = dataset[['YearsExperience']]
y = dataset['Salary']

X=X.values.reshape(-1,1)
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X,y)

Experience=float(input("Please Enter the Years of Experience: "))
Pred_Salary=model.predict([[Experience]])
print("You can expect a salary around {} ".format(Pred_Salary) )
