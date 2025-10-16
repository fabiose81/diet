import pytest
from pymongo import MongoClient
from testcontainers.mongodb import MongoDbContainer
from server.app import create_server

@pytest.fixture(scope="session")
def mongo_container():
    with MongoDbContainer("mongo:7.0") as mongo:
        uri = mongo.get_connection_url()
        yield uri
        client = MongoClient(uri)
        client.drop_database("diet")
        client.close()
        
@pytest.fixture(scope="session")
def server(mongo_container):
    client_db = MongoClient(mongo_container).mydb
    app = create_server(db=client_db)
    app.config["TESTING"] = True
    return app
    
@pytest.fixture
def client(server):
    with server.test_client() as client:
        yield client
        
@pytest.fixture(scope="session", autouse=True)
def cleanup_after_tests(request):
    def fin():
        if request.session.testsfailed == 0:
            print("✅ All tests passed — cleaning MongoDB data")

    request.addfinalizer(fin)