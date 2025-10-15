import logging
from typing import Union, Dict, Any
from server.dao.models import Diet, Meal, MealItem
from server.dao.diet_dao import DietDAO

logging.basicConfig(level=logging.INFO)

class DietService:
    def __init__(self, db):
        self.diet_dao = DietDAO(db)
        
    def _ensure_diet_obj(self, data: Union[Dict[str, Any], Diet]) -> Diet:
        if isinstance(data, Diet):
            return data

        meal_dict = data.get("meal", {})
        items = []
        for it in meal_dict.get("items", []):
            items.append(
                MealItem(
                    food=str(it.get("food", "")),
                    amount=int(it.get("amount", 0)),
                    unit=str(it.get("unit", "")),
                    calories=int(it.get("calories", 0)),
                )
            )

        meal = Meal(items)
        diet = Diet(date=str(data.get("date", "")), time=str(data.get("time", "")), meal=meal)
        return diet

    def add(self, diet_input: Union[Dict[str, Any], Diet]):
        try:
            diet = self._ensure_diet_obj(diet_input)
            doc = diet.to_dict() 
            inserted_id = self.diet_dao.add(doc)
            logging.info(f"✅ Inserted document with ID: {inserted_id}")
            return inserted_id, None
        except Exception as e:
            logging.error(f"❌  Error in service layer: {e}")
            return None, str(e)
        
    def get_all(self):
        try:
            docs = list(self.diet_dao.get_all())
            diets = [Diet.from_dict(doc) for doc in docs]
            logging.info(f"✅ Returned all documents")
            return diets, None
        except Exception as e:
            logging.error(f"❌  Error in get_all: {e}")
            return None, str(e)
        
    def get(self, id: str):
        try:
            doc = self.diet_dao.get(id)
            if doc:
                diet = Diet.from_dict(doc)
                logging.info(f"✅ Returned document with ID: {id}")
                return diet.to_dict(), None
            else:
                return "Diet not found", None
        except Exception as e:
            logging.error(f"❌  Error in get: {e}")
            return None, str(e)

    def update(self, id, diet_input: Union[Dict[str, Any], Diet]):
        try:
            diet = self._ensure_diet_obj(diet_input)
            doc = diet.to_dict() 
            self.diet_dao.update(id, doc)
            logging.info(f"✅ Updated document with ID: {id}")
            return diet_input, None
        except Exception as e:
            logging.error(f"❌  Error in service layer: {e}")
            return None, str(e)
        
    def delete(self, id: str):
        try:
            deleted_count = self.diet_dao.delete(id)
            logging.info(f"✅ Deleted document with ID: {id}")
            return str(deleted_count), None
        except Exception as e:
            logging.error(f"❌  Error in get: {e}")
            return None, str(e)