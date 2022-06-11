from routes import app

app.add_api("swagger.yml")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)