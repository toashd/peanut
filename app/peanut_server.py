#!/usr/bin/env python

'''A small Python payment server'''

import os
import stripe

from util import requires_ssl

from flask import Flask
from flask import request
from flask import json

# from OpenSSL import SSL

VERSION = '0.1.0'

# Creates the app
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/', methods=['GET'])
def index():
    ''' Index page '''
    return 'Peanut - A small Python payment server'

@app.route('/version', methods=['GET'])
def version():
    ''' Prints the version '''
    return 'Peanut version %s' % VERSION

@app.route('/payment', methods=['POST'])
@requires_ssl
def pay():

    # Sets the stripe api key
    stripe.api_key = app.config['STRIPE_SECRET_KEY']

    # Parses the request as JSON
    json = request.get_json(force=True)

    # Fetches the credit card details
    token       = json['stripeToken']
    amount      = json['amount']
    currency    = json['currency']
    description = json['description']

    # Creates the charge on Stripe
    # This will charge the user's card
    try:
        charge = stripe.Charge.create(
                    amount=amount,
                    currency=currency,
                    card=token,
                    description=description
                  )
    except stripe.CardError as e:
        # The card has been declined
        pass

    return "Success!"

if __name__ == '__main__':
    # Set as 0.0.0.0 to be accessible outside your local machine
    app.run(debug=app.config['DEBUG'], host='0.0.0.0')

