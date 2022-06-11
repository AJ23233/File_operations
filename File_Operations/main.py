# Filename: main.py
# Description: This file is responsible for starting application from routes
# Author: Ajay Vanara

from routes import app

app.add_api("swagger.yml")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)