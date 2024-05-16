#Importing the file format
import json

#

data = {

    'name': 'Amir Banks',
    'age': 29,
    'city': 'Anchorage, AK',
    'intrests': ['Tufting', 'Typing', 'Skating','Reading','Science'],
    'is_student': True
}



#Creating Json and writing the py objects contents to json.
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print("Data has been written to data.json")

# Opening the data.json file so it can be read as a JSON file.
with open('data.json','r') as json_file:

    #Create an object called loaded_data. Load the json file into the argument.
    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)


#Altering The JSON Object
loaded_data['age'] = 34 #<-ints
loaded_data['intrests'].append('Secret hobby')

#Rewrite the changes to the jason file.
with open('data.json','w') as json_file:

    json.dump(loaded_data,json_file,indent=4)

print("Data has been re-written to data.json")