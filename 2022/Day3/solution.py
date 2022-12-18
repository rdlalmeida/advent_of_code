import os

# This function receives a line from the puzzle_input file, validates it, and analyses it and returns the odd element in there, i.e., 
# the one that is not supposed to belong there (the only character in both halves of the input string)
def getOddElement(line):
    # Check if the line received has an even number of characters. Raise an exception if not
    if (len(line) % 2 != 0):
        raise Exception("ERROR: The line received '" + str(line) + "' does not have an even number of characters. Cannot continue...")
    
    # Alright, split the string in half
    line0 = line[0: int(len(line)/2)]
    line1 = line[int(len(line)/2): len(line)]
    
    # Raise an Exception if, by some reason, the two halves don't have the same length
    if (len(line0) != len(line1)):
        raise Exception("ERROR: line0 has " + str(len(line0)) + "characters, while line1 has " + str(len(line1)) + " characters. Cannot continue...")
    
    # Use a loop to find which element is present in both halves
    common_elements = []
    for item0 in line0:
        # If a character from the first half is in the second one
        if item0 in line1:
            # Set into the final array
            common_elements.append(item0)
                
    # The common elements array should have only one element. Validate this before returning it
    if len(common_elements) != 1:
        # This may mean that there's simply more than one of the odd elements in one half of the rucksack. Validate if the elements
        # in the array are the same. Raise the exception only if more than one different element was found
        while (len(common_elements) > 1):
            item = common_elements.pop()
            
            # If the item that I just popped is not in the remaining elements, i. e., there are more than one odd element in the rucksack
            if item not in common_elements:
                # Raise the exception then
                raise Exception("ERROR: Found more than one common element in the strings: " + ",".join(common_elements) + ". Expected only one of these")
    
    # If not, all is good. Return the item back
    return common_elements[0]

# This function receives a list with the odd elements found and computes the final score based on the priority assignments, which
# is basically the ASCII int value of each character
def computePriorities(odd_elements):
    final_score = 0
    
    for item in odd_elements:
        if 97 <= ord(item) <= 122:
            # Got a small cased value. Subtract 96 from it, since ord('a') = 97 and I want 'a' = 1, 'b' = 2, ..., 'z' = 26
            final_score += (ord(item) - 96)
            # print("'" + str(item) + "' = " + str(ord(item) - 96))
            
        elif 65 <= ord(item) <= 90:
            # Its an upper case character then. Subtract 38 instead because ord('A') = 65 and I want 'A' = 27, 'B' = 28, ..., 'Z' = 52
            final_score += (ord(item) - 38)        
            # print("'" + str(item) + "' = " + str(ord(item) - 38))
            
    # Done. Return the final result
    return final_score

# This function receives 3 lines from the puzzle input and determines the common character is all of them, if any
def getBadges(line0, line1, line2):
    common_items = []
    for item in line0:
        if (item in line1) and (item in line2):
            # Put the item in the array only if I it is present in all of the lines
            common_items.append(item)
    
    # Validate against multiple common elements found
    if (len(common_items) != 1):
        while(len(common_items) > 1):
            item = common_items.pop()
            
            if item not in common_items:
                raise Exception("ERROR: Found more than one common element in the strings: " + ",".join(common_items) + ". Expected only one of these")
    
    print(common_items[0])
    return common_items[0]
            
if __name__ == "__main__":
    # Same old, same old
    puzzle_input_path = os.getcwd() + "\\2022\\Day3\\puzzle_input.txt"
    puzzle_input_handler = open(puzzle_input_path)
    
    odd_items = []
    
    line = puzzle_input_handler.readline().strip('\n')
    
    lines = []
    badges = []
    
    while (line != ""):
        while (len(lines) < 3):
            lines.append(line)
            line = puzzle_input_handler.readline().strip('\n')
        
        # Got three lines in the array. Call the function, reset the array and read a new line
        badges.append(getBadges(lines[0], lines[1], lines[2]))
        
        lines = []
        
        ################# SOLUTION FOR PART 1 ##############
        # odd_items.append(getOddElement(line=line))
        
        # line = puzzle_input_handler.readline().strip('\n')
        ################# SOLUTION FOR PART 1 ##############
    
    print(badges)
    print("Got " + str(len(badges)) + " badges out of this")
    
    badges_score = computePriorities(badges)
    
    print("Badges final score: " + str(badges_score))
    
    # Check out the results
    # print(odd_items)
    
    # small = []
    # large = []
    
    # for i in range(97, 123, 1):
    #     small.append(chr(i))
    
    # for i in range(65, 91, 1):
    #     large.append(chr(i))
    
    # small_score = computePriorities(small)
    
    # print("Small case score = " + str(small_score))
    
    # large_score = computePriorities(large)
    # print("Large case score = " + str(large_score))
    
    final_score = computePriorities(odd_elements=odd_items)
    