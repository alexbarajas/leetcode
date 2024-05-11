import json

JSON_FILE_PATH = "leetcode_difficulties.json"


def script_for_file_alias_creation_in_difficulty_folder(leetcode_name, difficulty):
    leetcode_name_split = "\ ".join((leetcode_name + ".py").split())
    return f"ln -s ../../all_leetcode/{leetcode_name_split} difficulties/{difficulty}/{leetcode_name_split}"


# Function to load Leetcode difficulties from JSON file
def load_leetcode_difficulties():
    try:
        with open(JSON_FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"easy": [], "medium": [], "hard": []}


# Function to save Leetcode difficulties to JSON file
def save_leetcode_difficulties(leetcode_difficulties):
    with open(JSON_FILE_PATH, "w") as file:
        json.dump(leetcode_difficulties, file, indent=4)


# Function to add a new Leetcode file
def add_leetcode_file():
    leetcode_file = input("What leetcode file? (ex. '1. Two Sum'): ")
    difficulty = input("What difficulty? (easy / medium / hard): ")
    tags = input("What tags separated by commas? (ex. 'array, hashmap'): ")

    # Load Leetcode difficulties from JSON file
    leetcode_difficulties = load_leetcode_difficulties()

    # Append the new Leetcode file to the specified difficulty
    if leetcode_file not in leetcode_difficulties[difficulty]:
        leetcode_difficulties[difficulty].append(leetcode_file)

    # Save updated Leetcode difficulties to JSON file
    save_leetcode_difficulties(leetcode_difficulties)
    generate_symbolic_link_commands()


def generate_symbolic_link_commands():
    with open("symbolic_link_commands.sh", "w") as file:
        file.write("cd .. # this resolves the permission issues by moving to the parent directory\n")
        leetcode_difficulties = load_leetcode_difficulties()
        for difficulty, files in leetcode_difficulties.items():
            for leetcode_file in files:
                command = script_for_file_alias_creation_in_difficulty_folder(leetcode_file, difficulty)
                file.write(command + "\n")


# print(load_leetcode_difficulties())

add_leetcode_file()
# generate_symbolic_link_commands()


# TODO after burger make a function so that 42. Trapping Rain Water gets added to all_leetcode directory also to difficulties/hard


