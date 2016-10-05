from flask import Flask, render_template 
app = Flask(__name__)

#creates homepage
@app.route('/')
def index():
    return render_template('index.html')

#create about page
@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)


