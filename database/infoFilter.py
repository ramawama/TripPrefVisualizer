# Read in and store the data from 'TripsAndLeaderStatusInfo.xlsx'
# Read in and store the data from 'PrefsTemplate.xlsx'

import pandas as pd
from datetime import datetime
import os
import json
import trip_leader
import trip
import trip_preference
#from server.server import upload_path
import sys
#from server.server import upload_path

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir=os.path.dirname(current_dir)
database_files_dir=os.path.join(root_dir, 'server')
sys.path.append(database_files_dir)

import server
from server import upload_path



# function to read the excel spreadsheet
def read_TripInfo(filepath_info, filepath_prefs):
    data_info = {}
    sheet1_info = []
    sheet2_info = []

    data_prefs = {}
    sheet3_prefs = []
    sheet4_prefs = []


    # read data from Info-Sheet 1: "Prefs Template"

    # df = DataFrame
    df = pd.read_excel(filepath_info, sheet_name='Prefs Template', index_col=0, skiprows=1)
    df = df.rename(columns={"Unnamed: 1": "Start Date", "Unnamed: 2": "End Date", "Unnamed: 3": "TRiP", "Unnamed: 4": "Trip Category", "Unnamed: 5": "# of Total Guides Needed", "Unnamed: 6": "# of Lead Guides Needed"})

    # put dates in proper format: '%m-%d-%Y'
    df['Start Date'] = pd.to_datetime(df['Start Date'], format='%m-%d-%Y')
    df['End Date'] = pd.to_datetime(df['End Date'], format='%m-%d-%Y')

    trip.delete_all_trips()
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
        # if row['Trip Category'] != "Biking":
        #     trip_category = row['Trip Category']
        # else:
        #     trip_category = "Mountain Biking"
        trip_category = row['Trip Category']
        # F Column: "# of Total Guides Needed"
        num_total_guides = row['# of Total Guides Needed']
        # G Column: "# of Lead Guides Needed"
        num_lead_guides = row['# of Lead Guides Needed']

        # print(f"Start Date: {start_date}, End Date: {end_date}, TRiP: {trip_title}, Trip Category: {trip_category}, # of Total Guides Needed: {num_total_guides}, # of Lead Guides Needed: {num_lead_guides}")
        
        # def create_trip(id, name, category, start_date, end_date, lead_guides_needed, total_guides_needed)
        trip.create_trip(trip_number, trip_title, trip_category, start_date, end_date, num_lead_guides, num_total_guides)

        sheet1_info.append({"Start Date": start_date, "End Date": end_date, "TRiP": trip_title, "Trip Category": trip_category, "# of Total Guides Needed": num_total_guides, "# of Lead Guides Needed": num_lead_guides})
    
    # read data from Info-Sheet 2: "Trip Leader Info"
    df = pd.read_excel(filepath_info, sheet_name='Trip Leader Info', index_col=0, skiprows=3)
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
            if row['Overnight'] == "LG":
                category_overnight = "Lead"
            elif row['Overnight'] == "I":
                category_overnight = "Promotion"
        else:
            category_overnight = "None"
        # E Column: "Mountain Biking" - Promotional Category
        if pd.notna(row['Mountain Biking']):
            if row['Mountain Biking'] == "LG":
                category_mountain_biking = "Lead"
            elif row['Mountain Biking'] == "I":
                category_mountain_biking = "Promotion"
        else:
            category_mountain_biking = "None"
        # F Column: "Spelunking" - Promotional Category
        if pd.notna(row['Spelunking']):
            if row['Spelunking'] == "LG":
                category_spelunking = "Lead"
            elif row['Spelunking'] == "I":
                category_spelunking = "Promotion"
        else:
            category_spelunking = "None"
        # G Column: "Watersports" - Promotional Category
        if pd.notna(row['Watersports']):
            if row['Watersports'] == "LG":
                category_watersports = "Lead"
            elif row['Watersports'] == "I":
                category_watersports = "Promotion"
        else:
            category_watersports = "None"
        # H Column: "Surfing" - Promotional Category
        if pd.notna(row['Surfing']):
            if row['Surfing'] == "LG":
                category_surfing = "Lead"
            elif row['Surfing'] == "I":
                category_surfing = "Promotion"
        else:
            category_surfing = "None"
        # I Column: "Sea Kayaking" - Promotional Category
        if pd.notna(row['Sea Kayaking']):
            if row['Sea Kayaking'] == "LG":
                category_sea_kayaking = "Lead"
            elif row['Sea Kayaking'] == "I":
                category_sea_kayaking = "Promotion"
        else:
            category_sea_kayaking = "None"

        sheet2_info.append({"Class": leader_class, "Name": leader_name, "Overnight": category_overnight, "Mountain Biking": category_mountain_biking, "Spelunking": category_spelunking, "Watersports": category_watersports, "Surfing": category_surfing, "Sea Kayaking": category_sea_kayaking})

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

    sheet2_info.append({"Title": "Total LG", "Overnight": total_LG_overnight, "Mountain Biking": total_LG_mountain_biking, "Spelunking": total_LG_spelunking, "Watersports": total_LG_watersports, "Surfing": total_LG_surfing, "Sea Kayaking": total_LG_sea_kayaking})

    data_info["sheet1_info"] = sheet1_info
    data_info["sheet2_info"] = sheet2_info

    # return data_info


    # read data from Prefs-Sheet 4: "Trip Leader Information"

    df = pd.read_excel(filepath_prefs, sheet_name='Trip Leader Information', index_col=0)

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

    sheet4_prefs.append({"TRiP Leader Name": trip_leader_name, "UFID": leader_ufid, "Semesters Left": semesters_left, "Satisfaction Rating": satisfaction_rating, "Number of trips assigned last semester": trips_last_semester, "Trips Dropped": trips_dropped, "Trips Picked Up": trips_pickedup, "Categories interested in becoming a lead guide": categories_of_interest, "Preferred Leaders to lead with": preferred_leaders})

    preferred_leaders = json.dumps(preferred_leaders)


    # read data from Prefs-Sheet 3: "Prefs Template"

    # df = DataFrame
    df = pd.read_excel(filepath_prefs, sheet_name='Prefs Template', index_col=0, skiprows=1)
    df = df.rename(columns={"Unnamed: 2": "TRiP", "Unnamed: 3": "Preferences"})
    columns_deleted = ['Unnamed: 4', 'Unnamed: 5']
    df.drop(columns_deleted, axis=1, inplace=True)

    new_trip_number = 0
    for index, row in df.iterrows():
        new_trip_number += 1
        # C Column: "TRiP" - Trip Names
        trip_name = row['TRiP']
        # D Column: "Preferences" - Preference Ratings (0-5)
        preference_rating = row['Preferences']


        # print("UFID:", leader_ufid)
        # print("Trip number:", new_trip_number)
        # print("Preference Rating:", preference_rating)


        # create_trip_preference(trip_leader_id, trip_id, preference):
        trip_preference.create_trip_preference(leader_ufid, new_trip_number, preference_rating)

        # print(f"Trip Date: {trip_date}, Trip Name: {trip_name}, Preference Rating: {preference_rating}")     

        sheet3_prefs.append({"Trip Name": trip_name, "Preference Rating": preference_rating})

    # calculate reliability score
    reliability_score = trips_pickedup - trips_dropped

    # def create_leader(ufid, name, class_year, semesters_left, reliability_score, num_trips_assigned, preferred_co_leaders, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role)
    trip_leader.create_leader(leader_ufid, trip_leader_name, leader_class, semesters_left, reliability_score, trips_last_semester, preferred_leaders, category_overnight, category_mountain_biking, category_spelunking, category_watersports, category_surfing, category_sea_kayaking)

    data_prefs["sheet3_prefs"] = sheet3_prefs
    data_prefs["sheet4_prefs"] = sheet4_prefs

    # print(trip.get_all_trips())

    #return data_prefs


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


def run_filter():
    print("running run_filter")

    folder_name = "TRiP Data"
    
    script_directory = os.path.dirname(__file__)

    # Set curr_directory to the parent directory of TRiP Data
    curr_directory = os.path.join(script_directory, folder_name)

    # Check if the folder exists
    if os.path.exists(curr_directory) and os.path.isdir(curr_directory):
        filepath_info = None
        # Find the 'TripsAndLeaderStatusInfo.xlsx' file first
        target_filename = 'TripsAndLeaderStatusInfo.xlsx'
        target_filepath = os.path.join(curr_directory, target_filename)
        if os.path.exists(target_filepath) and os.path.isfile(target_filepath):
            filepath_info = target_filepath
            print(f"Found target file '{target_filename}'")
        else:
            print(f"Target file '{target_filename}' not found")
            
        # Iterate through all files in the folder
        for filename_prefs in os.listdir(curr_directory):
            # Check if it's a file (not a subfolder) and not the target file
            if os.path.isfile(os.path.join(curr_directory, filename_prefs)) and filename_prefs != target_filename:
                filepath_prefs = os.path.join(curr_directory, filename_prefs)
                # Check if filepath_info is set before attempting to read
                if filepath_info:
                    read_TripInfo(filepath_info, filepath_prefs)
                    print("read: ", filename_prefs)
                    print(filepath_prefs)
    else:
        print("The folder is not the directory")


def main():
    # curr_directory = os.path.dirname(__file__) # gets the current directory to add to the relative path

    # # Read in and store the data from 'TripsAndLeaderStatusInfo.xlsx'
    # filename_info = "Example_Data\\TripsAndLeaderStatusInfo.xlsx"
    # filepath_info = os.path.join(curr_directory, filename_info)

    # # Read in and store the data from 'PrefsTemplate.xlsx'
    # filename_prefs = "Example_Data\\Prefs\\JohnPrefs.xlsx"
    # filepath_prefs = os.path.join(curr_directory, filename_prefs)

    # data = read_TripInfo(filepath_info, filepath_prefs)
    # # write_data(data, "Example_Data\\DataInfo.json")


    # UNCOMMENT 'return data_prefs' WHEN RUNNING THE MAIN
    folder_name = "TRiP Data"
    
    script_directory = os.path.dirname(__file__)

    # Set curr_directory to the parent directory of TRiP Data
    curr_directory = os.path.join(script_directory, folder_name)

    # Check if the folder exists
    if os.path.exists(curr_directory) and os.path.isdir(curr_directory):
        # Initialize filepath_info outside the loop
        filepath_info = None
        # Find the 'TripsAndLeaderStatusInfo.xlsx' file first
        target_filename = 'TripsAndLeaderStatusInfo.xlsx'
        target_filepath = os.path.join(curr_directory, target_filename)
        if os.path.exists(target_filepath) and os.path.isfile(target_filepath):
            print(f"Found target file '{target_filename}'")
            filepath_info = target_filepath
        else:
            print(f"Target file '{target_filename}' not found")
            
        # Iterate through all files in the folder
        for filename_prefs in os.listdir(curr_directory):
            # Check if it's a file (not a subfolder) and not the target file
            if os.path.isfile(os.path.join(curr_directory, filename_prefs)) and filename_prefs != target_filename:
                filepath_prefs = os.path.join(curr_directory, filename_prefs)
                # Check if filepath_info is set before attempting to read
                if filepath_info:
                    data = read_TripInfo(filepath_info, filepath_prefs)
                    write_data(data, "test_json")
                    print("read: ", filename_prefs)
    else:
        print("The folder is not the directory")
    
def find_trip_info_folder(upload_path):
    # Check if the upload path exists and is a directory
    if os.path.exists(upload_path) and os.path.isdir(upload_path):
        filepath_info = None
        # Iterate through files in the upload path
        for filename in os.listdir(upload_path):
            filepath = os.path.join(upload_path, filename)
            # Check if the file path includes 'TripsAndLeaderStatusInfo.xlsx'
            if os.path.isfile(filepath) and 'TripsAndLeaderStatusInfo.xlsx' in filepath:
                filepath_info = filepath
                break
        
        # If 'TripsAndLeaderStatusInfo.xlsx' file is found, search for the folder containing it
        if filepath_info:
            for root, dirs, files in os.walk(upload_path):
                for folder in dirs:
                    folder_path = os.path.join(root, folder)
                    if filepath_info.startswith(folder_path):
                        return folder_path
            print("Folder containing 'TripsAndLeaderStatusInfo.xlsx' not found")
        else:
            print("File 'TripsAndLeaderStatusInfo.xlsx' not found in the upload path")

    else:
        print("The upload path is not a directory or does not exist")

# if __name__ == "__main__":
#     main()

# if __name__ == "__main__":
#     run_filter()

if __name__ == "__main__":
     find_trip_info_folder(upload_path)


# TO RUN: python infoFilter.py