import os

# Start by reading each line of the puzzle_input.txt file into an array of strings
elf_assignments = open(os.getcwd() + "\\2022\\Day4\\puzzle_input.txt")
# elf_assignments = open(os.getcwd() + "\\2022\\Day4\\test.txt")

# Get the first line and strip it from any newlines terminating it
line = elf_assignments.readline().strip('\n')

# Setup an array to store the cases where one assignment fully contains another
fully_contained = []

# And another for the ones that just overlap
overlapping_assignments = []
non_overlapping_assignments = []

# Create a simple counter to identify the line assignments. Set it to 1 because I've read one line already
counter = 1

# Do this while there are assignments to process
while (line != ""):
    
    # Extract both assignments by splitting the string by the separating comma
    assignments = line.split(',')
    
    # Extract the assignment values to a list too
    assignmentA = assignments[0].split('-')
    
    # Check if only two values were also returned from this one
    if (len(assignmentA) != 2):
        raise Exception("ERROR: The fist assignment on line " + str(counter) + " has " + str(len(assignmentA)) + " limits instead of the expected 2. Cannot continue")
    
    # Repeat the process for the other one
    assignmentB = assignments[1].split('-')
    
    if (len(assignmentB) != 2):
        raise Exception("ERROR: The second assignment on line " + str(counter) + " has " + str(len(assignmentB)) + " limits instead of the expected 2. Cannot continue.")
    
    # I expect two and exactly two elements in the list returned. Validate that first
    if (len(assignments) != 2):
        raise Exception("ERROR: Line " + str(counter) + " has " + str(len(assignments)) + " instead of the 2 expected. Cannot continue...")
    
    # Each assignment is comprised of a min and a max value. An assignment A fully contains another assignment B if
    # minB >= minA && maxB <= maxA
    # This comparison needs to go both ways.
    minA = int(assignmentA[0])
    maxA = int(assignmentA[1])
    
    minB = int(assignmentB[0])
    maxB = int(assignmentB[1])
    
    if ((minA >= minB and maxA <= maxB) or (minB >= minA and maxB <= maxA)):
        # If this rule is verified, one of the assignments fully contains the other. Add it to the list if so
        fully_contained.append(line)
        
    # On the other hand, the rule to detect a overlapping assignment is actually simpler. Considering the same A, B assignments with a min and a max each, an assignment overlaps
    # another if:
    # maxA >= minB and maxB >= minA, which can also be written as
    # minB <= maxA and minA <= maxB
    
    if ((maxA >= minB) and (maxB >= minA)):
        overlapping_assignments.append(line)
    else:
        non_overlapping_assignments.append(line)
    
    # Read a new line
    line = elf_assignments.readline().strip('\n')
    
    # Increment the counter before going for another line processing
    counter += 1

# The last line was empty. Decrement the counter so that everything matches up
counter -= 1
    
# Printout all fully contained assignments
# for assignment in fully_contained:
#     print(assignment)
    
print("From " + str(counter) + " assignments considered, " + str(len(fully_contained)) + " had one of them fully contained in the other")

# Printout all overlapping assignments
# for assignment in overlapping_assignments:
#     print(assignment)
    
print("From " + str(counter) + " assignments considered, " + str(len(overlapping_assignments)) + " were found overlapping")

# Printout all non overlapping assignments. These are easier to verify
# for assignment in non_overlapping_assignments:
#     print(assignment)
    
print("From " + str(counter) + " assignments considered, " + str(len(non_overlapping_assignments)) + " were found non overlapping")