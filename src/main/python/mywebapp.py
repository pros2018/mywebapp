from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    return 'Hello, welcome to my simple web application'

# Run the application
if __name__ == '__main__':
    app.run(debug=True,port='7001')
