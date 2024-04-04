from flask import Flask, make_response, redirect, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        resp = make_response(redirect('/welcome'))
        resp.set_cookie('name', name)
        resp.set_cookie('email', email)
        return resp
    else:
        return render_template('form.html')

@app.route('/welcome')
def welcome():
    name = request.cookies.get('name')
    return render_template('welcome.html', name=name)

@app.route('/logout', methods=['POST'])
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('name')
    resp.delete_cookie('email')
    return resp

if __name__ == "__main__":
    app.run(debug=True)