from server.controller.diet_controller import create_diet_blueprint

import logging
import os
from flask import Flask

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

import collections
import collections.abc
collections.MutableMapping = collections.abc.MutableMapping

from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)
  
def connect_db(): 
    db_host = os.getenv('DATABASE_HOST', 'localhost')
    db_port = int(os.getenv('DATABASE_PORT', 7017))
    db_name = os.getenv('DATABASE', 'diet')

    try:
        client = MongoClient(
                    host=db_host, 
                    port=db_port, 
                    serverSelectionTimeoutMS=5000
                    )
        client.admin.command('ping') 
        db = client[db_name]
        logging.info(f"✅ Connected to MongoDB at {db_host}:{db_port}, using database '{db_name}'")
        return db, None 
    except ConnectionFailure as e:
        logging.error(f"❌ Could not connect to MongoDB: {e}")
        return None, e
    except OperationFailure as e:
        logging.error(f"❌ Operation failure: {e}")
        return None, e

def create_server(db):
    server = Flask(__name__)
    server.register_blueprint(create_diet_blueprint(db), url_prefix='/diet')
    
    return server

if __name__ == '__main__':
    db, error = connect_db()
    if error:
        exit(1)
    else:
        server = create_server(db)
        server_port = int(os.getenv('SERVER_PORT', 5000))
        server.run(host="0,0,0,0", port=server_port)