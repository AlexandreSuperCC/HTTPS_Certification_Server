# -*- coding: utf-8 -*-
"""

Created on Wed May  6 12:46:22 2020
@author: Mr ABBAS-TURKI

Modified on April 2021
@author: Mr Perronnet

"""

from flask import Flask, render_template

# définir le message secret
SECRET_MESSAGE = "Hello world" # A modifier

RESOURCES_DIR = "resources/"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"

app = Flask(__name__)

@app.route("/")
def get_secret_message():
    return render_template('index.html',secret_message=SECRET_MESSAGE) 

if __name__ == "__main__":
    # HTTP version
    #app.run(debug=True, host="127.0.0.1", port=8081)
    # HTTPS version; Il faut que l'on utilise le terminal ici(tapez: py run_server.py)
    context = (SERVER_PUBLIC_KEY_FILENAME,SERVER_PRIVATE_KEY_FILENAME)
    app.run(debug=True, host="127.0.0.1", port=8081, ssl_context=context)
    # A compléter
