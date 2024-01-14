from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/index')
def index():
    return render_template('index.html', name='PyCharm')


@app.route('/form')
def show_form():
    # Render the initial form
    return render_template('form.html')


@app.route('/result', methods=['GET', 'POST'])
def result_form():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Render a new HTML page with the submitted data
        return render_template('result.html', name=name, email=email, message=message)


if __name__ == '__main__':
    app.run()
