# Setup

# Load the analysed data to trends_analysed
df = pd.read_csv('data/trends_analysed.csv')

#outputs file creation
from pathlib import Path
Path('outputs').mkdir(exist_ok=True)

import matplotlib.pyplot as plt
import pandas as pd

#Chart 1: Top 10 Stories by Score
# Step 1: Get top 10 stories by score
top_stories_score = df.sort_values(by='Score', ascending=False).head(10)

# Step 2: Shorten titles to max 50 characters
top_stories_score['Short_Title'] = top_stories_score['Title'].apply(
    lambda x: x[:50] + '...' if len(x) > 50 else x
)

# Step 3: Create horizontal bar chart
plt.figure(figsize=(12, 8))

plt.barh(top_stories_score['Short_Title'], top_stories_score['Score'])

# Highest score on top
plt.gca().invert_yaxis()

# Titles and labels
plt.title("Top 10 Stories by Score", fontsize=16)
plt.xlabel("Score", fontsize=12)
plt.ylabel("Story Title", fontsize=12)

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('outputs/chart1_top_stories.png')
plt.show()


#Chart 2: Stories per Category
# Step 1: Count stories per category
category_counts = df['Category'].value_counts()

# Step 2: Create bar chart
plt.figure()

plt.bar(category_counts.index, category_counts.values, color=plt.cm.tab10.colors)

# Step 3: Add title and labels
plt.title("Number of Stories by Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

# Step 4: Save BEFORE show
plt.savefig("outputs/chart2_categories.png", dpi=300, bbox_inches='tight')

# Step 5: Show chart
plt.show()

#close figure
plt.close()

#Chart 3: Score vs Comments
# Step 1: Split data based on popularity
popular = df[df['is_popular'] == True]
not_popular = df[df['is_popular'] == False]

# Step 2: Create scatter plot
plt.figure()

plt.scatter(popular['Score'], popular['No Of Comments'], label='Popular')
plt.scatter(not_popular['Score'], not_popular['No Of Comments'], label='Not Popular')

# Step 3: Labels and title
plt.title("Score vs Number of Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")

# Step 4: Legend
plt.legend()

# Step 5: Save BEFORE show
plt.savefig("outputs/chart3_scatter.png", dpi=300, bbox_inches='tight')

# Step 6: Show plot
plt.show()

# close figure
plt.close()

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

#Dashboard

# -------------------------
# Chart 1: Top 10 stories
# -------------------------
top10 = df.sort_values(by='Score', ascending=False).head(10)
top10['Short_Title'] = top10['Title'].apply(
    lambda x: x[:50] + '...' if len(x) > 50 else x
)

axes[0].barh(top10['Short_Title'], top10['Score'])
axes[0].invert_yaxis()
axes[0].set_title("Top 10 Stories")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Title")

# -------------------------
# Chart 2: Categories
# -------------------------
category_counts = df['Category'].value_counts()
axes[1].bar(category_counts.index, category_counts.values,color=plt.cm.tab10.colors)
axes[1].set_title("Stories by Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis='x', rotation=45)

# -------------------------
# Chart 3: Scatter plot
# -------------------------
popular = df[df['is_popular'] == True]
not_popular = df[df['is_popular'] == False]

axes[2].scatter(popular['Score'], popular['No Of Comments'], label='Popular')
axes[2].scatter(not_popular['Score'], not_popular['No Of Comments'], label='Not Popular')

axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Comments")
axes[2].legend()

# -------------------------
# Dashboard title
# -------------------------
fig.suptitle("TrendPulse Dashboard", fontsize=16)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Save BEFORE show
plt.savefig("outputs/dashboard.png", dpi=300, bbox_inches='tight')

# Show
plt.show()

plt.close()



#df.sort_values(by='Score', ascending=False).head(10) sorting the values by descending order for top 10
#lambda x: x[:50] + '...' if len(x) > 50 else x will checks for the 50 characters. If character count is >50 then it will return ..... and if count is <50 hen it will print as is
#plt.barh horizontal bar
#plt.bar(category_counts.index, category_counts.values, color=plt.cm.tab10.colors) #bar graph having different colurs for diffrent bars
#plt.savefig saves the graph in image format.
#plt.scatter scatter graph with popular and non popular
#plt.title gives the title of the graph
#plt.xlabel gives label to x axis and plt.ylabel gives label to y axis
