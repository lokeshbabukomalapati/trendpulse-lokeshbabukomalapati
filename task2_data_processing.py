import pandas as pd
import json

# Path to JSON file
file_path = "data/trends_20260831.json"

# Load JSON into a JSON Directories
with open(file_path, 'r') as f:
    file_data = json.load(f)
# Flatten the dictionary of lists into a single list of dictionaries for DataFrame creation
flattened_data = []
for category, stories in file_data.items():
    for story in stories:
        flattened_data.append(story)

# Create DataFrame from the flattened list
df = pd.DataFrame(flattened_data)

print(f"Total rows loaded {len(df)}")

# Remove duplicates based on 'Post_ID'
df = df.drop_duplicates(subset='Post_ID', keep='first')
print(f"Total Duplicate Rows Dropped {len(df)}")

#reset index after dropping rows
df = df.reset_index(drop=True)
print(f"Total duplicate rows remain after dropped {df['Post_ID'].duplicated().sum()}")

# Get the count of missing values for each column
missing_values_count = df.isnull().sum()

# Display the missing values count
print("Missing values count per column:")
print(missing_values_count)

# Drop rows with missing values in key columns
df = df.dropna(subset=['Post_ID', 'Title', 'Score'])

# reset index after cleaning
df = df.reset_index(drop=True)

# Get the count of missing values for each column after dropping rows
missing_values_count_drop = df.isnull().sum()

# Display the missing values count
print("Missing values count per column after drop:")
print(missing_values_count_drop)

# Convert 'No Of Comments' to numeric, coercing errors to NaN
df['No Of Comments'] = pd.to_numeric(df['No Of Comments'], errors='coerce')

# Fill NaN values with 0 (or another appropriate value based on context)
df['No Of Comments'] = df['No Of Comments'].fillna(0)

# Convert the column to integer type
df['No Of Comments'] = df['No Of Comments'].astype('int64')

# Display the data types after conversion
print(df.dtypes)

#remove rows having score < 5
df = df[df['Score']>=5]
print(f"Count of rows not having Score < 5 {len(df)}")
df = df.reset_index(drop=True)

#strip extra spaces from the title column
df['Title'] = df['Title'].str.replace(r'\s+', ' ', regex=True).str.strip()

print(f"Remaining rows cout after cleaning {len(df)}")

output_path = "data/trends_clean.csv"
df.to_csv(output_path, index=False)

# Confirmation message
print(f"Saved {len(df)} rows to {output_path}")

# Summary: number of stories per category
print("\nStories per category:")
print(df['Category'].value_counts())

#Comments
#with open(file_path, 'r') as f: # opening file in readble mode.
#file_data = json.load(f) #Loads the data in json directories
#flattened_data = [] # Flatten the dictionary of lists into a single list of dictionaries for DataFrame creation
#for category, stories in file_data.items(): #this will loops for the key category and value stories
#again nested loop for stories
#flattened_data.append(story) #it will add the story to the flattened_data list
#df = pd.DataFrame(flattened_data) # creates dataframe for flattend_data
#drop_duplicates # removes the duplicates
#isnull checks for the null values or missing valus
#to_numeric(df['No Of Comments'], errors='coerce') #to_numeric will converts into numeric. coerce will place NaN for missed values or null values.
#.fillna(0) #changes NaN values to 0
#dropna removes any rows or columns having the null or missed values having NaN
#astype converts the data type
#df[df['Score']>=5] df['Score'] lists all scores. again it will filters the Scores having > 5
#str.replace(r'\s+', ' ', regex=True).str.strip() Stips the leading spaces by using regular expressions
#df.to_csv(output_path, index=False) will writes the data to csv file and index false will skips the rownum to write in file

