#!/usr/bin/env python

'''A small Python payment server'''

import stripe

from flask import Flask
from flask import request
from flask import json

STRIPE_SECRET_KEY = 'YOUR_TEST_OR_LIVE_SECRET_KEY'

# Creates the app
app = Flask(__name__)

@app.route('/payment', methods=['POST'])
def pay():

    # Sets the stripe api key
    stripe.api_key = STRIPE_SECRET_KEY

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
    except stripe.CardError, e:
        # The card has been declined
        pass

    return "Success!"


if __name__ == '__main__':
    # Set as 0.0.0.0 to be accessible outside your local machine
    app.run(debug=True, host= '0.0.0.0')

