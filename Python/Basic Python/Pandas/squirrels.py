# Squirrels
import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color = data['Primary Fur Color']

gray = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray, cinnamon, black]
}
df = pandas.DataFrame(data_dict)
# print(df)
df.to_csv("new_data.csv")
