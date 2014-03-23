def load_data(filename):
    '''file to load data'''
    with open(filename, 'r') as f: #open the file
        contents = f.readlines() #put the lines to a variable.
    print contents
    return contents