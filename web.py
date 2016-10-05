from flask import Flask, render_template 
app = Flask(__name__)

#creates homepage
@app.route('/')
def index():
    return render_template('index.html')

#runs the new instance
app.run(debug=True)



