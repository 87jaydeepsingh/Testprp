from flask import Flask, render_template, request
import pymongo
client = pymongo.MongoClient(
    "mongodb+srv://saud:mlab3431@hospitals.5loco.mongodb.net/helpagainstcovid?retryWrites=true&w=majority")

mydatabase = client.helpagainstcovid
collection = mydatabase.botdata


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    print("Hello World")
    print("Hello Python")
    return render_template('home.html')


@app.route('/get')
def get_bot_response():
    message = request.args.get('msg')
    if collection.find_one({'"questions"': message}):
        ans = collection.find_one({'"questions"': message})
        #print('Question',message,' Answer',ans)
        resp = ans['"answer"']
        return str("<div id='a'>"+message+"<br></div><div id='b'>"+resp+"</div>")
    else:
        return "<br><div id='a'>"+message+"<br></div><div id='b'>Enter Valid Question<br></div><br>"

if __name__ == '__main__':
    app.run(debug=True)
