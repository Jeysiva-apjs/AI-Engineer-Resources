from pathlib import Path
import json

# py dictionary
bootcamp_content = {
    "topics": [
        'Python', 'SQL', 'Math and Statistics', 'Machine Learning', 'Deep Learning', 'Virtual Internship'
    ]
}

path = Path(__file__).parent
path = path / 'bootcamp.json'

def write_json(): 
    with open(path, 'w') as file:
        json.dump(bootcamp_content, file, indent=2)

def read_json():
    with open(path, 'r') as file:
        content = json.load(file)
    print(content)


def main():
    write_json() 
    read_json()

if __name__ == "__main__":
    main()
