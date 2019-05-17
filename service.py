from flask import Flask, session, url_for, redirect, render_template, request, abort, flash, jsonify, Response
from flask_restful import Api
from search_store_resource import SearchStoreResource
import os

app = Flask(__name__)
api = Api(app)
api.add_resource(SearchStoreResource, '/search')

@app.route("/", methods=['GET'])
def root():
    return render_template("index.html", runtime=os.environ['RUNTIME'])

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return redirect('/', code=302)

