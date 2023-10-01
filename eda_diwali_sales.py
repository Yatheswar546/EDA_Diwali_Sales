# -*- coding: utf-8 -*-
"""EDA_Diwali_Sales

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14CVs4X7smT6EE_ImUQh72YLpOK8UsXQn

#Importing Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

"""#Importing the dataset"""

dataset = pd.read_csv('/content/Diwali Sales Data.csv', encoding='unicode_escape');
#to avoid encoding error, use 'unicode_escape'

dataset.shape

dataset.head()

dataset.info()

"""#Deleting unrelated columns"""

dataset.drop(['Status','unnamed1'],axis=1,inplace=True);

"""#Data Cleaning
#Checking Null Values
"""

pd.isnull(dataset)

pd.isnull(dataset).sum()

"""#Deleting Null Values"""

dataset.dropna(inplace=True)

pd.isnull(dataset).sum()

"""#Changing datatype"""

dataset['Amount'] = dataset['Amount'].astype('int');

dataset['Amount'].dtypes

dataset.columns

"""#Renaming a column"""

dataset.rename(columns = {'Marital_Status':'Shaadi'})

dataset.describe()

dataset[['Age','Orders']].describe()

"""#Exploratory Data Analysis

#Gender
"""

gender = sb.countplot(x = 'Gender', data=dataset)

"""#Labeling the columns"""

gender = sb.countplot(x = 'Gender', data=dataset)

for bars in gender.containers:
  gender.bar_label(bars)

"""#Calculating the total amount based on gender using groupby"""

dataset.groupby(['Gender'],as_index=False)

dataset.groupby(['Gender'],as_index=False)['Amount'].sum()

gender_sales =dataset.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sb.barplot(x='Gender', y='Amount', data = gender_sales)

"""From above graphs we can conclude that most of the buyers are females

#Age
"""

age = sb.countplot(data = dataset, x='Age Group', hue='Gender')

age = sb.countplot(data = dataset, x='Age Group', hue='Gender')

for bars in age.containers:
  age.bar_label(bars)

"""#Calculating the total amount based on age using groupby"""

age_sales  = dataset.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sb.barplot(x='Age Group', y='Amount', data = age_sales)

"""From above data we can conclude that max. people are of age 26-35 which makes huge sales

#State
"""

state = sb.countplot(data = dataset, x='State')
plt.xticks(rotation=90)

for bars in state.containers:
  state.bar_label(bars)

"""#Total no. of orders from 10 states"""

state_sales = dataset.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
state_sales = sb.barplot(data = state_sales, x='State', y='Orders')
plt.xticks(rotation = 90)

for bars in state_sales.containers:
  state_sales.bar_label(bars)

"""From the above graph we can observe that most sales are from Uttar Pradesh, Maharashtra, Karnataka

#Marital Status
"""

marital_status = sb.countplot(data = dataset, x='Marital_Status')

for bars in marital_status.containers:
  marital_status.bar_label(bars)

marital_status_sales = dataset.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

marital_status_sales = sb.barplot(data = marital_status_sales, x='Marital_Status', y='Amount', hue='Gender')

for bars in marital_status_sales.containers:
  marital_status_sales.bar_label(bars)

"""From above graph we can say that most of the sales are from married women.

#Occupation
"""

sb.set(rc = {'figure.figsize': (20,5)})
occupation = sb.countplot(data = dataset, x='Occupation')

for bars in occupation.containers:
  occupation.bar_label(bars)
# plt.xticks(rotation=90)

occupation_sales = dataset.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

occupation_sales = sb.barplot(data = occupation_sales, x='Occupation', y='Amount')

# for bars in occupation_sales.containers:
#   occupation_sales.bar_label(bars)

"""From above graph most sales are from IT Sector, Health Care, Aviation

#Product Category
"""

sb.set(rc = {'figure.figsize': (20,5)})
products = sb.countplot(data = dataset, x='Product_Category')

for bars in products.containers:
  products.bar_label(bars)

products_sales = dataset.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

products_sales = sb.barplot(data = products_sales, x='Product_Category', y='Amount')

plt.xticks(rotation = 90)

"""From above graph we can conclude that most of products are from Food, Clothing & Electronics

#Top 10 Products based on Product ID's
"""

product_id = dataset.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sb.barplot(data = product_id, x='Product_ID', y='Orders')

"""#Conclusion

Based on the analysis we can conclude that most of the sales are done by Married women of age group 26-35 from UP, Maharastra and Karnataka working in IT Sector, Healthcare and Aviation and more likely to buy products from Food, Clothing & Electronics category
"""