import requests
import time
from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_data():
	
	print(requests.get('http://cloudcomputingapp.azurewebsites.net/').content)

if __name__ == "__main__":
	for i in range(100):
		start_time = time.time()
		get_data()
		print("time taken: ", time.time()-start_time)