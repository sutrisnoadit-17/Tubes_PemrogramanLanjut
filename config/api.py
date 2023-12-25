import requests
from datetime import datetime

endPointCities = "https://raw.githubusercontent.com/sutrisnoadit-17/api-jadwal-sholat-tubes-proglan/main/kota.json"
endPointSchedule = "https://raw.githubusercontent.com/sutrisnoadit-17/api-jadwal-sholat-tubes-proglan/main/jadwal/"
def dateSeparated():
    tmpDate = str(datetime.now().date())
    return {"year":tmpDate[0:4], "month" : tmpDate[5:7],"day" : tmpDate[8:10]}
def testConnection():
    try:
        requests.get('https://github.com/',timeout=00.2)
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
            print("API request successful")
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
    url = endPointSchedule+f"{argArea}/{dateSeparated()['year']}/{dateSeparated()['month']}.json"
    try:
        response = requests.get(url)
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
def getDaily(argArea):
    return getScheduleAll(argArea)[int(dateSeparated()['day']) - 1]
if __name__ == '__main__':
    print(getDaily("malang"))
