from give_bmi import give_bmi, apply_limit


height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
bmi = [22.507863455018317, 28.997794961352657]
print(apply_limit(bmi, 26))
