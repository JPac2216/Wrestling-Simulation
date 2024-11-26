from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")

def index():
    data = []
    with open('wwemen.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    #for wrestler in data:
    #   print(f"{wrestler['Superstar']}'s theme song is {wrestler['Theme Song']}.")
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)