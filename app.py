# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/visualizations')
def visualizations(): 
    return render_template('visualizations.html')

@app.route('/global_temp_data')
def global_temp_data(): 
    return render_template('global_temp_data.html')

@app.route('/CO2_data')
def CO2_data(): 
    return render_template('CO2_data.html')

if __name__ == "__main__":
    app.run(debug=True)