# Peanut

A small stripe payment server.

## Get up and running

Peanut consists of a single-file Python server using the lightweight Python REST framework Flask
along with the Stripe Python SDK for creating the payment requests.

First, you’ll need pip, which is a command-line utility for installing python packages. If you don’t have pip installed, you can install it by following the instructions found [here](https://pip.readthedocs.org/en/latest/installing.html#install-pip).

Open a terminal and pip install Flask by entering the following command:

```bash
sudo pip install Flask
```

Next, install the Python Stripe library with the following command:

```bash
sudo pip install --index-url https://code.stripe.com --upgrade stripe
```

Start the peanut server by executing the Python script within a terminal session:

``` bash
python peanut_server.py
```

## Limitations
Peanut is just a simple payment server forwarding payment requests to stripe without storing any credit
card and payments informations, respectively. In a real world app, you’d likely add the customer’s
order, along with the requisite shipping address, product IDs, and other order information, to a
database so the order could be fulfilled properly.

### License

MIT

