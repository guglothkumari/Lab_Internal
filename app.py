from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Register.html')
@app.route('/register', methods=['POST'])
def register():
    name = request.form['username']
    email = request.form['email']
    year = request.form['year']
    return render_template('successful.html', name=name, year=year)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
