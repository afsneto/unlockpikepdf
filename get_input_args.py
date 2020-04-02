import argparse


def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Path or file to unlock pdf files --data with default value ''
      2. Directory to save the output files --dir with default value ''
      3. Suffix to save the original files

     Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object 
    """

    # Create Parse using ArgumentParser
    welcome = "Unlock .pdf files with passwords"
    parser = argparse.ArgumentParser(description=welcome)

    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument('--data', '-d', required=True, type=str, default='',
                        help='Path or file to unlock pdf files')
    parser.add_argument('--dir', type=str, default='',
                        help='Directory to save the files')
    parser.add_argument('--suff', type=str, default='',
                        help='Suffix of unlock files')

    # Replace None with parser.parse_args() parsed argument collection that
    # you created with this function
    return parser.parse_args()
