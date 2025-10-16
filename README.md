## Description
    Python server to persiste diet information into mongodb.
    CRUD teste with Testcontainer by Pytest.
    GitAction pipeline to push server and database image to AWS ECR and create stack to CloudFormation.

![alt text](https://github.com/fabiose81/diet/blob/master/diet.jpg?raw=true)

### For Python server and Docker container
    In python folder create a file .env and insert:

    SERVER_PORT=5000
    DATABASE_HOST=travel_database #localhost
    DATABASE_PORT=27017  #7018

    SERVER_CONTAINER_NAME=diet_server
    SERVER_CONTAINER_PORT=5000:5000

    DATABASE_IMAGE=mongo:latest
    DATABASE_CONTAINER_NAME=diet_database
    DATABASE_CONTAINER_PORT=7018:27017
    DATABASE=diet

### For Postman test

#### AddDiet

    {
        "date" : "12-10-2024",
        "time" : "12:30",
        "meal" : {
            "items" : [
              {
              	"food" : "rice",
			    "amount" : 50,
			    "unit" : "gr",
			    "calories": 150
              },
              {
              	"food" : "egg",
			    "amount" : 2,
			    "unit" : "un",
			    "calories": 160
              },
              {
              	"food" : "potato",
			    "amount" : 150,
			    "unit" : "gr",
			    "calories": 100
              }
            ]          
        }
    }

#### GetDiet

    {
        "id": "68dff00df541bc68d78e785f"
    }

#### UpdateDiet

    Same json structure but it must to add the id key

    {
        "id" : "68dff00df541bc68d78e785f"
        "date" : "12-10-2024",
        "time" : "12:30",
        "meal" : {
            "items" : [
              {
              	"food" : "bean",
			    "amount" : 50,
			    "unit" : "gr",
			    "calories": 150
              }
              ...
            ]          
        }
    }

#### DeleteDiet

    {
        "id": "68dff00df541bc68d78e785f"
    }


  
