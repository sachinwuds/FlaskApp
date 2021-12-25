import datetime as dt

# from flask import Flask
from flask import Flask,request, abort, make_response ,render_template         

app = Flask(__name__)



@app.route("/",methods = ['GET'])
def hello_world():
    resp = make_response(f"The Cookie has been set")
    now = dt.datetime.now()
    current_time = now.strftime("%H:%M")
    
    print(current_time)
    resp = make_response(render_template("index.html"))
    resp.set_cookie('CurrentTime',current_time)
    return resp

@app.route("/getcookie",methods = ['GET'])
def get_cookies():
    resp = make_response(f"The Cookie has been set")
    now = dt.datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    resp.set_cookie('CurrentTime',current_time)
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

