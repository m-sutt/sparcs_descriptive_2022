import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# step 1: load data set
df = pd.read_csv('https://health.data.ny.gov/resource/5dtw-tffi.csv')

## Display column names
print(df.columns)

## display the first few rows to verify
df.head()

# step 2: cleaning data
## change default to not display exponential notation but float
pd.set_option('display.float_format', lambda x: '%.3f' % x)

##  # Convert 'length_of_stay' to numeric, forcing errors to NaN
df['length_of_stay'] = pd.to_numeric(df['length_of_stay'], errors='coerce')
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
df['total_costs'] = pd.to_numeric(df['total_costs'], errors='coerce')


## remove all white space, lower case, replace space with underscore
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(','').str.replace(')','').str.replace('-','_')
df_len = len(df)


## remove commas from total_charges and total_costs
df.total_charges = df.total_charges.apply(lambda x : x.replace(',', ''))
df.total_costs = df.total_costs.apply(lambda x : x.replace(',', ''))

# Step 2: so much maths -- descriptive statistics and categorical variables
## descriptive statistics for Length of Stay (LOS), Total Charges, and Total Costs
## added the "\n" for aesthetics

print("\nDescriptive Stats for Length of Stay")
print(df['length_of_stay'].describe())

print("\nDescriptive Stats for Total Charges")
print(df['total_charges'].describe())

print("\nDescriptive Stats for Total Costs")
print(df['total_costs'].describe())

## count distribution for Age Group, Gender, and Type of Admission
print("\nAge Group Distribution")
print(df['age_group'].value_counts())

print("\nGender Distribution")
print(df['gender'].value_counts())

print("\nType of Admission Distribution")
print(df['type_of_admission'].value_counts())

# Step 3: Visualization
##

## Bar plot for Age Group
plt.figure(figsize=(6, 4))
sns.countplot(x='age_group', data=df, order=df['age_group'].value_counts().index)
plt.title('Distribution of Age Group')
plt.xlabel('Age Group')
plt.ylabel('Frequency')
plt.savefig('barplot_age_group.png')
plt.show()

## Bar plot for Gender
plt.figure(figsize=(6, 4))
sns.countplot(x='gender', data=df, order=df['gender'].value_counts().index)
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.savefig('barplot_gender.png')
plt.show()

## Bar plot for Type of Admission
plt.figure(figsize=(6, 4))
sns.countplot(x='type_of_admission', data=df, order=df['type_of_admission'].value_counts().index)
plt.title('Distribution of Admission Types')
plt.xlabel('Admission Types')
plt.ylabel('Frequency')
plt.savefig('barplot_type_of_admission.png')
plt.show()

