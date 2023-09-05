from website import create_app
from flask import Flask, session
from flask_session import Session

SESSION_TYPE = 'memcache'
sess = Session()
app= create_app()

if __name__=='__main__':
    # Quick test configuration. Please use proper Flask configuration options
    # in production settings, and use a separate file or environment variables
    # to manage the secret key!
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)
    app.run(debug=True)
