import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# step 1: load data set
df = pd.read_csv('https://health.data.ny.gov/resource/5dtw-tffi.csv')

## Display column names
print(df.columns)

## display the first few rows to verify
#df.head().  // this was not that great
# much better
print(df.head())

## remove all white space, lower case, replace space with underscore
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(','').str.replace(')','').str.replace('-','_')

# step 2: cleaning data
## change default to not display exponential notation but float
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Convert 'length_of_stay', 'total_charges', and 'total_costs' to numeric, and getting rid of commas
df['length_of_stay'] = pd.to_numeric(df['length_of_stay'].str.replace('+', ''), errors='coerce')
df['total_charges'] = pd.to_numeric(df['total_charges'].str.replace(',', ''), errors='coerce') #fix
df['total_costs'] = pd.to_numeric(df['total_costs'].str.replace(',', ''), errors='coerce') #fix


# Verify if conversion was successful
print(df[['length_of_stay', 'total_charges', 'total_costs']].head())



# Step 3: Descriptive statistics for Length of Stay (LOS), Total Charges, and Total Costs
## length of stay
print("\nDescriptive Stats for Length of Stay") ##fix?
print(df['length_of_stay'].describe())

## total charges
# Remove commas and convert 'total_charges' to numeric, forcing errors to NaN

print("\nDescriptive Stats for Total Charges") ##fix?
print(df['total_charges'].describe())

#total costs
print("\nDescriptive Stats for Total Costs") ##fix?
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



# Cap outliers at the 95th percentile
cap = df['total_charges'].quantile(0.95)
df['capped_total_charges'] = np.where(df['total_charges'] > cap, cap, df['total_charges'])

# Boxplot for Capped Total Charges
plt.figure(figsize=(8, 4))
sns.boxplot(data=df, x='capped_total_charges')
plt.title('Boxplot for Capped Total Charges')
plt.savefig('boxplot_capped_total_charges.png')
plt.show()

# Log transformation (add 1 to avoid log(0) issues)
df['log_total_charges'] = np.log1p(df['total_charges'])

# Boxplot for Log-transformed Total Charges
plt.figure(figsize=(8, 4))
sns.boxplot(data=df, x='log_total_charges')
plt.title('Boxplot for Log-transformed Total Charges')
plt.savefig('boxplot_log_total_charges.png')
plt.show()
# Summary of Findings: please see README.md
