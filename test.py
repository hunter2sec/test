from flask import Flask
import os

PORT = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
app.config.from_object(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
