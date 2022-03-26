from operator import index
from flask import Flask, render_template, request, redirect, session   # added render_template!
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def display():
     return render_template('index.html')

@app.route("/result",methods=["POST"])
def result():
    print("Got Post Info")
    print(request.form)
    name = request.form['yourname']
    location = request.form['location']
    fav=request.form['fav']
    free =request.form['free']
    return render_template('show.html', name=name, location=location,fav=fav,free=free)



# @app.route("/result")
# def show_user():
#     print("Showing the User Info From the Form")
#     print(request.form)
#     return render_template('show.html', name_on_template=session['name'], location_on_template=session['location'],fav_on_template=session['fav'],free_on_template=session['free'])


if __name__=="__main__":
    app.run(debug=True)