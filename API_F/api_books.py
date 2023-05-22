import flask
from flask import request, jsonify

# Creates the Flask application object, which contains data about the application
app = flask.Flask(__name__)
# error in app if code is malformed
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'favorite_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'favorite': 'With a clamor of bells that set the swallows soaring.',
     'year_published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'favorite_sentence': 'to wound the autumnal city.',
     'year_published': '1975'}
]


# GET - sends data from the application to the user.
# POST - receives data from a user.
# The process of mapping URLs to functions is called routing.
@app.route('/', methods=['GET'])
def home():
    return "<h1>Philosophy Books</h1><p>This site is a prototype API. </p>"


# A route to return all available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    # convert lists and dictionaries to JSON format
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # the id must be provided like this: ?id=0 called query parameters
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # takes the list of results and renders them in the browser as JSON.
    return jsonify(results)


# method of the application object
app.run()
