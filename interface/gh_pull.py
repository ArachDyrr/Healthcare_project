# make sure that the db.sqlite3 is not actively ignored in github. 
# rest_server/medisch_centrum_randstad/db.sqlite3




import sqlite3
import pandas as pd

# establish connection to database
# conn = sqlite3.connect('https://github.com/<username>/<repository>/raw/<branch>/<path>/<database_name>.db')
# conn = sqlite3.connect('https://github.com/<username>/<repository>/raw/<branch>/rest_server/medisch_centrum_randstad/db.sqlite3.db')
conn = sqlite3.connect('https://github.com/ArachDyrr/Healthcare_project/blob/main/rest_server/medisch_centrum_randstad/db.sqlite3')
# conn = sqlite3.connect('https://github.com/ArachDyrr/Healthcare_project/raw/main/rest_server/medisch_centrum_randstad/db.sqlite3')
# conn = sqlite3.connect('https://github.com/ArachDyrr/Healthcare_project/raw/db.sqlite3')

# read data from database into pandas dataframe
df = pd.read_sql_query("SELECT * FROM <df1>", conn)

# # manipulate data using pandas
# df['new_column'] = df['old_column'] + 1

# # write updated data back to database
# df.to_sql('<table_name>', conn, if_exists='replace', index=False)

# close database connection
conn.close()


print(df.head())


# Groet,
# Stephan Dekker