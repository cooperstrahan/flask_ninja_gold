from flask import Flask, render_template, redirect, request, session
import random
import datetime

app = Flask(__name__)
app.secret_key = "key"

@app.route('/')
def index():
    if 'total' not in session:
        session['total'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    value = request.form['hidden']
    time = datetime.datetime.now()
    if value == 'Farm':
        num = random.randint(10,20)
        session['total'] += num
    if value == 'Cave':
        num = random.randint(5,10)
        session['total'] += num
    if value == 'House':
        num = random.randint(2,5)
        session['total'] += num
    if value == 'Casino':
        num = random.randint(-50,50)
        session['total'] += num
    if num >= 0:
        session['activities'].insert(0,f"Earned {num} golds from the {value}! ({time})")
    elif num < 0:
        session['activities'].insert(0,f"Lost {num} golds to the {value}... Bummer ({time})")
    print("*" * 50)
    print(session)
    print("*" * 50)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)