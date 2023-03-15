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
df_input= pd.DataFrame({input_1 : [genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]})
print (df_input)
# input= [genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]
# print (input)

model = df['coef']

print (type(input[0]))
# lifespan_predicted = 8.333 +input[0]*1
lifespan_predicted = round(df['intercept'][0]+input[0]*model[0]+input[1]*model[1]+input[2]*model[2]+input[3]*model[3]+input[4]*model[4]+input[5]*model[5]+input[6]*model[6]+input[7]*model[7],1)
print(f'the predicted lifespan is: {lifespan_predicted}')