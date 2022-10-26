"""
guestbook
"""
import os
import logging
from flask import Flask, redirect, request, url_for

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

signatures = []

app = Flask(__name__)

# configs
font = os.environ['FONT']
font_color = os.environ['COLOR']
environment = os.environ['ENV']
version = os.environ['VER']

@app.route('/', methods=['GET'])
def index():
    """
    create index
    """
    html = """
        Signatures: <br />
        <font face="%(font)s" color="%(color)s">
            %(message)s
        </font>

        <br /><br />
        <form action="/signatures" method="post">
            Sign the Guestbook: <input type="text" name="message"><br />
            <input type="submit" value="Sign">
        </form>

        <br /><br />
        Debug Info: <br />
        ENVIRONMENT is %(environment)s
        <br /><br />
        Version: %(version)s
    """

    messages_html = "<br />".join(signatures)
    return html % {"font": font, "color": font_color, "message": messages_html, "environment": environment, "version": version}

@app.route('/signatures', methods=['POST'])
def write():
    """
    write post
    """
    message = request.form.get('message')
    signatures.append(message)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
