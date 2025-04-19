import json
import os
import subprocess
import urllib.parse

JSON_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "leetcode_data.json"))
ALL_LEETCODE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../all_leetcode"))
SYMBOLIC_LINK_COMMAND_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../support/symbolic_link_commands.sh"))
README_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../README.md"))


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
    tags = input("What tags separated by commas? (ex. 'array, hash table, 2d dynamic programming'): ")
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


def update_readme_file():
    generate_readme_markdown()


# update_readme_file()
add_leetcode_file()


def create_markdown_link(leetcode_name):
    """Creates a relative Markdown link to the solution file, handling spaces."""
    # Ensure the file has a .py extension for the path
    file_name = leetcode_name + ".py"
    # Construct the relative path
    relative_path = os.path.join("all_leetcode", file_name).replace("\\", "/")  # Ensure forward slashes
    # URL-encode the path to handle spaces and special characters safely in links
    encoded_path = urllib.parse.quote(relative_path)
    # Create the Markdown link: [display name](path)
    return f"[{leetcode_name}]({encoded_path})"


def generate_readme_markdown(leetcode_data):
    """Generates Markdown content listing LeetCode problems by difficulty and topic."""
    if not leetcode_data:
        return "# LeetCode Solutions\n\nNo solutions added yet."

    # --- Group problems by difficulty ---
    problems_by_difficulty = {"easy": [], "medium": [], "hard": []}
    all_topics = set()

    for name, details in leetcode_data.items():
        difficulty = details.get("difficulty", "unknown").lower()
        topics = details.get("topics", [])
        link = create_markdown_link(name)
        topic_str = f"(Topics: {', '.join(topics)})" if topics else ""
        markdown_line = f"- {link} {topic_str}"

        if difficulty in problems_by_difficulty:
            problems_by_difficulty[difficulty].append(markdown_line)
        else:
            # Handle potential unknown difficulties if JSON data is inconsistent
            if "unknown" not in problems_by_difficulty:
                problems_by_difficulty["unknown"] = []
            problems_by_difficulty["unknown"].append(markdown_line)

        for topic in topics:
            all_topics.add(topic)

    # --- Group problems by topic ---
    problems_by_topic = {topic: [] for topic in all_topics}
    for name, details in leetcode_data.items():
        difficulty = details.get("difficulty", "Unknown").capitalize()
        topics = details.get("topics", [])
        link = create_markdown_link(name)
        markdown_line = f"- {link} (Difficulty: {difficulty})"  # Show difficulty when grouped by topic

        for topic in topics:
            if topic in problems_by_topic:
                problems_by_topic[topic].append(markdown_line)

    # --- Assemble the Markdown string ---
    markdown_content = ["# LeetCode Solutions"]

    # Add Difficulty Section
    markdown_content.append("\n## Problems by Difficulty")
    # Add problems ensuring consistent order (Easy, Medium, Hard, then others)
    for difficulty in ["easy", "medium", "hard"]:
        if problems_by_difficulty.get(difficulty):
            markdown_content.append(f"\n### {difficulty.capitalize()}")
            markdown_content.extend(sorted(problems_by_difficulty[difficulty]))  # Sort alphabetically by name

    # Add any other difficulties found (e.g., "unknown")
    for difficulty, problems in problems_by_difficulty.items():
        if difficulty not in ["easy", "medium", "hard"] and problems:
            markdown_content.append(f"\n### {difficulty.capitalize()}")
            markdown_content.extend(sorted(problems))  # Sort alphabetically

    # Add Topic Section
    markdown_content.append("\n## Problems by Topic")
    if not problems_by_topic:
        markdown_content.append("\n*No topics assigned yet.*")
    else:
        # Add problems for each topic, sorted alphabetically
        for topic in sorted(list(all_topics)):  # Sort topics alphabetically
            if problems_by_topic.get(topic):
                markdown_content.append(f"\n### {topic.capitalize()}")
                markdown_content.extend(sorted(problems_by_topic[topic]))  # Sort problems alphabetically

    return "\n".join(markdown_content)
