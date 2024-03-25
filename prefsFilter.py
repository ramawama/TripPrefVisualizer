# Read in and store the data from 'PrefsTemplate.xlsx'

import pandas as pd
from datetime import datetime
import os
import json
from database import trip_leader
from database import trip
from database import trip_preference

# function to read the excel spreadsheet
def read_data(file_path):
    data = {}
    sheet1_data = []
    sheet2_data = []

    # read data from Sheet 1: "Prefs Template"

    # df = DataFrame
    df = pd.read_excel(file_path, sheet_name='Prefs Template', index_col=0)
    df = df.rename(columns={"Unnamed: 2": "TRiP", "Unnamed: 3": "Preferences"})
    columns_deleted = ['Unnamed: 1', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6']
    df.drop(columns_deleted, axis=1, inplace=True)

    for index, row in df.iterrows():
        # C Column: "TRiP" - Trip Names
        trip_name = row['TRiP']
        # D Column: "Preferences" - Preference Ratings (0-5)
        preference_rating = row['Preferences']

        # print(f"Trip Date: {trip_date}, Trip Name: {trip_name}, Preference Rating: {preference_rating}")

        sheet1_data.append({"Trip Name": trip_name, "Preference Rating": preference_rating})

    # remove the first line appended (titles of columns)
    if sheet1_data:
        sheet1_data.pop(0)

    # read data from Sheet 2: "Trip Leader Information"

    df = pd.read_excel(file_path, sheet_name='Trip Leader Information', index_col=0)

    # df.iloc[row_index, column_index]
    # Name
    trip_leader_name = df.iloc[2,1]
    # UFID
    leader_ufid = df.iloc[3,1]
    # Semesters Left
    semesters_left = df.iloc[4,1]
    # Satisfaction Rating
    satisfaction_rating = df.iloc[5,1]
    # Number of TRiPs assigned last semester
    trips_last_semester = df.iloc[7,1]
    # TRiPs Dropped
    trips_dropped = df.iloc[8,1]
    # TRiPs Picked-Up
    trips_pickedup = df.iloc[9,1]
    
    # Categories interested in becoming a Lead Guide (0-3)
    categories_of_interest = []
    # check if a category of interest 1 was inputted    
    if len(df) > 12 and len(df.columns) > 1:
        category1 = df.iloc[12, 1]
        if not is_blank(category1):
            categories_of_interest.append(category1)
    # check if a category of interest 2 was inputted  
    if len(df) > 12 and len(df.columns) > 2:
        category2 = df.iloc[12, 2]
        if not is_blank(category2):
            categories_of_interest.append(category2)  
    # check if a category of interest 3 was inputted  
    if len(df) > 12 and len(df.columns) > 3:
        category3 = df.iloc[12, 3]
        if not is_blank(category3):
            categories_of_interest.append(category3)

    # Preferred TRiP Leaders (0-3)
    preferred_leaders = []
    # check if a preferred leader 1 was inputted
    if len(df) > 14 and len(df.columns) > 1:
        preferred_leader1 = df.iloc[14, 1]
        if not is_blank(preferred_leader1):
            preferred_leaders.append(preferred_leader1)
    # check if a preferred leader 2 was inputted
    if len(df) > 14 and len(df.columns) > 2:
        preferred_leader2 = df.iloc[14, 2]
        if not is_blank(preferred_leader2):
            preferred_leaders.append(preferred_leader2)
    # check if a preferred leader 3 was inputted
    if len(df) > 14 and len(df.columns) > 3:
        preferred_leader3 = df.iloc[14, 3]
        if not is_blank(preferred_leader3):
            preferred_leaders.append(preferred_leader3)

    # preferred_leaders = json.dumps(preferred_leaders)
    # trip_leader.create_leader()
    # l == preferred_leaders
    sheet2_data.append({"TRiP Leader Name": trip_leader_name, "UFID": leader_ufid, "Semesters Left": semesters_left, "Satisfaction Rating": satisfaction_rating, "Number of trips assigned last semester": trips_last_semester, "Trips Dropped": trips_dropped, "Trips Picked Up": trips_pickedup, "Categories interested in becoming a lead guide": categories_of_interest, "Preferred Leaders to lead with": preferred_leaders})

    data["sheet1_data"] = sheet1_data
    data["sheet2_data"] = sheet2_data

    return data

def is_blank(value):
    # Function to check if a value is blank
    return pd.isna(value) or value == ""

def convert_to_serializable(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    else:
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def write_data(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4, default=convert_to_serializable)


def main():
    curr_directory = os.path.dirname(__file__) # gets the current directory to add to the relative path
    file_name = "NEWRachelPrefs.xlsx"
    file_path = os.path.join(curr_directory, file_name) # creates the relative path
    data = read_data(file_path)
    write_data(data, "NEWRachel.json")

if __name__ == "__main__":
    main()


# TO RUN: python prefsFilter.py