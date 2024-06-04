import os

# Function to determine the last position of a block of 4 characters where these characters are all distinct, for the first time in it
def detectSequenceStart(sequence, slot_size):
    # Use an incremental loop to build the 4 character window and move it to the right until 4 distinct characters are set in it
    for i in range(0, len(sequence) - slot_size, 1):
        # Set the window
        slot = sequence[i:(i + slot_size)]
        
        # Determine if all characters are unique
        if (uniqueWindow(slot)):
            # If a True was returned from the last execution, I found the beginning of the sequence. Return the index of the last
            # character, as intended
            return (i + slot_size)
        
        # Otherwise, continue with the analysis
    
    # If this for reaches the end without finding a valid sequence, raise an Exception
    raise Exception("ERROR: Unable to find a 4 character window with only distinct characters")
        

# This function receives a 4 character window (sub string) and returns if all characters in it are different from each other or not
def uniqueWindow(slot):
    # if (len(slot) != 4):
    #     raise Exception("ERROR: The window provided: " + slot + " does not have the required 4 characters.")
    
    # Convert the string into a 4 element list for easier manipulation
    slot_list = []
    slot_list[:0] = slot
    
    # Use a while loop to ensure all characters are different. Return false if that is not the case
    while (len(slot_list) > 0):
        char0 = slot_list.pop()
        
        if(char0 in slot_list):
            # If the character that I just extracted has a copy in the list, it means that not all characters are unique.
            # Nothing else to do but to return the reply
            return False
    
    # If the list was processed and the condition that returns False was never encountered, it means that this window has only
    # distinct elements in it. Return True if the code gets to this point
    return True
    

if __name__ == "__main__":
    puzzle_input_path = os.getcwd() + "\\2022\\Day6\\puzzle_input.txt"
    puzzle_input_handle = open(puzzle_input_path)
    sequence = puzzle_input_handle.readline().strip('\n')
    
    sequence_start = detectSequenceStart(sequence, 14)
    
    print("The transmission starts at index = " + str(sequence_start))
    
    examples = [
        "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
        "bvwbjplbgvbhsrlpgdmjqwftvncz",
        "nppdvjthqldpwncqszvftbrmjlhg",
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
                ]
    
    for example in examples:
        last_index = detectSequenceStart(example, 14)
        print(example + " = " + str(last_index))