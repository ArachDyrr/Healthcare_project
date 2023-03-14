#!/usr/bin/env python

# Imports
import logging
import pandas as pd
# import requests
import sqlite3
from sklearn import linear_model
from sklearn.model_selection import train_test_split


# logging info
logging.basicConfig(level=logging.DEBUG)

dbName = "rest_server/medisch_centrum_randstad/db.sqlite3"
tableName = "rest_api_netlify"
url = "http://localhost:8080/medish_centrum_randstad/api/netlify?page=1"
csvFile = "rest_server_new/medisch_centrum_randstad/data/data.csv"


##########################
### Read from REST API ###
##########################
# logging.info("Extract from REST API")
# response = requests.get(url)
# file_contents= response.json()  #dictionary
# logging.info("Load API Response into Pandas dataframe")
# df = pd.DataFrame.from_dict(file_contents['data'])
# #all the needed info was condensed into one data column called 'data'
# df3 = df.copy() #keep original for df3 
# logging.debug(df.head())
# logging.info("Load dataset in Database")


######################
### Read from .csv ###
######################
# df pd.read_csv('csvFile',skipinitialspace=True)
# df3 = df.copy() #keep original for df3
# logging.info("Load dataset in Database")


############################
### Read from SQlite3 db ###
############################

## saving the new df to SQL
dbConnection = sqlite3.connect(dbName)

# query db and write to pd:
dfFromDB = pd.read_sql_query(f"SELECT * FROM {'rest_api_netlify'}", dbConnection)
# sql adds index, remove:
df = dfFromDB.drop('id', axis=1)
pd.set_option('display.max_columns', 10)
# print(df.head())


#########################
### Regulair cleaning ### 
#########################

# remove negative values
df = df[(df >= 0).any(axis=1)]

# remove duplicates
df = df.drop_duplicates()

# convert non numeric to NaN
df = df.apply(lambda y: pd.to_numeric(y, errors='coerce') if y.dtype == 'object' else y)
df = df.apply(lambda y: pd.astype('float64') if y.dtype == 'object' else y)

# remove NaN
df = df.dropna()

# Add BMI
df['bmi'] = round(df['mass'] / (df['length'] / 100) ** 2, 1)



################################################## uncut 'lifespan','mass'
### df5 singificant values that dont need a cut### cut 'genetic','exercise','smoking','alcohol','bmi'
################################################## drop 'length'

# create df5 with lifespan and mass. length because they are not significant. Pearsons p_value > 0.05
df5 = df[['lifespan','mass']].copy()


################################
### Calculate cut vatriables ### 
################################

df_cut = df.copy()

## the IQR clipping for outliers 
# Computing IQR
Q1 = df_cut.quantile(0.25)
Q3 = df_cut.quantile(0.75)
IQR = Q3 - Q1

# Clipping the IQR*|15.*IQD|
df_cut = df_cut[~((df_cut < (Q1 - 1.5 * IQR)) |(df_cut > (Q3 + 1.5 * IQR))).any(axis=1)]
df_cut = df_cut[['genetic','exercise','smoking','alcohol','bmi']]

############################
### Join df_cut with df5 ###
############################

df5 = df5.join(df_cut)

# remove NaN
df5 = df5.dropna()
###################################
### Save, commit and close connection ###
###################################


# save to SQLlite
df5.to_sql('df5', if_exists='replace', con=dbConnection)
print('Generated DF5: succesfully written to SQL database')
df5.to_csv('df5.csv')
print('Generated DF5: succesfully written to df5.csv')



dbConnection.commit()
dbConnection.close()
