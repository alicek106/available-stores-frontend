from flask import Flask, render_template
from flask_restful import Api
from modules.search_store_resource import SearchStoreResource
import os

app = Flask(__name__)
api = Api(app)
api.add_resource(SearchStoreResource, '/search')


@app.route("/", methods=['GET'])
def root():
    return render_template("index.html", runtime=os.environ['RUNTIME'], version=os.environ['version'])

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return redirect('/', code=302)
