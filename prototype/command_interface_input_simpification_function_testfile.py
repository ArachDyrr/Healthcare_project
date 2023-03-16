import logging
import pandas as pd


# input safeguarding


def inputDigit(message, acceptableRange):
    inputStr = str()
    withinRange = False
    numberOfTries = 3
    inputNum = None
    i = 0

    while not (inputStr.isdigit() and withinRange) and i < numberOfTries:
        inputStr = input(message)
        logging.debug(inputStr)

        if inputStr.isdigit():
            inputNum = float(inputStr)

            if inputNum in acceptableRange:
                return inputNum

        i += 1

    return None

# initialize data of lists.
data_questions = {'feature': ['genetic', 'length', 'mass', 'alcohol', 'sugar', 'smoking', 'exercise'],
        'acc_min': [50,140,40,0,0,0,0],
        'acc_max': [121,221,171,21,21,41,9],
        'per':['age in years','in cm','in kg','consumption in glasses per day',
               'consumption in cubes per day','in sigarettes per day','in hours per day'] }

# Create DataFrame
df_q = pd.DataFrame(data_questions) 

print (df_q)



def input_q(name):
    min,max, per = df_q.loc[df_q['feature'] == name, ['acc_min','acc_max', 'per']].values[0]
    return int(inputDigit(f"Please enter, {name} {per} in the range: {min}-{max-1} ", range(min,max)))
    
print()
genetic='genetic'
test = input_q (genetic)
print (test)


# # Select 'acceptable' and 'per' values for the 'genetic' feature
# acceptable, per = df_q.loc[df_q['feature'] == 'genetic', ['acceptable', 'per']].values[0]

# # Print the results
# print(f"Acceptable range for genetic feature: {acceptable}")
# print(f"Unit of measurement for genetic feature: {per}")
print()
test = input_q ('mass')
print (test)
