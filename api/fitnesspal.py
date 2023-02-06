import requests
import json

# Define a class for Body Weight Loss Calculator
class BodyWeightLossCalculator:
    # Initialize instance variables for gender, age, weight, height, activity_level, goal_weight
    def __init__(self, gender, age, weight, height, activity_level, goal_weight):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.activity_level = activity_level
        self.goal_weight = goal_weight

    # Method to calculate Basal Metabolic Rate (BMR)
    def calculate_bmr(self):
        # Check if gender is male or female and calculate BMR accordingly
        if self.gender == 'male':
            bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        else:
            bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
        # Return calculated BMR
        return bmr

    # Method to calculate Total Daily Energy Expenditure (TDEE)
    def calculate_tdee(self):
        # Check the activity level and calculate TDEE accordingly
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
        # Return calculated TDEE
        return tdee

    # Method to calculate daily caloric deficit
    def calculate_daily_caloric_deficit(self):
        # Calculate target TDEE and BMR
        target_tdee = self.calculate_tdee()
        target_weight = self.weight - (self.weight - self.goal_weight)
        target_bmr = target_weight * 10 + self.calculate_bmr() - self.weight * 10
        # Calculate daily caloric deficit
        daily_caloric_deficit = target_tdee - target_bmr
        # Return calculated daily caloric deficit
        return daily_caloric_deficit

    # Method to calculate the target macros
    def calculate_macros(self):
        # Define ratios for protein, fat, and carbohydrates
        protein_ratio = 0.30
        fat_ratio = 0.20
        carbohydrate_ratio = 0.50
        # Calculate daily amount of each macro
        daily_protein = self.weight * protein_ratio
        daily_fat = self.weight * fat_ratio
        daily_carbohydrate = self.weight * carbohydrate_ratio
        # Calculate daily caloric deficit
        daily_caloric_deficit = self.calculate_daily_