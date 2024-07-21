import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("./swagger/swagger.yml")

@app.route('/')
def welcome():
    return "<h1>Welcome to the new Employee Records database</h1>"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port =8000)