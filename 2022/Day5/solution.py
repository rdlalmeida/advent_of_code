import os
import re

puzzle_input_file = open(os.getcwd() + "\\2022\\Day5\\puzzle_input.txt")

# Function to read the initial crate arrangement from the puzzle input text file. This arrangement is stored in the initial lines before the empty one
def retrieve_crate_arrangement(input_file):
    line = input_file.readline()
    
    crate_arrangement = []
    
    counter = 1
    
    # Start by reading all the lines from the crate arrangement
    while (line != '\n'):
        crate_arrangement.append(line.strip('\n'))
        
        line = input_file.readline()
        
        counter += 1
        
    # I need to read the crate arrangement array from bottom to top in order to fill up a dictionary with the crate arrangement
    
    queues = crate_arrangement.pop()
    
    # queues is a string like " 1  2  3 ...", i.e., numbers separated by a ton of spaces. Process these into an array of int to be used as dictionary indexes
    queues = re.split(r'\s{2,}', queues)
    
    # The queues list is still full with strings. Convert those to int first
    for i in range(0, len(queues)):
        queues[i] = int(queues[i])
    
    # Create the dictionary
    crates = {}
    
    # And populate it with an empty list for each entry to initialize it
    for i in range(0, len(queues)):
        crates[queues[i]] = []
    
    # Use a while loop to pop lines from the crate arrangement, process them and put them in the corresponding dictionary
    crate_line = crate_arrangement.pop()
    
    
    while(len(crate_arrangement) >= 0):
        
        # First, remove all '[' and ']' from the crate designations
        # crate_line = crate_line.replace('[', '').replace(']', '').replace('   ', '').split(' ')
                
        # print(crate_line)
        
        # Next, I need to be imaginative here... Splitting the string by spaces does not work. Once there's a missing crate in the line, the whole thing freaks out and inserts way more
        # spaces than needed. So, for each line, I can see that I can get the item that I need at every 1 + 4*i index, i a range from 0 to the original
        # line length
        clean_crate_line = ""
        for i in range(1, len(crate_line), 4):
            clean_crate_line += crate_line[i]
            
        # The clean line string has as many characters as there are queues. Populating these in the dictionary should be trivial
        for i in range(0, len(clean_crate_line)):
            if (clean_crate_line[i] != ' '):
                crates[queues[i]].append(clean_crate_line[i])
        
        
        # Get another crate line
        try:
            crate_line = crate_arrangement.pop()
        except:
            # print("Tried to remove a crate line from the arrangement but it is empty already..")
            break
        
    return crates

def retrieve_moves(input_file):
    line = input_file.readline().strip('\n')
    
    # Same as before. In this case, process the lines into three element tuples: the first element is the number of crates to move, then the origin queue,
    # followed by the destination queue
    
    moves = []
    
    while(line != ""):
        # Format the string for an easier processing into a tuple
        line = line.replace('move ', '').replace(' from ', ',').replace(' to ', ',')
        
        print(line)
        
        # Convert the string into an int tuple and store it in the moves list
        moves.append(tuple(map(int, line.split(','))))
        
        # Grab a new line
        line = input_file.readline().strip('\n')
    
    return moves

# Function to move the crates using the 9000 crane model, i.e., the one that moves one crate at a time
def move_crates_9000(crates, moves):
    # I have a dictionary of crates and an array of moves. I can now develop an algorithm to move the crates around based on each tuple in the moves array
    for move in moves:
        # The first tuple item refers to the number of crates to move. Use it as a loop limiter
        crates_to_move = move[0]
        
        while (crates_to_move > 0):
            # Move the crates around using the 2nd and 3rd tuple indexes to access the proper dictionary entry and the pop and append functions to simulate the move of the crates
            crates[move[2]].append(crates[move[1]].pop())
            
            # Decrement the number of crates to move
            crates_to_move -= 1
            
    
    # All done. Extract the top crate in each queue to a string to form the solution
    top_crates = ""
    
    for entry in crates:
        top_crates += crates[entry][len(crates[entry]) - 1]
    
    return top_crates

# Function to move the crates using the 9001 crane model, i.e., the one that moves all the crates at once
def move_crates_9001(crates, moves):
    
    # Cycle through all the moves
    for move in moves:
        crates_to_move = move[0]
        
        # Now use a simple array slice to move the whole line of crates from one queue to the other
        crates[move[2]] += crates[move[1]][len(crates[move[1]]) - crates_to_move::1]
        
        # Notice that the moved crates are still in the original queue. Remove them
        while (crates_to_move > 0):
            crates[move[1]].pop()
            
            crates_to_move -= 1
    
    # Done. Retrieve the string that has the top crates in each queue and return it
    top_crates = ""
    for entry in crates:
        top_crates += crates[entry][len(crates[entry]) - 1]
        
    return top_crates
    
if __name__ == "__main__":
    crates = retrieve_crate_arrangement(input_file=puzzle_input_file)
    
    # print(crates)
    
    moves = retrieve_moves(input_file=puzzle_input_file)
    
    # moves = [(1, 4, 1), (2, 4, 8), (5, 9, 6)]
    
    # print(moves)
    
    # top_crates_9000 = move_crates_9000(crates=crates, moves=moves)
    
    top_crates_9001 = move_crates_9001(crates=crates, moves=moves)
    
    # print("Top crate arrangement with crane 9000 = " + top_crates_9000)
    
    print(crates)
    
    print("Top crate arrangement with crane 9001 = " + top_crates_9001)
    