
import connexion

app = connexion.App(__name__, specification_dir="./")

@app.route("/ping")
def ping():
	return "pong"
