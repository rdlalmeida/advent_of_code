import os

# First, a simple reminder:
# A = X = Rock = 1
# B = Y = Paper = 2
# C = Z = Scissors = 3
# 
# Rock beats Scissors and Paper beats Rock, so A Z = LOSS (0), A X = TIE (3) and A Y = WIN (6)
# Paper beats Rock and Scissors beats Paper, so B X = LOSS (0), B Y = TIE (3) and B Z = WIN (6)
# Scissors beats Paper and Rock beats Scissors, so C Y = LOSS (0), C Z = TIE (3) and C X = WIN (6)
# 
# The second part of the problem establishes that:
# X = LOSS
# Y = TIE
# Z = WIN

# This function receives the puzzle_input file handler and returns a list of 2 element tuples with each move coded as one character strings
def getMoves(puzzle_input):
    # Create and empty list to store the processing results
    moves_list = []
    
    # Read the first line of the file
    line = puzzle_input.readline().strip('\n')
    
    # Same old, same old: use a loop to go through every line in the file, process them into two element tuples and store them in a list to be returned
    while(line != ""):
        move = line.split(" ")
        moves_list.append(tuple(move))
        
        line = puzzle_input.readline().strip('\n')
    
    # All done. Return the final list
    return moves_list

# This function processes the list of moves and calculates a score per move based on the rules established above, i.e., if the move resulted in a win, tie or loss plus the score associated to the move of the second column
def processMoves(moves_list):
    # Create an empty list to store the scores of each move
    move_scores = []
    
    # And process the input list in a loop
    for move in moves_list:
        # Reset the partial score keeper
        base_score = 0
        
        # Now its just a matter of coding the rules established above
        # The fist move is Rock
        if move[0] == 'A':
            if move[1] == 'Z':
                # LOSS
                base_score += 0
            elif move[1] == 'X':
                # TIE
                base_score += 3
            elif move[1] == 'Y':
                # WIN
                base_score += 6
            else:
                # Raise an exception if the second move is neither 'X', 'Y', or 'Z'
                raise Exception("ERROR: Illegal second move detected: " + move[1] + ". Cannot continue...")
                
        # The fist move is Paper
        elif move[0] == 'B':
            if move[1] == 'X':
                # LOSS
                base_score += 0
            elif move[1] == 'Y':
                # TIE
                base_score += 3
            elif move[1] == 'Z':
                # WIN
                base_score += 6
            else:
                raise Exception("ERROR: Illegal second move detected: " + move[1] + ". Cannot continue...")
            
        # The fist move is Scissors then
        elif move[0] == 'C':
            if move[1] == 'Y':
                # LOSS
                base_score += 0
            elif move[1] == 'Z':
                # TIE
                base_score += 3
            elif move[1] == 'X':
                # WIN
                base_score += 6
            else:
                raise Exception("ERROR: Illegal second move detected: " + move[1] + ". Cannot continue...")
        
        # Otherwise something weird must have happened...
        else:
            raise Exception("ERROR: Unrecognizable move detected: " + move[0] + ". Cannot continue...")
        
        # Win, tie and loss condition processed. Now to count the score from the second move
        if move[1] == 'X':
            base_score += 1
        elif move[1] == 'Y':
            base_score += 2
        else:
            base_score += 3
        
        # Done. Store this in the score list and continue with another one
        move_scores.append(base_score)
    
    # All done. Return the final score list
    return move_scores

# This function is for the second part of the problem. It receives the original list of moves and changes it according to the rules specified
# For example, if an original move is ('A', 'X'), in this context it means that the first move was Rock and the contest must end in a LOSS, so the moves needs to be translated to
# (Rock, Paper), i.e., ('A', 'Y'). This way I can use the other function to compute the final result as before
def translateMoves(moves_list):
    new_moves_list = []
    
    for move in moves_list:
        # Fist move is Rock
        if move[0] == 'A':
            # And the context needs to end in a LOSS
            if move[1] == 'X':
                # Set the second move to Scissors to force a LOSS
                new_moves_list.append(tuple([move[0], 'Z']))
                continue
            
            # Now I need to force a tie
            elif move[1] == 'Y':
                # So set the second move to Rock as well
                new_moves_list.append(tuple([move[0], 'X']))
                continue
            else:
                # Otherwise it needs to end in a win so set the second move to Paper
                new_moves_list.append(tuple([move[0], 'Y']))
                continue
        # Repeat this logic for the rest
        elif move[0] == 'B':
            if move[1] == 'X':
                new_moves_list.append(tuple([move[0], 'X']))
                continue
            elif move[1] == 'Y':
                new_moves_list.append(tuple([move[0], 'Y']))
                continue
            else:
                new_moves_list.append(tuple([move[0], 'Z']))
                continue
        else:
            if move[1] == 'X':
                new_moves_list.append(tuple([move[0], 'Y']))
                continue
            elif move[1] == 'Y':
                new_moves_list.append(tuple([move[0], 'Z']))
                continue
            else:
                new_moves_list.append(tuple([move[0], 'X']))
                continue
    
    # Done. Return the translated list and move on
    return new_moves_list
            
    

if __name__ == "__main__":
    input_path = os.getcwd() + "\\2022\\Day2\\puzzle_input.txt"
    
    input_file = None
    
    try:
        input_file = open(input_path)
    except Exception:
        print("Unable to open the file at " + input_path)
        exit()
    
    moves_list = getMoves(input_file)
    # moves_list = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]
    # print(moves_list)
    
    # Translate the list according to the rules in the second part of this problem
    new_moves_list = translateMoves(moves_list)
    
    # print("\n\nTranslated moves: ")
    # print(new_moves_list)
    
    scores_list = processMoves(new_moves_list)
    
    # The final answer is simply the sum of the previous list
    print("Total score = " + str(sum(scores_list)))