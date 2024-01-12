 
# Import necessary libraries
from flask import Flask, render_template, request
import sqlite3

# Create a Flask app
app = Flask(__name__)

# Define the database connection
conn = sqlite3.connect('facebook.db')
c = conn.cursor()

# Define the main route
@app.route('/')
def index():
    # Render the index.html file
    return render_template('index.html')

# Define the profile route
@app.route('/profile')
def profile():
    # Get the user's profile information from the database
    user_id = request.args.get('user_id')
    profile_info = c.execute('SELECT * FROM users WHERE user_id=?', (user_id,)).fetchone()

    # Render the profile.html file and pass the profile information
    return render_template('profile.html', profile_info=profile_info)

# Define the friends route
@app.route('/friends')
def friends():
    # Get the user's friends list from the database
    user_id = request.args.get('user_id')
    friends_list = c.execute('SELECT * FROM friends WHERE user_id=?', (user_id,)).fetchall()

    # Render the friends.html file and pass the friends list
    return render_template('friends.html', friends_list=friends_list)

# Run the app
if __name__ == '__main__':
    app.run()
