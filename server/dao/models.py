from dataclasses import dataclass, field, asdict
from typing import Dict, Any, Optional

@dataclass
class MealItem:
    food: str
    amount: int
    unit: str
    calories: int

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
    
    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MealItem":
        return MealItem(
            food=d.get("food", ""),
            amount=int(d.get("amount", 0)),
            unit=d.get("unit", ""),
            calories=int(d.get("calories", 0)),
        )

@dataclass
class Meal:
    items: list[MealItem]
    total_calories: int = field(init=False)
    
    def __post_init__(self):
        self.total_calories = sum(int(item.calories) for item in self.items)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [item.to_dict() for item in self.items],
            "total_calories": self.total_calories,
        }
        
    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Meal":
        items = [MealItem.from_dict(i) for i in d.get("items", [])]
        meal = Meal(items)
        if "total_calories" in d:
            try:
                meal.total_calories = int(d["total_calories"])
            except Exception:
                meal.total_calories = sum(int(it.calories) for it in meal.items)
                
        return meal

@dataclass
class Diet:
    date: str
    time: str
    meal: Meal
    id: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        d = {
            "date": self.date,
            "time": self.time,
            "meal": self.meal.to_dict(),
        }
        
        return d
    
    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Diet":
        id = d.get("_id")
        meal_dict = d.get("meal", {}) if isinstance(d, dict) else {}
        meal = Meal.from_dict(meal_dict)
        return Diet(
            date=d.get("date", ""),
            time=d.get("time", ""),
            meal=meal,
            id=str(id)
        )