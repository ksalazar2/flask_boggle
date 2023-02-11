from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session, jsonify
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'plswork'
# debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def display_board():
    """Display game board."""

    board = boggle_game.make_board()
    session['board'] = board

    return render_template('base.html', game_board = board)

@app.route('/submit-word')
def handle_guess():
    """Handle guess submitted by user."""

    user_guess = request.args['guess']
    board = session['board']
    print(user_guess)
    print(board)
    resp = boggle_game.check_valid_word(board, user_guess)
    print(resp)
    return jsonify({'result': resp})