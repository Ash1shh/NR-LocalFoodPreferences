import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__,template_folder='template')
import csv
# from pymongo import MongoClient

# mongoClient = MongoClient() 
# db = mongoClient.flask_db
# #recipes=db.recipes    
# db.segment.drop()

# header = [ "name", "id", "minutes","contributor_id","submitted","tags","nutrition","n_steps","steps","description","ingredients","n_ingredients","food type","cal"]
# csvfile = open('RAW_recipes.csv', 'r')
# reader = csv.DictReader( csvfile )

# for each in reader:
#     row={}
#     for field in header:
#         row[field]=each[field]
        
#     #print (row)
#     db.segment.insert_one(row)
# segment=db.segment
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/dem')
def dem():
    return render_template('dem.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/menu')
def menu():
    return render_template('menu.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/signin')
def signin():
    return render_template('signin.html')
@app.route('/predict',methods=['POST','GET'])
def predict():
    recipe=pd.read_csv('RAW_recipes.csv')
    df=pd.DataFrame(recipe)

    food=request.form['foodType']
    mint=request.form['Mintime']
    maxt=request.form['Maxtime']
    mcal=request.form['mincal']
    macal=request.form['maxcal']
    cit=request.form['city1']
    mint=int(mint)
    maxt=int(maxt)
    mcal=int(mcal)
    macal=int(macal)
    nam=[]
    mins=[]
    calor=[]
    setp=[]
    des=[]
    ind=[]
    for i in df.index:
        if(df['food type'][i]==food and df['city'][i]==cit and mint<df['minutes'][i]<maxt and mcal<float(df['cal'][i])<macal):
            nam.append(df['name'][i])
            mins.append(df['minutes'][i])
            calor.append(df['cal'][i])
            setp.append(df['steps'][i])
            des.append(df['description'][i])
            ind.append(df['ingredients'][i])
        

    list_of_tuples = list(zip(nam, mins,calor,setp,des,ind)) 
    df3 = pd.DataFrame(list_of_tuples, columns = ['Name', 'Minutes','Calories','Steps','Description','Ingridients']) 
    return render_template('output.html',  tables=[df3.sample(n=3).to_html(classes='table-striped')], titles=df3.columns.values)

if __name__ == "__main__":
    app.run(debug=True)

