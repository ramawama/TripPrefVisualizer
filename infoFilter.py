# Read in and store the data from 'TripsAndLeaderStatusInfo.xlsx'
# Read in and store the data from 'PrefsTemplate.xlsx'

import pandas as pd
from datetime import datetime
import os
import json
from database import trip_leader
from database import trip
from database import trip_preference

# function to read the excel spreadsheet
def read_TripInfo(file_path2, file_path1):
    data1 = {}
    sheet1_data = []
    sheet2_data = []

    # read data from Sheet 1: "Prefs Template"

    # df = DataFrame
    df = pd.read_excel(file_path2, sheet_name='Prefs Template', index_col=0, skiprows=1)
    df = df.rename(columns={"Unnamed: 1": "Start Date", "Unnamed: 2": "End Date", "Unnamed: 3": "TRiP", "Unnamed: 4": "Trip Category", "Unnamed: 5": "# of Total Guides Needed", "Unnamed: 6": "# of Lead Guides Needed"})

    # put dates in proper format: '%m-%d-%Y'
    df['Start Date'] = pd.to_datetime(df['Start Date'], format='%m-%d-%Y')
    df['End Date'] = pd.to_datetime(df['End Date'], format='%m-%d-%Y')
    trip_number = 0

    for index, row in df.iterrows():
        trip_number += 1  
        # B Column: "Start Date"
        start_date = row['Start Date'].strftime('%m-%d-%Y')
        # C Column: "End Date" --- check if 'End Date' cell is empty
        if pd.notna(row['End Date']):
            end_date = row['End Date'].strftime('%m-%d-%Y')
        else:
            end_date = start_date
        # D Column: "TRiP"
        trip_title = row['TRiP']
        # E Column: "Trip Category"
        trip_category = row['Trip Category']
        # F Column: "# of Total Guides Needed"
        num_total_guides = row['# of Total Guides Needed']
        # G Column: "# of Lead Guides Needed"
        num_lead_guides = row['# of Lead Guides Needed']

        # print(f"Start Date: {start_date}, End Date: {end_date}, TRiP: {trip_title}, Trip Category: {trip_category}, # of Total Guides Needed: {num_total_guides}, # of Lead Guides Needed: {num_lead_guides}")

        # def create_trip(id, name, category, start_date, end_date, lead_guides_needed, total_guides_needed)
        trip.create_trip(trip_number, trip_title, trip_category, start_date, end_date, num_lead_guides, num_total_guides)

        sheet1_data.append({"Start Date": start_date, "End Date": end_date, "TRiP": trip_title, "Trip Category": trip_category, "# of Total Guides Needed": num_total_guides, "# of Lead Guides Needed": num_lead_guides})
    
    # read data from Sheet 2: "Trip Leader Info"
    df = pd.read_excel(file_path2, sheet_name='Trip Leader Info', index_col=0, skiprows=3)
    df = df.rename(columns={"Unnamed: 1": "Class", "Unnamed: 2": "Name", "Unnamed: 3": "Overnight", "Unnamed: 4": "Mountain Biking", "Unnamed: 5": "Spelunking", "Unnamed: 6": "Watersports", "Unnamed: 7": "Surfing", "Unnamed: 8": "Sea Kayaking"})
    columns_deleted = ['Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11']
    df.drop(columns_deleted, axis=1, inplace=True)

    for index, row in df.iterrows():
        # B Column: "Class" - TRiP Leader's Year
        if pd.notna(row['Class']):
            leader_class = int(row['Class'])
        # stop recording data if no more leaders are in the chart
        else:
            break
        # C Column: "Name" - TRiP Leader's Name
        if pd.notna(row['Name']):
            leader_name = row['Name']
        # D Column: "Overnight" - Promotional Category
        if pd.notna(row['Overnight']):
            category_overnight = row['Overnight']
        else:
            category_overnight = "None"
        # E Column: "Mountain Biking" - Promotional Category
        if pd.notna(row['Mountain Biking']):
            category_mountain_biking = row['Mountain Biking']
        else:
            category_mountain_biking = "None"
        # F Column: "Spelunking" - Promotional Category
        if pd.notna(row['Spelunking']):
            category_spelunking = row['Spelunking']
        else:
            category_spelunking = "None"
        # G Column: "Watersports" - Promotional Category
        if pd.notna(row['Watersports']):
            category_watersports = row['Watersports']
        else:
            category_watersports = "None"
        # H Column: "Surfing" - Promotional Category
        if pd.notna(row['Surfing']):
            category_surfing = row['Surfing']
        else:
            category_surfing = "None"
        # I Column: "Sea Kayaking" - Promotional Category
        if pd.notna(row['Sea Kayaking']):
            category_sea_kayaking = row['Sea Kayaking']
        else:
            category_sea_kayaking = "None"

        sheet2_data.append({"Class": leader_class, "Name": leader_name, "Overnight": category_overnight, "Mountain Biking": category_mountain_biking, "Spelunking": category_spelunking, "Watersports": category_watersports, "Surfing": category_surfing, "Sea Kayaking": category_sea_kayaking})

    # Total LG
    # Promotion Category: Overnight
    total_LG_overnight = df.iloc[30,2]
    # Promotion Category: Mountain Biking
    total_LG_mountain_biking = df.iloc[30,3]
    # Promotion Category: Spelunking
    total_LG_spelunking = df.iloc[30,4]
    # Promotion Category: Watersports
    total_LG_watersports = df.iloc[30,5]
    # Promotion Category: Surfing
    total_LG_surfing = df.iloc[30,6]
    # Promotion Category: Sea Kayaking
    total_LG_sea_kayaking = df.iloc[30,7]

    sheet2_data.append({"Title": "Total LG", "Overnight": total_LG_overnight, "Mountain Biking": total_LG_mountain_biking, "Spelunking": total_LG_spelunking, "Watersports": total_LG_watersports, "Surfing": total_LG_surfing, "Sea Kayaking": total_LG_sea_kayaking})

    data1["sheet1_data"] = sheet1_data
    data1["sheet2_data"] = sheet2_data

    # return data1

    data2 = {}
    sheet3_data = []
    sheet4_data = []

    # read data from Sheet 3: "Prefs Template"

    # df = DataFrame
    df = pd.read_excel(file_path1, sheet_name='Prefs Template', index_col=0)
    df = df.rename(columns={"Unnamed: 2": "TRiP", "Unnamed: 3": "Preferences"})
    columns_deleted = ['Unnamed: 1', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6']
    df.drop(columns_deleted, axis=1, inplace=True)

    for index, row in df.iterrows():
        # C Column: "TRiP" - Trip Names
        trip_name = row['TRiP']
        # D Column: "Preferences" - Preference Ratings (0-5)
        preference_rating = row['Preferences']

        # print(f"Trip Date: {trip_date}, Trip Name: {trip_name}, Preference Rating: {preference_rating}")

        sheet3_data.append({"Trip Name": trip_name, "Preference Rating": preference_rating})

    # remove the first line appended (titles of columns)
    if sheet3_data:
        sheet3_data.pop(0)

    # read data from Sheet 4: "Trip Leader Information"

    df = pd.read_excel(file_path1, sheet_name='Trip Leader Information', index_col=0)

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

    sheet4_data.append({"TRiP Leader Name": trip_leader_name, "UFID": leader_ufid, "Semesters Left": semesters_left, "Satisfaction Rating": satisfaction_rating, "Number of trips assigned last semester": trips_last_semester, "Trips Dropped": trips_dropped, "Trips Picked Up": trips_pickedup, "Categories interested in becoming a lead guide": categories_of_interest, "Preferred Leaders to lead with": preferred_leaders})

    # def create_leader(ufid, name, class_year, semesters_left, reliability_score, num_trips_assigned, preferred_co_leaders, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role)
    preferred_leaders = json.dumps(preferred_leaders)
    # trip_leader.create_leader()

    data2["sheet3_data"] = sheet3_data
    data2["sheet4_data"] = sheet4_data

    return data1


# function to read the excel spreadsheet
def read_LeaderInfo(file_path):
    data2 = {}
    sheet3_data = []
    sheet4_data = []

    # read data from Sheet 3: "Prefs Template"

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

        sheet3_data.append({"Trip Name": trip_name, "Preference Rating": preference_rating})

    # remove the first line appended (titles of columns)
    if sheet3_data:
        sheet3_data.pop(0)

    # read data from Sheet 4: "Trip Leader Information"

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
    sheet4_data.append({"TRiP Leader Name": trip_leader_name, "UFID": leader_ufid, "Semesters Left": semesters_left, "Satisfaction Rating": satisfaction_rating, "Number of trips assigned last semester": trips_last_semester, "Trips Dropped": trips_dropped, "Trips Picked Up": trips_pickedup, "Categories interested in becoming a lead guide": categories_of_interest, "Preferred Leaders to lead with": preferred_leaders})

    data2["sheet3_data"] = sheet3_data
    data2["sheet4_data"] = sheet4_data

    return data2


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

    file_name1 = "Example_Data\\Prefs\\RachelPrefs.xlsx"
    file_path1 = os.path.join(curr_directory, file_name1)

    # Read in and store the data from 'TripsAndLeaderStatusInfo.xlsx'
    file_name2 = "Example_Data\\TripsAndLeaderStatusInfo.xlsx"
    file_path2 = os.path.join(curr_directory, file_name2) # creates the relative path
    data2 = read_TripInfo(file_path2, file_path1)
    write_data(data2, "Example_Data\\TripInfo.json")

    # Read in and store the data from 'PrefsTemplate.xlsx'
    # file_name1 = "NEWRachelPrefs.xlsx"
    # file_path1 = os.path.join(curr_directory, file_name1) # creates the relative path
    data1 = read_LeaderInfo(file_path1)
    write_data(data1, "Example_Data\\Prefs\\Rachel.json")

if __name__ == "__main__":
    main()


# TO RUN: python infoFilter.py