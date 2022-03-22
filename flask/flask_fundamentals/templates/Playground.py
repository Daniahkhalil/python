from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/play')                           
def play():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template("index.html",_num=3)  

@app.route('/play/<num>')                           
def play_num_color(num):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template("index.html", _num=int(num))  
@app.route('/play/<num>/<color>')                           
def play_num(num,color):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template("index.html", _num=int(num),_color=color)  
if __name__=="__main__":
    app.run(debug=True) 