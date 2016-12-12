from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")

@application.route('/index')
def index():
    return render_template('index.html')

@application.route('/history')
def history():
    median_4bedroom_plot = open('./static/img/median_4bedroom.html', 'r').read()
    median_4bedroom_normalized_plot = open('./static/img/median_4bedroom_normalized.html', 'r').read()
    return render_template('history.html',
                           median_4bedroom_plot=median_4bedroom_plot,
                           median_4bedroom_normalized_plot=median_4bedroom_normalized_plot)
@application.route('/price')
def price():
    return render_template('price.html')

if __name__ == '__main__':
    application.run()
