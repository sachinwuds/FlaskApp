import datetime as dt

# from pymongo import mongo_client
from flask_pymongo import PyMongo
# from flask import Flask
from flask import Flask,request, abort, make_response ,render_template         

app = Flask(__name__)
#make sure you are not using your login credentials
#Create one user and use that user name and password here
app.config["MONGO_URI"] = "mongodb+srv://USERNAME:PASSSWORD@firstclustor.uskjt.mongodb.net/firstdb?retryWrites=true&w=majority"
mongo = PyMongo(app)
# print(mongo.db)

# collections = mongo.db.list_collection_names()
# for collection in collections:
#    print(collection)
# print(mongo.db.)

#Here is profile is collection in the firstdb database
db_operations = mongo.db.profile



@app.route("/",methods = ['GET']) 
def hello_world():
    now = dt.datetime.now()
    current_time = now.strftime("%H:%M")    
    resp = make_response(render_template("index.html"))
    resp.set_cookie('CurrentTime',current_time)
    return resp

@app.route("/getcookie",methods = ['GET'])
def get_cookies():
    # new_user = {'Name' : 'xyz', 'Age' : 20}
    # db_operations.insert_one(new_user)
    return render_template("availability.html")  



@app.route("/checkavailability",methods = ['POST'])
def Isitemavailable():
    current_time = request.cookies.get('CurrentTime')
    timestring = request.form['timestring']
    itemname = request.form['itemname']
    time_list = timestring.split(',')
    current_time = dt.datetime.strptime(current_time, '%H:%M').time()
    is_available = False
    for i in time_list:
        time = i.split('-')
        if time[0] <= time[1] and not is_available:
            starttime = dt.datetime.strptime(time[0], '%H:%M').time()
            endtime = dt.datetime.strptime(time[1], '%H:%M').time()
            is_available = starttime <= current_time <= endtime

    if is_available:
        return "<p>{0} available</p>".format(itemname)
    else:
        return "<p>{0} is not available</p>".format(itemname)


# load_dotenv()
# MONGODB_URI = os.environ['MONGODB_URI']

# client = MongoClient(MONGODB_URI)
# db = client.test
# for db_info in client.list_database_names():
#    print(db_info)