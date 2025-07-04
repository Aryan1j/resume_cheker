from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form.get('name')
    score = request.form.get('score')

 
    if not name or not score:
        flash("Both fields are required!", "error")
        return redirect(url_for('index'))

    try:
        score = int(score)
    except ValueError:
        flash("Score must be a number!", "error")
        return redirect(url_for('index'))


    result = "Likely to get Interview" if score >= 80 else "Needs Improvement"

  
    session['name'] = name
    session['result'] = result

    return redirect(url_for('result'))

@app.route('/result')
def result():
    return render_template('result.html', name=session.get('name'), result=session.get('result'))

if __name__ == '__main__':
    app.run(debug=True)
