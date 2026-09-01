load pandas as pd
# load a CSV file into a DataFrame using its path in trends clean
df = pd.read_csv('data/trends_clean.csv')
#Print shape of Trnds Clean Data Frame
print(f"Loaded Date {df.shape}")
#Print first 5 rows
print(f"\nFirst 5 Rows:")
print(df.head(5))
#Average of Score
avg_score = df['Score'].mean()
#Average of Num Comments
avg_comments = df['No Of Comments'].mean()
print(f"\n")
print(f"Average score   : {avg_score:,.0f}")
print(f"Average comments: {avg_comments:,.0f}")
#Basic Analysis with NumPy
# mean, median, and standard deviation of score
mean_score = df['Score'].mean()
median_score = df['Score'].median()
std_dev_score = df['Score'].std()
# highest score and lowest score
max_score = df['Score'].max()
min_score = df['Score'].min()
print(f"\n--- NumPy Stats ---")
print(f"Mean score   : {mean_score:,.0f}")
print(f"Median score : {median_score:,.0f}")
print(f"Std deviation: {std_dev_score:,.0f}")
print(f"Max score    : {max_score:,.0f}")
print(f"Min score    : {min_score:,.0f}")
# Category with the Most Stories
most_stories_category = df['Category'].value_counts().idxmax()
num_most_stories = df['Category'].value_counts().max()

print(f"\nMost stories in: {most_stories_category} ({num_most_stories} stories)")

# Story with the Most Comments
story_with_most_comments = df.loc[df['No Of Comments'].idxmax()]
most_comments_title = story_with_most_comments['Title']
most_comments_count = story_with_most_comments['No Of Comments']
print(f'\nMost commented story: "{most_comments_title}"    - {most_comments_count:,.0f} comments')

# Add new columns
df['engagement'] = df['No Of Comments'] / df['Score']+1
df['is_popular'] = df['Score']>df['Score'].mean()

# Display the new columns for verification
display(df[['Post_ID', 'Title', 'Score', 'No Of Comments', 'engagement', 'is_popular']].head())

#Save the Result
df.to_csv('data/trends_analysed.csv', index=False)
print(f"Saved {len(df)} rows to data/trends_analysed.csv")


#df = pd.read_csv('data/trends_clean.csv') lodes the csv file.
#df.shape gives number of rows and columns
#print(df.head(5)) prints top 5 details
#.mean will give average
#{avg_score:,.0f} number with comma seperated and have no decimals
#.mean gives mean,.meadian gives meadian .std give standard deviation
#.max will give highest value and .min gives lowest value
#value_counts() it will give count value of story category and .idxmax() gives the highest values for these values. .max wil return highest value.
#df['engagement'] adding new columns to the existing details
#df.to_csv('data/trends_analysed.csv', index=False) it will writes the data in csv format
