#Importing neccesary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Reading the csv file
importcsvfile = pd.read_csv('/Users/aditya/Downloads/train.csv')

#Grouping passengers by my chosen attributes
datagroupie = importcsvfile.groupby(['Age', 'Pclass', 'Embarked', 'Survived', 'Sex', 'SibSp'])

#passenger in each group
grpcount = datagroupie.size().reset_index(name='Passenger Count')

#Displaying the results
print(grpcount)

# Create count plots using Seaborn
plt.figure(figsize=(12, 6))
sns.countplot(data=grpcount, x='Age', hue='Survived')
plt.title('Passenger Count by Age Group (Survived vs. Not Survived)')
#printing the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
