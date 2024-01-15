# MSDS460
#Here is my model used to minimize cost of my diet
model += 0.15 * x1 + 0.21 * x2 + 1.33 * x3 + 0.59 * x4 + 2.29 * x5, "Total_Cost"

#Nutritional constraints
model += 0 * x1 + 170 * x2 + 0 * x3 + 470 * x4 + 340 * x5 <= 35000, "Sodium"
model += 200 * x1 + 80 * x2 + 70 * x3 + 270 * x4 + 200 * x5 >= 14000, "Calories"
model += 7 * x1 + 3 * x2 + 1 * x3 + 14 * x4 + 22 * x5 >= 350, "Protein"
model += 0 * x1 + 0 * x2 + 0 * x3 + 0 * x4 + 3 * x5 >= 140, "Vitamin_D"
model += 0 * x1 + 30 * x2 + 25.6 * x3 + 0 * x4 + 358.4 * x5 >= 9100, "Calcium"
model += 2 * x1 + 0.9 * x2 + 0.4 * x3 + 0 * x4 + 1.6 * x5 >= 126, "Iron"
model += 118 * x1 + 27 * x2 + 210 * x3 + 130 * x4 + 306 * x5 >= 32900, "Potassium"

Above were the values that I gathered for each of the food items and their nutrional values

The final total cost was 130.54
It used 46.67 servings of sardines and 157.79 servings of pasta
This was due to pasta containing 0 sodium meaning that it did not have to worry about going over the maximum intake plus pasta was the cheapest item out of the five items I choose. 
Sardines were so heavily used because they were the only item to contain a signifigant amount of vitamin D and calcium which were two requirements of my diet. 
