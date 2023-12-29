import requests
from datetime import datetime
import pandas as pd
from tkinter import messagebox 

endPointCities = "https://raw.githubusercontent.com/sutrisnoadit-17/api-jadwal-sholat-tubes-proglan/main/kota.json"
endPointSchedule = "https://raw.githubusercontent.com/sutrisnoadit-17/api-jadwal-sholat-tubes-proglan/main/jadwal/"
check = False
def msgBox(argMsg):
    messagebox.showwarning("Error",argMsg)
    return None
def dateSeparated():
    tmpDate = str(datetime.now().date())
    return {"year":tmpDate[0:4], "month" : tmpDate[5:7],"day" : tmpDate[8:10]}

def testConnection():
    try:
        requests.get('https://github.com/')
    except requests.exceptions.RequestException as e:
        return False 
    except Exception as e:
        return False
    else:
        print("?")
        return True

def getCities():
    try:
        response = requests.get(endPointCities)
        if response.status_code == 200:
            return response.json()  
        else:
            print(f"API request failed with status code {response.status_code}")
            return None
    except requests.ConnectionError:
        print("Failed to establish a connection to the API")
        return None
    except requests.Timeout:
        print("Request to the API timed out")
        return None
    except requests.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return None
    
def getScheduleAll(argArea):
    try:
        url = endPointSchedule+f"{argArea}/{dateSeparated()['year']}/{dateSeparated()['month']}.json"
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            importToCsv(url)
            return response.json()  
        if response.status_code == 404:
            msgBox("Daerah Tidak Ditemukan")
            return False
        else:
            print(f"API request failed with status code {response.status_code}")
            return None
    except requests.ConnectionError:
        print("Failed to establish a connection to the API")
        return None
    except requests.Timeout:
        print("Request to the API timed out")
        return None
    except requests.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return None
    
def getDaily(argArea):
    resp = getScheduleAll(argArea)[int(dateSeparated()['day']) - 1]
    if resp is not False:
        return resp
    else:
        return False

def importToCsv(argJson):
    path = 'file/prev.csv'
    df = pd.read_json(argJson)
    try:
        df.to_csv(path, index=True)
    except pd.errors.EmptyDataError:
        print(f"Error: JSON file  is empty.")
    except pd.errors.JSONDecodeError:
        print(f"Error: Unable to decode JSON file at. Make sure the JSON is valid.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def toArr(csv_file_path):
    try:
        df = pd.read_csv(csv_file_path)
        array_data = df.values.tolist()
        return array_data
    except pd.errors.EmptyDataError:
        print(f" file at {csv_file_path} is empty.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# if __name__ == '__main__':
#     print(getScheduleAll("malaSSSng"))
