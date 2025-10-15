      
def test_crud(client):
    input = {
                "date" : "12-10-2025",
                "time" : "12:30",
                "meal" : {
                        "items" : [
                                   { "food" : "rice", "amount" : 50,  "unit" : "gr", "calories": 150 },
                                   { "food" : "egg", "amount" : 2, "unit" : "un", "calories": 160 },
                                   { "food" : "potato", "amount" : 150, "unit" : "gr", "calories": 100 }
                        ]
                    }
            }
    
    #Testing add Diet
    response_post = client.post("/diet", json=input, follow_redirects=True)
    assert response_post.status_code == 201
    id_generated = response_post.data.decode()
    assert id_generated

    #Testing get Diet to check add
    response_get = client.get("/diet", json={"id": id_generated}, follow_redirects=True)
    assert response_get.status_code == 200
    data = response_get.get_json()
    assert data["date"] == "12-10-2025"
    assert data["meal"]["items"][0]["food"] == "rice"
    
    #Testing update Diet
    input["id"] = id_generated
    input["meal"]["items"][0]["food"] = "bean"
    input["meal"]["items"][1]["food"] = "chicken"
    input["meal"]["items"][1]["unit"] = "gr"
    
    response_put = client.put("/diet", json=input, follow_redirects=True)
    assert response_put.status_code == 200
    id_updated = response_put.get_json()["id"]

    #Testing get Diet to check update
    response_get = client.get("/diet", json={"id": id_updated}, follow_redirects=True)
    assert response_get.status_code == 200
    data = response_get.get_json()
    assert data["meal"]["items"][0]["food"] == "bean"
    assert data["meal"]["items"][1]["food"] == "chicken"
    assert data["meal"]["items"][1]["unit"] == "gr"
    
    #Testing delete Diet
    response_delete = client.delete("/diet", json={"id": id_updated}, follow_redirects=True)
    assert response_delete.status_code == 200
    count = response_delete.data.decode()
    assert int(count) == 1
    
    #Testing get Diet to check delete
    response_get = client.get("/diet", json={"id": id_updated}, follow_redirects=True)
    assert response_get.status_code == 200
    data = response_get.data.decode()
    assert data == "Diet not found"