# Imports python modules
from time import time, sleep

# Imports functions created for this program
from get_input_args import get_input_args
from unlockpikepdf import unlockpikepdf


def main():
    in_arg = get_input_args()

    data = in_arg.data
    suff = in_arg.suff
    dir = in_arg.dir

    print('Data to load: ', data)
    print('Suffix to add: ', suff)
    print('Folder to save the file(s): ', dir)

    unlockpikepdf(data=in_arg.data, suff=in_arg.suff, dirtosave=in_arg.dir)


# Call to main function to run the program
if __name__ == "__main__":
    main()

# unlockpikepdf(data='ETT1-3000-PE-576-0001-00.pdf',
#               suff='_out', dirtosave='')

# unlockpikepdf(data=r'C:\Users\afsn3\Documents\GitHub\unlockpikepdf',
#               suff='_out', dirtosave='')

# TODO Developing a Unit Test
# https://code.visualstudio.com/docs/python/testing
