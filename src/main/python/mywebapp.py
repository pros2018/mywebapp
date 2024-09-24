from flask import Flask, jsonify, request

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    return 'Hello, welcome to my simple web application'

# Define a route for a JSON response
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'This is some sample data'}
    return jsonify(data)

# Define a route for handling errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Define a route for handling POST requests
@app.route('/api/data', methods=['POST'])
def post_data():
    if not request.json or 'name' not in request.json:
        return jsonify({'error': 'Bad Request'}), 400
    name = request.json['name']
    return jsonify({'message': f'Hello, {name}!'}), 201

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=7002)
