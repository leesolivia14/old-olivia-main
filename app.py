from flask import Flask, render_template, request

from college_rec_draft_2am import *

api_key = 'unwIttz59iNAXrLsiHSwV0n3Wrb8hKR0nm4TMq2D'
# creating an instance of Flask class
# needed so that Flask knows where to look for resources such as templates and static files
app = Flask(__name__)

# route() decorator to tell Flask what URL should trigger our function
@app.route("/", methods = ['GET', 'POST'])
# function returns message we want to display in the user's browser
def index_page():
    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':
        global data
        global location
        global budget
        global satread
        global satmath
        global act

        satread = 0
        satmath = 0
        act = 0



        data = request.form
        try:
            location = int(data.getlist('location')[0])
        except:
            location = 0
        
        try:
            budget = int(data.getlist('budget')[0])
        except:
            budget = 0
        
        try:
            satread = int(data.getlist('SATread')[0])
        except:
            satread = 0

        try:
            satmath = int(data.getlist('SATmath')[0])
        except:
            satmath = 0

        try:
            act = int(data.getlist('ACT')[0])
        except:
            act = 0

        size = data.getlist('size')

        #print(data.getlist('location'))
        print(location, budget, satread, satmath, act, size)
        
        global topfive
        topfive = getColleges(location, budget, satread, satmath, act)

        print("finished generating top 5 colleges")
        #print(topfive)

        return render_template("collage.html", first_name=topfive[0]['name'],
                                                first_state=topfive[0]['state'],
                                                first_appfee=topfive[0]['appfee'],
                                                first_roomboard=topfive[0]['roomboard'],

                                                second_name=topfive[1]['name'],
                                                second_state=topfive[1]['state'],
                                                second_appfee=topfive[1]['appfee'],
                                                second_roomboard=topfive[1]['roomboard'],
                                                    
                                                third_name=topfive[2]['name'],
                                                third_state=topfive[2]['state'],
                                                third_appfee=topfive[2]['appfee'],
                                                third_roomboard=topfive[2]['roomboard'],

                                                fourth_name=topfive[3]['name'],
                                                fourth_state=topfive[3]['state'],
                                                fourth_appfee=topfive[3]['appfee'],
                                                fourth_roomboard=topfive[3]['roomboard'],

                                                fifth_name=topfive[4]['name'],
                                                fifth_state=topfive[4]['state'],
                                                fifth_appfee=topfive[4]['appfee'],
                                                fifth_roomboard=topfive[4]['roomboard'])
                                                




@app.route("/collage", methods = ['GET', 'POST'])
def collage_page():
    if request.method == 'GET':
        return render_template("collage.html")

    if request.method == 'POST':
        
        
        return render_template("collage.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
