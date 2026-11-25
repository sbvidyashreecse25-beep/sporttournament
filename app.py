from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        return "Registration Successful"

    return "Sport Tournament Registration"

if __name__ == '__main__':
    app.run(debug=True)