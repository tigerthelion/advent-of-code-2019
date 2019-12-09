# --- Day 1: The Tyranny of the Rocket Equation ---

# --- Part 1 ---
# Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# The Elves quickly load you into a spacecraft and prepare to launch.

# At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

# For example:

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
# The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

# What is the sum of the fuel requirements for all of the modules on your spacecraft?

def round(number: float) -> int:
    num_str = str(number)
    try:
        return int(num_str.split('.')[0])
    except:
        return int(number)

def fuel_requirement(mass: int) -> int:
    fuel_req: int = round(mass / 3) -2
    return fuel_req


# Test cases
# print(fuel_requirement(12) == 2)
# print(fuel_requirement(14) == 2)
# print(fuel_requirement(1969) == 654)
# print(fuel_requirement(100756) == 33583)

module_masses = [147129,
128896,
86366,
121702,
106854,
107418,
96021,
116460,
100395,
149526,
146314,
56215,
59911,
96016,
86483,
115837,
84522,
137658,
105769,
149691,
127499,
95302,
53109,
101940,
106343,
140421,
88790,
105898,
68085,
85027,
99405,
116253,
55338,
50009,
58244,
145865,
145270,
148777,
139954,
147397,
128691,
63082,
144279,
76143,
73006,
105508,
62796,
144807,
66587,
50828,
143778,
73793,
76852,
119991,
103181,
105618,
106320,
136345,
68771,
82534,
94528,
65802,
74863,
139414,
65854,
149543,
87063,
85691,
148931,
139653,
90728,
100710,
110159,
131407,
129323,
145874,
127227,
129006,
105828,
67468,
136905,
89273,
133439,
78783,
90794,
116324,
132792,
135413,
142086,
62659,
59178,
59080,
122465,
62753,
112104,
92551,
90638,
145232,
133984,
139994
]
total_mass = 0
for mass in module_masses:
    total_mass += fuel_requirement(mass)
print(total_mass)


# --- Part Two ---
# During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence. 
# Apparently, you forgot to include additional fuel for the fuel you just added.

# Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. 
# However, that fuel also requires fuel, and that fuel requires fuel, and so on. 
# Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, 
# if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

# So, for each module mass, calculate its fuel and add it to the total. 
# Then, treat the fuel amount you just calculated as the input mass and repeat the process, 
# continuing until a fuel requirement is zero or negative. For example:

# A module of mass 14 requires 2 fuel. This fuel requires no further fuel 
# (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
# 
# At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, 
# which requires 21 fuel, which requires 5 fuel, which requires no further fuel. 
# So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.

# The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

# What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel? 
# (Calculate the fuel requirements for each module separately, then add them all up at the end.)


def calc_fuel_recursive(mass):
    fuel_req: int = round(mass / 3) - 2
    if fuel_req <= 0:
        return 0
    else:
        return fuel_req + calc_fuel_recursive(fuel_req)


# Test cases
# print(calc_fuel_recursive(1969) == 966)
# print(calc_fuel_recursive(100756) == 50346)
total_mass = 0
for module in module_masses:
    total_mass += calc_fuel_recursive(module)
print(total_mass)
