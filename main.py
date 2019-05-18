"""
Required Environment Values :
All values processed as String in Python Source Code.

1. ssm_url (in config_generator.py) : VPC Endpoint for SSM
2. RUNTIME (in controller.py) : 0 or 1 . 1 -> On Service
3. local

"""

from controller import app
from flask_bootstrap import Bootstrap

if __name__ == '__main__':
    Bootstrap(app)
    app.run(debug=True, host='0.0.0.0', port=80)
