
def read_file():
    # file = open('days.txt', 'r')

    # data = file.read()
    # print(data)

    # data_list = content.readlines()
    # print(data_list)

    # for line in file:
    #     print(line)

    # file.close()
    
    # context manager --> auto closes
    with open('days.txt', 'r') as file:
        data = file.read()
        print(data)

def write_file():
    with open('study_days.txt', 'w') as file:
        file.write('DSA Day')
        file.writelines(['\nMaths Day', '\nML Day'])

def append_file():
    with open('study_days.txt', 'a') as file:
        file.write('\nProject Day')

characters = ["Mario", "Luigi", "Peach", "Yoshi", "Bowser", "Toad"]

def write_characters_to_file(filename):
    # open file
    file = open(filename, 'w+')
    
    # write to file
    for c in characters:
        file.write(c + "\n")
    
    # Moving the cursor to the start. 
    file.seek(0, 0)
    
    content = file.read()
    print(content)
    
    # close file
    file.close()

    return


def main():
    write_file()
    append_file()
    write_characters_to_file('characters.txt')

if __name__ == "__main__":
    main()