import requests
import json

class BodyWeightLossCalculator:
    def __init__(self, gender, age, weight, height, activity_level, goal_weight):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.activity_level = activity_level
        self.goal_weight = goal_weight

    def calculate_bmr(self):
        if self.gender == 'male':
            bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        else:
            bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
        return bmr

    def calculate_tdee(self):
        if self.activity_level == 'sedentary':
            tdee = 1.2 * self.calculate_bmr()
        elif self.activity_level == 'lightly active':
            tdee = 1.375 * self.calculate_bmr()
        elif self.activity_level == 'moderately active':
            tdee = 1.55 * self.calculate_bmr()
        elif self.activity_level == 'very active':
            tdee = 1.725 * self.calculate_bmr()
        else:
            tdee = 1.9 * self.calculate_bmr()
        return tdee

    def calculate_daily_caloric_deficit(self):
        target_tdee = self.calculate_tdee()
        target_weight = self.weight - (self.weight - self.goal_weight)
        target_bmr = target_weight * 10 + self.calculate_bmr() - self.weight * 10
        daily_caloric_deficit = target_tdee - target_bmr
        return daily_caloric_deficit

    def calculate_macros(self):
        protein_ratio = 0.30
        fat_ratio = 0.20
        carbohydrate_ratio = 0.50
        daily_protein = self.weight * protein_ratio
        daily_fat = self.weight * fat_ratio
        daily_carbohydrate = self.weight * carbohydrate_ratio
        daily_caloric_deficit = self.calculate_daily_caloric_deficit()
        target_protein = daily_protein
        target_fat = daily_fat
        target_carbohydrate = daily_caloric_deficit - (daily_protein * 4) - (daily_fat * 9)
        return {
            'protein': target_protein,
            'fat': target_fat,
            'carbohydrate': target_carbohydrate
        }

def calculate_diet_macros(gender, age, weight, height, activity_level, goal_weight):
    calculator = BodyWeightLossCalculator(gender, age, weight, height, activity_level, goal_weight)
    return calculator.calculate_macros()
