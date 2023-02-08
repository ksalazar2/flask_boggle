from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'plswork'

boggle_game = Boggle()

@app.route('/')
def display_board():
    """Display game board."""

    board = boggle_game.make_board()
    session['board'] = board

    return render_template('base.html', game_board = board)