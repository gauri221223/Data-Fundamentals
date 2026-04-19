import pandas as pd

#Load data
df = pd.read_csv("std_reg.csv")
print("Original Data:")
print(df)

#Find the duplicate 
duplicates = df[df.duplicated()]
print("\nDuplicate Records:")
print(duplicates)

#Remove duplicates based on StudentID
df_clean = df.drop_duplicates(subset="StudentID",keep = "first")

print("\nCleaned Data:")
print(df_clean)

#Save cleaned data
df_clean.to_csv("Cleaned_students.csv",index = False )