import json
import os

def load_json_file():
    folder_name=input('Enter folder name where JSON file is located: ')
    file_name= 'sasank_adoptions.json'
    file_path='C:/Users/sasan/OneDrive/Desktop/python/Files-assignment/sasank_adoptions.json'
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print('file loaded succesfully')
        return data    
    except FileNotFoundError as fnf_error:
        print(f'file{file_path} not found')
    except json.JSONDecodeError as json_error:
        print(f"Error decoding JSON: {json_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
data = load_json_file()