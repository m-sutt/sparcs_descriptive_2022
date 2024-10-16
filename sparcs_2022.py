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



# Step 2: so much maths -- descriptive statistics and categorical variables
## descriptive statistics for Length of Stay (LOS), Total Charges, and Total Costs
## added the "\n" for aesthetics

print("\nDescriptive Stats for Length of Stay")
print(df['length_of_stay'].describe())


print(df['total_charges'].isna().sum())
df = df.dropna(subset=['total_charges'])
print("\nDescriptive Stats for Total Charges") ## encountering a NaN situation, when doing dropna everything is zero.
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


## Histogram for Length of Stay
plt.hist(df['length_of_stay'].dropna(), bins=20, edgecolor='black')
plt.title('Distribution of Length of Stay')
plt.xlabel('Length of Stay')
plt.ylabel('Frequency')
plt.savefig('LOS_histogram.png')
plt.show()


## Boxplot for Total Charges
sns.boxplot(data=df, x='total_charges') #something is not quite right
plt.title('Boxplot for Total Charges')
plt.savefig('boxplot_total_charges.png')
plt.show()


# Summary of Findings: please see README.md
