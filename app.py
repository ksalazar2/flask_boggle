from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'plswork'

boggle_game = Boggle()
