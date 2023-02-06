def macro_calculator(weight, protein_ratio, fat_ratio, carb_ratio):
    protein_grams = weight * protein_ratio
    fat_grams = weight * fat_ratio
    carb_grams = weight * carb_ratio
    calories = (protein_grams * 4) + (fat_grams * 9) + (carb_grams * 4)
    sugar = carb_grams / 4
    print("Protein: ", protein_grams, "g")
    print("Fat: ", fat_grams, "g")
    print("Carbs: ", carb_grams, "g")
    print("Calories: ", calories, "cal")
    print("Sugar: ", sugar, "g")

# example usage
weight = 70
protein_ratio = 0.3
fat_ratio = 0.3
carb_ratio = 0.4
macro_calculator(weight, protein_ratio, fat_ratio, carb_ratio)

# The code defines a class BodyWeightLossCalculator that calculates various metrics related to body weight loss.
# The class initializes the following instance variables: gender, age, weight, height, activity_level, goal_weight.
# The class has a method calculate_bmr that calculates the Basal Metabolic Rate (BMR) of a person based on their gender, weight, height, and age.
# The class has a method calculate_tdee that calculates the Total Daily Energy Expenditure (TDEE) of a person based on their activity level and BMR.
# The class has a method calculate_daily_caloric_deficit that calculates the daily caloric deficit required to achieve a person's goal weight.
# The class has a method calculate_macros that calculates the daily amounts of protein, fat, and carbohydrates required to achieve a person's goal weight.