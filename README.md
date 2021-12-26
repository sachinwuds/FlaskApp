# FlaskApp
Hello Forks 
Here is the flask app to check the availability for an item in perticular time.

here is the parameter for check the status.
itemname = 'Dosa' #Item name for which we have to check availability
timestring =  "00:00-11:00,10:45-18:00,10:45-20:00" #diffrent time intervals ,The Item is only available in these time intervals.

#MongoDB database
we are using mongoDB database to store data . We have multiple options to connect but we are using
cloud mongoDB.


please feel free to contribute

client = pymongo.MongoClient("mongodb+srv://sachin:<password>@firstclustor.uskjt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
