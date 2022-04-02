from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<name>')
def index(name):
    param = {}
    param['title'] = name
    return render_template('base.html', **param)


@app.route('/list_prof/<list>')
def prof(list):
    return render_template('index.html', type_list=list)


@app.route('/training/<prof>')
def training(prof):
    return render_template('trainings.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')