from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')
    # return 'Hello, Yana!'

@app.route('/success/<name>')
def success(name):
    return render_template("present.html", value=name)
 
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0')