"""
Required Environment Values :

1. ssm_url (in config_generator.py) : VPC Endpoint for SSM
2. RUNTIME (in controller.py) : 0 or 1 . 1 -> On Service

"""

from controller import app
from flask_bootstrap import Bootstrap


# def before_request():
#     app.jinja_env.cache = {}


if __name__ == '__main__':
    Bootstrap(app)
    # app.before_request(before_request)
    app.run(debug=True, host='0.0.0.0', port=80)
