import pandas as pd
import numpy as np
import sklearn
from lets_plot import *

print("Pandas:", pd.__version__)
print("NumPy:", np.__version__)
print("sklearn:", sklearn.__version__)

# Load the dataset directly from GitHub
url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/star-wars-survey/StarWars.csv"
df = pd.read_csv(url, encoding="ISO-8859-1")

print("Rows:", df.shape[0], "Columns:", df.shape[1])
df.head()

print("\n--- Original Column Names ---")
for i, col in enumerate(df.columns):
    print(i, col)

print("\n--- Original Column Names ---")
for i, col in enumerate(df.columns):
    print(i, col)



rename_map = {
    "RespondentID": "respondent_id",
    
    "Have you seen any of the 6 films in the Star Wars franchise?":
        "seen_any",
        
    "Do you consider yourself to be a fan of the Star Wars film franchise?":
        "fan_starwars",
        
    "Which of the following Star Wars films have you seen? Please select all that apply.":
        "seen_films",
        
    "Unnamed: 4": "seen_ep1",
    "Unnamed: 5": "seen_ep2",
    "Unnamed: 6": "seen_ep3",
    "Unnamed: 7": "seen_ep4",
    "Unnamed: 8": "seen_ep5",
    
    "Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.":
        "rank_ep1",
    "Unnamed: 10": "rank_ep2",
    "Unnamed: 11": "rank_ep3",
    "Unnamed: 12": "rank_ep4",
    "Unnamed: 13": "rank_ep5",
    "Unnamed: 14": "rank_ep6",
    
    "Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.":
        "char_luke",
    "Unnamed: 16": "char_han",
    "Unnamed: 17": "char_leia",
    "Unnamed: 18": "char_anakin",
    "Unnamed: 19": "char_obiwan",
    "Unnamed: 20": "char_emperor",
    "Unnamed: 21": "char_darthmaul",
    "Unnamed: 22": "char_yoda",
    "Unnamed: 23": "char_boba",
    "Unnamed: 24": "char_jabba",
    "Unnamed: 25": "char_padme",
    "Unnamed: 26": "char_jarjar",
    "Unnamed: 27": "char_palpatine",
    "Unnamed: 28": "char_mace",
    
    "Which character shot first?": "shot_first",
    "Are you familiar with the Expanded Universe?": "know_eu",
    "Do you consider yourself to be a fan of the Expanded Universe?æ":
        "fan_eu",
    "Do you consider yourself to be a fan of the Star Trek franchise?":
        "fan_startrek",
    
    "Gender": "gender",
    "Age": "age_range",
    "Household Income": "income_range",
    "Education": "education",
    "Location (Census Region)": "location"
}

df = df.rename(columns=rename_map)

print("\n--- Cleaned Column Names ---")
for col in df.columns:
    print(col)
