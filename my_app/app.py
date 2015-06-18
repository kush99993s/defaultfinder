
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    # data = build_graph.get_data()
    
    # data_html = data.to_html()
    # data_html = data_html.replace('dataframe', 'table table-striped')
    data_html ="hello world"

    return render_template('index.html', data = data_html)

@app.route('/map')
def map():
	return render_template('map.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969, debug=True)