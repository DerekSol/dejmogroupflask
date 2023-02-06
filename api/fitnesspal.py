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

