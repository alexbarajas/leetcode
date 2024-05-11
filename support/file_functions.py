import os
import json
import subprocess

JSON_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../support/leetcode_difficulties.json"))
ALL_LEETCODE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../all_leetcode"))
DIFFICULTIES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../difficulties"))
SYMBOLIC_LINK_COMMAND_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../support/symbolic_link_commands.sh"))


def script_for_file_alias_creation_in_difficulty_folder(leetcode_name, difficulty):
    leetcode_name_split = "\ ".join((leetcode_name + ".py").split())
    return f"ln -s ../../all_leetcode/{leetcode_name_split} difficulties/{difficulty}/{leetcode_name_split}"


def create_leetcode_python_file(leetcode_name):
    os.makedirs(ALL_LEETCODE_PATH, exist_ok=True)
    all_leetcode_path = os.path.join(ALL_LEETCODE_PATH, leetcode_name + ".py")
    with open(all_leetcode_path, "w") as file:
        file.write("")


def load_leetcode_difficulties():
    try:
        with open(JSON_FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"easy": [], "medium": [], "hard": []}


def save_leetcode_difficulties(leetcode_difficulties):
    with open(JSON_FILE_PATH, "w") as file:
        json.dump(leetcode_difficulties, file, indent=4)


def add_leetcode_file():
    leetcode_file = input("What leetcode file? (ex. '1. Two Sum'): ")
    difficulty = input("What difficulty? (easy / medium / hard): ")
    # TODO incorporate tags when you have some spare time
    # tags = input("What tags separated by commas? (ex. 'array, hashmap'): ")
    leetcode_difficulties = load_leetcode_difficulties()
    if leetcode_file not in leetcode_difficulties[difficulty]:
        leetcode_difficulties[difficulty].append(leetcode_file)
        save_leetcode_difficulties(leetcode_difficulties)
        create_leetcode_python_file(leetcode_file)
        generate_symbolic_link_commands()


def generate_symbolic_link_commands():
    with open(SYMBOLIC_LINK_COMMAND_FILE, "w") as file:
        file.write("cd .. # this resolves the permission issues by moving to the parent directory\n")
        leetcode_difficulties = load_leetcode_difficulties()
        for difficulty, files in leetcode_difficulties.items():
            for leetcode_file in files:
                command = script_for_file_alias_creation_in_difficulty_folder(leetcode_file, difficulty)
                file.write(command + "\n")
    try:
        subprocess.run(["bash", SYMBOLIC_LINK_COMMAND_FILE], check=True)
        print(f"{leetcode_file}, successfully added.")
    except subprocess.CalledProcessError:
        pass


add_leetcode_file()
