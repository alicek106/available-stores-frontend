from flask import Flask, render_template, redirect
from flask_restful import Api
from modules.search_store_resource import SearchStoreResource
import os
from modules.send_message_resource import SendMessageResource

app = Flask(__name__)
api = Api(app)
api.add_resource(SearchStoreResource, '/search')
api.add_resource(SendMessageResource, '/report')

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/', code=302)

@app.route("/", methods=['GET'])
def root():
    return render_template("index.html", runtime=os.environ['RUNTIME'])

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return redirect('/', code=302)
