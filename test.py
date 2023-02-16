from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def appConfig(self):
        app.config['TESTING'] = True

    def test_home(self):
        """Ensure the correct information is being used"""

        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertIn('board', session)
            self.assertIn('highScore', session)
            self.assertIn('numGames', session)
            self.assertIn('<h1>BOGGLE GAME</h1>', html)

    def test_submit_word(self):
        """Test the view function for '/submit-word'. Make sure that the correct responses are being used."""

        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = [['T', 'E', 'S', 'T', 'S'], ['T', 'E', 'S', 'T', 'S'], [
                    'T', 'E', 'S', 'T', 'S'], ['T', 'E', 'S', 'T', 'S'], ['T', 'E', 'S', 'T', 'S']]
        resp1 = client.get('/submit-word?guess=test')
        self.assertEqual(resp1.json['result'], 'ok')
        resp2 = client.get('/submit-word?guess=not')
        self.assertEqual(resp2.json['result'], 'not-on-board')
        resp3 = client.get('/submit-word?guess=fsdgk')
        self.assertEqual(resp3.json['result'], 'not-word')

    def test_update_stats(self):
        """Test the view function for '/update-stats'. Make sure that the correct response is being used."""
        with app.test_client() as client:
            client.get('/')
            with client.session_transaction() as change_session:
                change_session['highScore'] = 50
                change_session['numGames'] = 99

        resp = client.post('/update-stats', json={'score': 100})
        self.assertEqual(resp.json['highscore'], 100)
        self.assertEqual(resp.json['numgames'], 100)
