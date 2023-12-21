import requests
def testConnection():
    try:
        requests.get('http://www.google.com',timeout=00.2)
    except requests.exceptions.RequestException as e:
        return False 
    except Exception as e:
        return False
    else:
        print("?")
        return True