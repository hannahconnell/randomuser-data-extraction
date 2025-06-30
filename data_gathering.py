import requests
import pandas as pd
import json
from pandasql import sqldf
RU_URL = 'https://randomuser.me/api/'
GENDERIZE_URL = 'https://api.genderize.io'
API_KEY= '36b8d57defd066963ad04d9625c76613'

def load_data():
    # Gather 250 user objects from RandomUser
    response = requests.get(RU_URLsou, params ={'results': 250})
    data = response.json()
    df = pd.json_normalize(data['results'])

    # Send list of names from RandomUser to Genderize, while taking advantage of Genderize's batch processing
    gender_predictions = []
    name_list = df['name.first'].tolist()
    BATCH_SIZE = 10
    for i in range(0, len(name_list), BATCH_SIZE):
        batch = name_list[i:i+BATCH_SIZE]
        params = [("name[]", name) for name in batch]
        params.append(("apikey", API_KEY))

        gender_response = requests.get(GENDERIZE_URL, params=params)
        gender_predictions.extend(gender_response.json())

    gender_df = pd.DataFrame(gender_predictions)

    # Merge gender_df to existing df and remove redundant name column
    df = df.merge(gender_df, how="left", left_on="name.first", right_on="name")
    df.drop(columns=["name"])
    return df
    
df = load_data()