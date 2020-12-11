from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('layout.html')

@app.route('/carrier objective')
def carrier_ojective():
    return render_template('carrier objective.html')

@app.route('/education')
def education():
        return render_template('education.html')

@app.route('/certifications')
def certifications():
        return render_template('certifications.html')

@app.route('/accomplishments')
def accomplishments():
        return render_template('accomplishments.html')

@app.route('/skills')
def skills():
        return render_template('skills.html')

@app.route('/contact')
def contact():
            return render_template('contact.html')

if(__name__=='__main__'):
    app.run(debug=True)
