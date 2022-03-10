import math

# This value kept popping up in all the calculations so I made it a constant
# I shall call it the "Nekoto's Constant"! (Just a joke don't sue me pls)
c = math.sqrt(3.0) / 2.0

# Finds the radius of incircle given a side length of triangle
def herons_equilateral(side_length = 1.0):
    semiperimeter = (3.0 * side_length) / 2.0
    numerator = pow(semiperimeter - side_length, 3.0)
    frac = numerator / semiperimeter
    return math.sqrt(frac)

# Basic Trig to get hypotenuse from height of triangle
def hyp_from_height(height):
    global c
    return height / c

# Stores data of each triangle based on series index
triangle_dict = {}
# Number of terms to take in the infinite series
terms = 30

total_area = 0.0
for t in range(1, terms + 1):
    if t == 1:
        radius = herons_equilateral(1.0)
        triangle_height = c
        triangle_dict[t] = [radius, triangle_height]
        
        circle_area = math.pi * pow(radius, 2.0)
        total_area += circle_area

        continue

    last_triangle_data = triangle_dict[t - 1]
    lt_radius = last_triangle_data[0]
    lt_height = last_triangle_data[1]
    new_height = lt_height - (2.0 * lt_radius)
    new_hyp = hyp_from_height(new_height)
    new_radius = herons_equilateral(new_hyp)

    triangle_dict[t] = [new_radius, new_height]

    new_circle_area = math.pi * pow(new_radius, 2.0) * 3.0
    total_area += new_circle_area


# Verify answer
true_answer = 11.0 * math.pi / 96.0
print("True Answer: " + str(true_answer))
print("Your Answer: " + str(total_area))
