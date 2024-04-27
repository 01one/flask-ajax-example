import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample list of existing usernames
existing_usernames = ["user1", "user2", "user3"]


def is_valid_username(username):
    # Double check
    return re.match("^[a-zA-Z0-9_]*$", username) is not None


@app.route('/')
def index():
    return render_template('username-id-generate.html')


@app.route('/check_username', methods=['POST'])
def check_username():
    username = request.form['username']
    if username in existing_usernames:
        return jsonify({'message': 'Username already exists! Please choose a different username.'})
    elif not is_valid_username(username):
        return jsonify({'message': 'Username contains special characters. Only letters, numbers, and underscores are allowed.'})
    else:
        return jsonify({'message': 'Username is available!'})


@app.route('/create_profile', methods=['POST'])
def create_profile():
    username = request.form['username']

    # Add the new username to the list of existing usernames
    existing_usernames.append(username)
    return f"Welcome, {username}! Your profile has been created successfully."


if __name__ == '__main__':
    app.run(debug=True)
