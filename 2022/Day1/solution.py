import os

if __name__ == "__main__":
    # Start by opening the puzzle_input file to a file handler
    elves_stores_path = os.getcwd() + "\\2022\\Day1\\puzzle_input.txt"
    elves_stores_file = open(elves_stores_path)
    
    # This one is really simple:
    # Use a nested loop to detect breaks (empty lines that denote another elf). The outer loop is used to force more iterations after finding an empty line, which
    # is typically the stop condition for while loops and I want to use those. The rest is easy. Accumulate all the calories read per elf in a variable and append it
    # to a list at the end of each inner loop. Simple
    
    # Read the first line
    line = elves_stores_file.readline().strip("\n")
    
    # Create an empty list to store the aggregated calorie counts
    total_calories_per_elf = []
    
    # Create the partial calorie accumulator
    current_calorie_count = 0
    # And lets go to work
    while (line != ""):
        while(line != ""):
            current_calorie_count += int(line)
            
            line = elves_stores_file.readline().strip("\n")
        
        # At this point I have read all the calories for the current elf into the accumulator. My line is now empty
        # First, store the current accumulator in the list and reset it to 0
        total_calories_per_elf.append(current_calorie_count)
        
        current_calorie_count = 0
        
        # And now try to read another line. If there is another elf after the least one, the line has another value and the cycle repeats.
        # But if the end of the file has been reached, another read operation now throws an exception. Capture it and deal with it instead of breaking this
        
        try:
            line = elves_stores_file.readline().strip()
        except Exception:
            # In this case, simply set the line back to an empty string and let the stop condition of the outer while do its thing
            line = ""
    
    # At this point, all elves where proper processed. Print out the final list and use a simple max to determine the one carrying the most calories
    # print(total_calories_per_elf)
    
    print("There is an elf carrying " + str(max(total_calories_per_elf)) + ". No one else has more than this dude")
    
    # The second part of this problem is even easier: sort the array with the cumulative results and add up the last three elements
    total_calories_per_elf.sort(reverse=False)
    
    print("Sorted list of total calories per elf:")
    print(total_calories_per_elf)
    
    # Extract the three last element
    heaviest_elves = total_calories_per_elf[len(total_calories_per_elf) - 3:]
    
    print("The heaviest elves are:")
    print(heaviest_elves)
    
    print("These carry a total of " + str(sum(heaviest_elves)) + " calories between them")