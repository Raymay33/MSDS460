import pulp
from pulp import LpVariable, LpProblem, lpSum, LpMinimize

model = LpProblem(name="Diet_Problem", sense=LpMinimize)

#Decision variables
x1 = LpVariable("Barilla_Angelhair_Pasta", lowBound=0, cat="Continous")
x2 = LpVariable("Butternut_Italian_bread", lowBound=0, cat="Continuous")
x3 = LpVariable("Dole_Frozen_mixed_fruit", lowBound=0, cat="Continuous")
x4 = LpVariable("Tyson_chicken_nuggets", lowBound=0, cat="Continuous")
x5 = LpVariable("Season_Sardines_in_Olive_Oil", lowBound=0, cat="Continuous")


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

# Solve the problem
model.solve()

# Print the results
print("Total Cost: $", round(model.objective.value(), 2))

# Display servings of each food item
for var in model.variables():
    print(f"{var.name}: {var.value()} servings")
    