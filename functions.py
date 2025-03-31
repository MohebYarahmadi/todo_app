import os

if not os.path.exists('files/todos.txt'):
    with open('files/todos.txt', 'w') as file:
        pass

def banner(witdh):
    print(" Cli Todo ".center(witdh, '='))
    print("You can manage your todo list by these commands:")
    print("add show remove remove compeleted")
    print("".center(witdh, '-'))


def parse_command(prompt):
    """Parse user input into command and flags.
    
    Args:
        prompt (str): The input prompt to display to the user.
        
    Returns:
        tuple: A tuple containing:
            - has_flags (bool): True if input contains additional text after command
            - raw_input (str): Return the if there is no flag after command
            - command (str): The extracted command (first word) if flag provided
            - space_pos (int): Position of first space, or -1 if none
    """
    # Get and clean user input
    raw_input = input(prompt).lower().strip()
    
    # Find the first space character
    space_pos = raw_input.find(' ')
    
    # Extract command and determine if flags exist
    if space_pos == -1:
        command = raw_input
        has_flags = False
    else:
        command = raw_input[:space_pos]
        has_flags = True
    
    return has_flags, raw_input, command, space_pos


def _space_pos(raw_input):
    return raw_input.find(' ')


def _get_list(filepath='files/todos.txt'):
    """Read to-do tasks from a textfile and return
    them as a list.
    
    Args:
        path (str): The path to the text file.
        
    Returns:
        list: A list containing:
            - Lines of the text file
    """
    with open(filepath) as file:
        return file.readlines()
    

def _post_list(lst, filepath='files/todos.txt'):
    """Write to-do tasks list in the text file.
    
    Args:
        path (str): The path to the text file.
        lst (list): A list to write into a text file.
        
    Returns:
        void
    """
    with open(filepath, 'w') as file:
        file.writelines(lst)


def _div(title, width=50, symbol='-'):
    """Print a divider with title in middle.
    
    Args:
        title (str): The title to put in the middle.
        width (int): Total width + title width.
        symbol (str): A character to use draw the divider.
    """
    print(f" {title} ".center(width, symbol))
