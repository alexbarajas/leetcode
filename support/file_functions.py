import os
import json
import subprocess

JSON_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "leetcode_data.json"))
ALL_LEETCODE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../all_leetcode"))
SYMBOLIC_LINK_COMMAND_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../support/symbolic_link_commands.sh"))


def string_split(string, python_file=False):
    if not python_file:
        return "\ ".join((string.replace(" ", "_")).split())
    return "\ ".join((string + ".py" if python_file else string).split())


def script_for_file_alias_creation_in_difficulty_folder(leetcode_name, difficulty):
    leetcode_name_split = string_split(leetcode_name, True)
    return f"ln -s ../../../all_leetcode/{leetcode_name_split} ../leetcode_groups/difficulties/{difficulty}/{leetcode_name_split}"


def script_for_file_alias_creation_in_topic_folder(leetcode_name, topics):
    leetcode_name_split = string_split(leetcode_name, True)
    commands = []
    for topic in topics:
        topic_name_split = string_split(topic)
        topic_folder = os.path.join(os.path.dirname(__file__), "../leetcode_groups/topics")
        topic_folder = os.path.join(topic_folder, topic_name_split)
        if not os.path.exists(topic_folder):
            os.makedirs(topic_folder)
        command = f"ln -s ../../../all_leetcode/{leetcode_name_split} ../leetcode_groups/topics/{topic_name_split}/{leetcode_name_split}"
        commands.append(command)
    return commands


def load_leetcode_data():
    try:
        with open(JSON_FILE_PATH, "r+") as file:
            return json.load(file)
    except FileNotFoundError:
        with open(JSON_FILE_PATH, "a+") as file:
            json.dump({}, file, indent=4)
            return {}
    except json.JSONDecodeError:
        with open(JSON_FILE_PATH, "a+") as file:
            json.dump({}, file, indent=4)
            return {}


def save_leetcode_data(leetcode_data):
    with open(JSON_FILE_PATH, "w") as file:
        json.dump(leetcode_data, file, indent=4)


def create_leetcode_python_file(leetcode_name):
    os.makedirs(ALL_LEETCODE_PATH, exist_ok=True)
    all_leetcode_path = os.path.join(ALL_LEETCODE_PATH, leetcode_name + ".py")
    with open(all_leetcode_path, "w") as file:
        file.write("")


def add_leetcode_file():
    leetcode_file = input("What leetcode file? (ex. '1. Two Sum'): ")
    difficulty = input("What difficulty? (easy / medium / hard): ")
    tags = input("What tags separated by commas? (ex. 'array, hash table'): ")
    topics = [tag.strip() for tag in tags.split(",")] if tags else []
    leetcode_data = load_leetcode_data()
    if leetcode_file not in leetcode_data:
        leetcode_data[leetcode_file] = {
            "difficulty": difficulty,
            "topics": topics
        }
        save_leetcode_data(leetcode_data)
        create_leetcode_python_file(leetcode_file)
        generate_symbolic_link_commands()
    else:
        print(f"{leetcode_file} is already in the data")


def generate_symbolic_link_commands():
    with open(SYMBOLIC_LINK_COMMAND_FILE, "w") as file:
        leetcode_data = load_leetcode_data()
        for leetcode_file, details in leetcode_data.items():
            difficulty = details["difficulty"]
            difficulty_command = script_for_file_alias_creation_in_difficulty_folder(leetcode_file, difficulty)
            file.write(difficulty_command + "\n")
            topics = details["topics"]
            topic_commands = script_for_file_alias_creation_in_topic_folder(leetcode_file, topics)
            for command in topic_commands:
                file.write(command + "\n")
    try:
        subprocess.run(["bash", SYMBOLIC_LINK_COMMAND_FILE], check=True)
    except subprocess.CalledProcessError:
        pass


def refresh_symbolic_link_commands_file():
    save_leetcode_data(load_leetcode_data())
    generate_symbolic_link_commands()


# refresh_symbolic_link_commands_file()
add_leetcode_file()


# TODO right now the json file is like
#  "1. Two Sum": {
#      "difficulty": "easy",
#      "topics": [
#          "array",
#          "hash table"
#      ]
#  },
#  make it so it's like this
#  "1. Two Sum": {
#      "difficulty": "easy",
#      "topics": [
#          "array",
#          "hash table"
#      ],
#      "study_list" : [
#          "75_quick_study",
#          "favorites",
#          "good_to_review"
#      ]
#  },
#  for example
