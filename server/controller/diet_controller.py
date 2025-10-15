from flask import Blueprint, request
from server.service.diet_service import DietService

def create_diet_blueprint(db):
    diet_blueprint = Blueprint('diet', __name__)
    diet_service = DietService(db)

    @diet_blueprint.route("/", methods=["POST"])
    def add():
        result, err = diet_service.add(request.get_json())
        return response(201, result, err)
 
    @diet_blueprint.route("/all", methods=["GET"])
    def get_all():
        result, err = diet_service.get_all()
        return response(200, result, err)
    
    @diet_blueprint.route("/", methods=["GET"])
    def get():
        id = request.get_json()["id"]
        result, err = diet_service.get(id)
        return response(200, result, err)
    
    @diet_blueprint.route("/", methods=["PUT"])
    def update():
        id = request.get_json()["id"]
        result, err = diet_service.update(id, request.get_json())
        return response(200, result, err)
    
    @diet_blueprint.route("/", methods=["DELETE"])
    def delete():
        id = request.get_json()["id"]
        result, err = diet_service.delete(id)
        return response(200, result, err)
       
    def response(status_success, result, err):
        if not err:
           return result, status_success
        else:
           return err, 400
    
    return diet_blueprint