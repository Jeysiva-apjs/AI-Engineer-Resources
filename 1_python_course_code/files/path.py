from pathlib import Path

def read_file(file_name):
    path = Path(__file__).parent
    file_path = path / file_name
    with open(file_path, 'r') as file:
        data = file.read()
        print(data)

def main():
    read_file('characters.txt')

if __name__ == "__main__":
    main()
