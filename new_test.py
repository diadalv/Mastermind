from collections import Counter
from itertools import product, permutations

def gen_color_combinations(
    code_length: int,
    total_colors: int,
    repeat_color: bool
) -> list[tuple]:
    """
    Generates all valid Mastermind codes.

    Args:
        code_length:   Number of positions in a code (e.g. 4).
        total_colors:  Number of distinct colors available (e.g. 6).
        repeat_color:  If True, the same color may appear more than once.
                       If False, each color may appear at most once.

    Returns:
        A list of tuples, each representing one possible code.
        Colors are represented as integers 1..total_colors.
        
    """

    """ Color list creation """
    colors = list(range(1, total_colors + 1))

    if repeat_color:
        """ Generate list of tuples with repeating colors """ 
        return list(product(colors, repeat=code_length))
    else:
        """ Generate list of tuples without repeating colors """
        return list(permutations(colors, code_length))



def validate_answered_colors(color_code, round_answer):
    exact_match = 0 # counter για τη σωστή θέση
    color_match = 0 # counter για τη λάθος θέση
    already_counted = [] # λίστα για χρώματα που ήδη μετρήσαμε 
    
    for i in range(len(color_code)):
        
        if color_code[i] == round_answer[i]:
            exact_match += 1 
        elif round_answer[i] in color_code:
            if already_counted.count(round_answer[i]) < color_code.count(round_answer[i]): #ελέγχουμε αν έχουμε μετρήσει ήδη το χρώμα
                color_match += 1 
                already_counted.append(round_answer[i]) # προσθέτουμε το χρώμα που ήδη μετρήσαμε σε άλλη λίστα

    return [exact_match, color_match]



def evaluate_color_combination(color_combinations, round_answer, answered_colors):
    combinations_to_keep= []
    
    for combination in color_combinations:
        answered_colors = validate_answered_colors(combination, round_answer)
           
        
        # Με την Counter βρίσκουμε τους συνδυασμούς των χρωμάτων 
        counter_combination = Counter(combination)
        counter_round_answer = Counter(round_answer)
                   
        common_counts = sum((counter_combination & counter_round_answer).values())
        common_answered_colors = answered_colors[0] + answered_colors[1]
        
        if common_counts == common_answered_colors:
            correct_position_color = 0
            for i in range(len(combination)):
                if combination[i] == round_answer[i]:
                    correct_position_color += 1            
            
            wrong_position_color = common_counts - correct_position_color 
            if answered_colors[0] == correct_position_color and answered_colors[1] == wrong_position_color:
                combinations_to_keep.append(combination) 
                       
    return combinations_to_keep     
              
              
color_combinations = gen_color_combinations(code_length=3, total_colors=5, repeat_color=False)  
# color_combinations = evaluate_color_combination(color_combinations, [2,2,1,3])
# for color in color_combinations:
    
#     print(color)     
print(len(color_combinations))

print("-------------------------------------------")

    
new_color_combinations = evaluate_color_combination(color_combinations, [3,2,1], [0,1]) # 1,4,5
for color in new_color_combinations:
    print(color)         

print(len(new_color_combinations))