import json  #importing json to use in python
import time #imprting time to use in python
import requests 
from datetime import datetime  #To work on date and time. Python doesnt have the date datatype
from pathlib import Path #To work on file path

#Creating data directory
data_dir = Path('data')
Path('data').mkdir(exist_ok=True)
#Placing the JSON file under data directory
file_path= data_dir/f"trends_{datetime.now().strftime('%Y%m%d')}.json"
print(f"A file at {file_path}")

base_url = "https://hacker-news.firebaseio.com/v0"  #This URL is base URL to create the URL for JSON files

#Category Groups to get the story ids
category_story_groups = {"technology":["AI","software","tech","code","computer","data","cloud","API","GPU","LLM"],
              "worldnews":["war","government","country","president","election","climate","attack","global"],
              "sports":["NFL","NBA","FIFA","sport","game","team","player","league","championship"],
              "science":["research","study","space","physics","biology","discovery","NASA","genome"],
              "entertainment":["movie","film","music","Netflix","game","book","show","award","streaming"]}
#header details
headers = {"User-Agent": "TrendPulse/1.0"}
#try and except is part of exceptional handling in python. Try will have the possible executable code. except has the exception logic. 
try:
	top_story_id_lists_response = requests.get(f"{base_url}/topstories.json")
	top_story_id_lists_response.raise_for_status()
	top_story_id_lists = top_story_id_lists_response.json()
except requests.RequestException as e:
    print(f"Failed to fetch top stories: {e}")
    top_story_id_lists = []
#Prints the top 125 story items
top_story_id_lists_subsets = top_story_id_lists[:]  #All story ids will get
all_story_list_details = []
print(f"Fetching details for {len(top_story_id_lists_subsets)} top stories...")
for top_story_id_lists_subset in top_story_id_lists_subsets:
    try:
        story_detail_list_response = requests.get(f"{base_url}/item/{top_story_id_lists_subset}.json")
        story_detail_list_response.raise_for_status() # Raise an exception for HTTP errors
        story_detail_list = story_detail_list_response.json()
        if story_detail_list: # Ensure story_details is not None or empty
            all_story_list_details.append(story_detail_list)
    except requests.RequestException as e:
        print(f"Failed to fetch details for story {top_story_id_lists_subset}: {e}")
    time.sleep(2) # Sleep logic. Sleep timer is 2 secs.

# 2. Filter stories by keywords from 'category_story_groups'
filtered_category_story = {category_story_group: [] for category_story_group in category_story_groups}

for all_story_list_detail in all_story_list_details:
    if all_story_list_detail and 'title' in all_story_list_detail: # Ensure story is valid and has a 'title' key
        category_story_title = all_story_list_detail['title'].lower()
        for category_story_group, category_story_keywords in category_story_groups.items():
            for category_story_keyword in category_story_keywords:
                if category_story_keyword.lower() in category_story_title:
                    filtered_category_story[category_story_group].append(all_story_list_detail)
                    break # Add to category and move to next story

# Prepare data for JSON output, including the 'Collected At' timestamp
output_data = {}
for category_name, storie_details in filtered_category_story.items():
    output_data[category_name] = [] # Initialize list for each category
    # Print top 5 stories
    print(f"\n--- {category_name.upper()} Stories ({len(storie_details)} total) ---")
    if not storie_details:
        print("  No stories found for this category.")
    else:
        for i, all_story_list_detail in enumerate(storie_details[:25]): # Display top 25 stories for each category
          print(f"  {i+1}. Post_ID: {all_story_list_detail.get('id', 'N/A')}")
          print(f"  \t Title: {all_story_list_detail.get('title', 'N/A')}")
          print(f"  \t Category: {category_name}")
          print(f"  \t Score: {all_story_list_detail.get('score', 'N/A')}")
          print(f"  \t No Of Comments: {all_story_list_detail.get('descendants', 'N/A')}")
          print(f"  \t Author: {all_story_list_detail.get('by', 'N/A')}")
          print(f"     Collected At: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Collect all stories for JSON output
    for all_story_list_detail in storie_details:
        story_info = {
            'Post_ID': all_story_list_detail.get('id', 'N/A'),
            'Title': all_story_list_detail.get('title', 'N/A'),
            'Category': category_name,
            'Score': all_story_list_detail.get('score', 'N/A'),
            'No Of Comments': all_story_list_detail.get('descendants', 'N/A'),
            'Author': all_story_list_detail.get('by', 'N/A'),
            'Collected At': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        output_data[category_name].append(story_info)
#Saving the story details to JSSON File. Indent 2 will give clear details and using commonly. Indent 4 will give data with more space and efficiently.
with open(file_path, 'w') as f:
json.dump(output_data, f, indent=4)

import pandas as pd
with open(file_path, 'r') as f:
    file_data = json.load(f)

# Flatten the dictionary of lists into a single list of dictionaries for DataFrame creation
flattened_data = []
for category, stories in file_data.items():
    for story in stories:
        flattened_data.append(story)

df_file_data = pd.DataFrame(flattened_data)
#Getting total stories based on unique post_id
total_stories = df_file_data['Post_ID'].nunique() if not df_file_data.empty else 0
print(f"Collected {total_stories} stories.Saved to {file_path}")


#Comments
#category_story_groups is dictionary having key and values. technology is a key inside [ ] are list of values.
#try - except is exceptional handling in python. Try has the possible executable statements. If any thing goes wrong then it is handled by except.
#top_story_id_lists = [] is used to not crash the code. If any APIs fail then this variable it will be used as still defined.
#story_detail_list_response.raise_for_status() # it will raise exception  if any fails for http request
#for all_story_list_detail #loop starts for the all_story_list_details
# if all_story_list_detail and 'title' in all_story_list_detail: # if statement checks to ensure story is valid and has a 'title' key 
#top_story_id_lists_response.json() # converts http requests to python objects
#for i, all_story_list_detail in enumerate(storie_details[:25]): #Display top 25 stories for each category
#flattened_data.append(story) # It will add the all story points to file
#logic first collects the story ids in a list. get the url.json based on base url. After story ids, logic will get the details of the story ids.It will get the top 25 stories as per category story ids.
