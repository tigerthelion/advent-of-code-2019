# --- Day 4: Secure Container ---
# You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

# However, they do remember a few key facts about the password:

# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Other than the range rule, the following are true:

# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
# How many different passwords within the range given in your puzzle input meet these criteria?

# Your puzzle input is 284639-748759.

# The first half of this puzzle is complete! It provides one gold star: *
# 895 is answer
# --- Part Two ---
# An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

# Given this additional criterion, but still ignoring the range rule, the following are now true:

# 112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
# 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
# 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
# How many different passwords within the range given in your puzzle input meet all of the criteria?



def adjacency_check(sequence):
    sequence = str(sequence)
    seq_len = len(sequence)
    
    chains = []
    chain = sequence[0]
    counter = 1
    while counter < seq_len:
        next_digit = sequence[counter]
        
        if next_digit == chain[-1]:
            chain += next_digit
        else:
            chains.append(chain)
            chain = next_digit

        counter+=1
        cur_digit = next_digit
    chains.append(chain)


    for chain in chains:
        if len(chain) == 2:
            return True   
    
    return False

def increasing_check(sequence):      
    sequence = str(sequence)
    seq_len = len(sequence)
    
    counter = 1
    cur_digit = sequence[0]
    while counter < seq_len:
        next_digit = sequence[counter]
    
        # Check if there is an adjacency
        if next_digit < cur_digit:
            return False
        
        counter+=1
        cur_digit = next_digit
    return True
            

password_count = 0
for i in range(284639,748760):
    if adjacency_check(i) and increasing_check(i):
        password_count +=1

print(password_count)



