import unittest
import requests

class testApi(unittest.TestCase):
    def testEndpointCities(self):
        url = "https://raw.githubusercontent.com/sutrisnoadit-17/api-jadwal-sholat-tubes-proglan/main/kota.json"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'text/plain; charset=utf-8')
        self.assertIsInstance(response.json(), list)
        
    def testEndpointCities(self):
        url = "https://raw.githubusercontent.com/sutrisnoadit-17/api-jadwal-sholat-tubes-proglan/main/kota.json"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'text/plain; charset=utf-8')
        self.assertIsInstance(response.json(), list)
            
if __name__ == '__main__':
    unittest.main()