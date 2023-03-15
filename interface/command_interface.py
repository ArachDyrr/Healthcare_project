"""Interface for health_app"""
# imports
# import pickle
# import logging
import sqlite3
import pandas as pd

# with open("reg.pkl", "rb") as f:
#     reg = pickle.load(f)

# open connection to SQLite.db
dbName = "rest_server/medisch_centrum_randstad/db.sqlite3"


dbConnection = sqlite3.connect(dbName)

# query db and write to pd:
dfFromDB = pd.read_sql_query(f"SELECT * FROM {'coef'}", dbConnection)
# sql adds index, remove:
df = dfFromDB.drop('index', axis=1)
pd.set_option('display.max_columns', 10)
print(df.head(12))





# genetic = float(input('Vul de genetische leeftijd in: '))
# length = float(input('Vul de lengte in centimeters in: ')) 
# mass = float(input ("Vul het lichaamsgewicht in hele kilo's in: "))
# alcohol = float(input("Vul het aantal glazen alcohol per dag in: "))
# sugar = float(input("Vul het aantal suikerklontjes per dag in: "))
# smoking = float(input("Vul het aantal sigaretten per dag in: "))
# exercise = float(input("Vul het aantal uren beweging per dag in: "))
# divider = pow(length/100, 2) if length >0 else None
# bmi = round(mass/divider)
# # logging.debug(f'bmi: {bmi}')


genetic = int(77)
length = int(177) 
mass = int(77)
alcohol = int(2)
sugar = int(2)
smoking = int(2)
exercise = int(2)
divider = pow(length/100, 2) if length >0 else None
bmi = round(mass/divider)

# lifespan_predict = reg.predict([[genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]])
# print(lifespan_predict)
# df = pd.DataFrame(data=[pi, e, phi])
# df_input= pd.DataFrame(data=['genetic', 'length', 'mass', 'alcohol', 'sugar', 'smoking', 'exercise', 'bmi'], [genetic, length, mass, alcohol, sugar, smoking, exercise, bmi])
# print (df_input.head)
# input= [genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]
# print (input)
# Python code demonstrate creating
# DataFrame from dict narray / lists
# By default addresses.
  

  
# initialize data of lists.
data = {'feature': ['genetic', 'length', 'mass', 'alcohol', 'sugar', 'smoking', 'exercise', 'bmi'],
        'input_1': [genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]}
  
# Create DataFrame
df_input = pd.DataFrame(data)
  
# Print the output.
print(df_input)


# multiply the rows of df and df_input for the relevant row. add the interceptor where the data crosses the y-axis. 
lifespan_predicted = sum(df_input['input_1'].multiply(df['coef'])),1)+ round(df['intercept'][0] + 

print(f'the predicted lifespan is: {lifespan_predicted}')

