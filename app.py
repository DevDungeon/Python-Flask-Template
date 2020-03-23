from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



if __name__ == '__main__':
    load_dotenv()
    app.run(ssl_context='adhoc', port=9999, host='localhost', debug=True)
