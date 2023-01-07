import json as j
import csv
from time_manipulation import find_time
import pandas as pd

#json file deserializing
data = []
for line in open('recipes.json','r'):
    data.append(j.loads(line))


#create a list of target words and similar instances
list_of_words = ['chili','chilies','chiles','chilli']

#looking for the target words in the data and extracting them into a new object
extracted_recipes = []
for i in data:
    if any(word in i['ingredients'].lower() for word in list_of_words):
        extracted_recipes.append(i)
    

#creating a new field to keep the total time it takes to cook a rewcipe which consists of cookTime and prepTime
for i in extracted_recipes:
    if find_time(i['cookTime']):
        if find_time(i['prepTime']):
            i['totalTime'] = find_time(i['cookTime']) + find_time(i['prepTime'])
        else:
            i['totalTime'] = find_time(i['cookTime'])
    elif find_time(i['prepTime']):
        i['totalTime'] = find_time(i['prepTime'])
    else:
       i['totalTime'] = 'unknown'

#based on the totalTime, a new field is created to categorize the difficulty level of each recipe
for i in extracted_recipes:
    if i['totalTime'] >= 60:
        i['difficulty'] = 'Hard'
    elif i['totalTime'] >= 30 and i['totalTime'] < 60:
        i['difficulty'] = 'Meduim'
    elif i['totalTime'] < 30:
        i['difficulty'] = 'Easy'
    else:
        i['difficulty'] = 'Unkown'

##creating the requested CSV file 
# for i in extracted_recipes:
#     print(i['name'], i['prepTime'],i['cookTime'],i['totalTime'],i['difficulty'])

# data_file = open('test.csv', 'w')
# csv_writer = csv.writer(data_file)
# count = 0
# for rec in extracted_recipes:
#     if count == 0:
#         header = rec.keys()
#         csv_writer.writerow(header)
#     csv_writer.writerow(rec.values())
# data_file.close()
