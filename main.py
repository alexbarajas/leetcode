import os
import re
import urllib.parse

# --- Configuration ---
ALL_LEETCODE_DIR = "all_leetcode"
DIFFICULTY_README_DIR = "leetcode_groups/difficulties"
TOPIC_README_DIR = "leetcode_groups/topics"


def extract_metadata(filepath):
    """Extracts metadata from the LeetCode solution file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(
            r'LeetCode Problem: (.*?)\nLink: (.*?)\nDifficulty: (.*?)\nTopics: (.*?)(?:\n|$)',
            content,
            re.DOTALL
        )
        if match:
            title = match.group(1).strip()
            link = match.group(2).strip()
            difficulty = match.group(3).strip().lower()
            topics_str = match.group(4).strip()
            topics = [topic.strip().lower().replace(" ", "_") for topic in topics_str.split(',') if topic.strip()]
            return {
                "title": title,
                "link": link,
                "difficulty": difficulty,
                "topics": topics,
                "filename": os.path.basename(filepath)
            }
    return None


def update_readme(directory, filename, entry):
    """Appends a new entry to the specified README file."""
    readme_path = os.path.join(directory, filename)
    with open(readme_path, 'a', encoding='utf-8') as f:
        f.write(entry)


def generate_markdown_entry(metadata, all_leetcode_dir="all_leetcode"):
    """Generates a problem title with LeetCode link, followed by repo links."""
    encoded_filename_py = urllib.parse.quote(f"{metadata['filename']}")
    repo_link_py = f"/all_leetcode/{encoded_filename_py}"

    # Check if a JavaScript file with the same base name exists
    base_name, ext = os.path.splitext(metadata['filename'])
    js_filename = f"{base_name}.js"
    encoded_filename_js = urllib.parse.quote(js_filename)
    repo_link_js = f"/all_leetcode/{encoded_filename_js}"
    js_exists = os.path.exists(os.path.join(all_leetcode_dir, js_filename))

    problem_number = metadata["title"].split(".")[0]
    problem_title = metadata["title"].split(".")[1].strip()

    entry = f"{problem_number}. [{problem_title}]({metadata['link']})\n"
    entry += f"  - [Python]({repo_link_py})\n"
    if js_exists:
        entry += f"  - JavaScript: [Repo]({repo_link_js})\n"
    return entry


if __name__ == "__main__":
    filepath = os.path.join(ALL_LEETCODE_DIR, "1. Two Sum.py")
    metadata = extract_metadata(filepath)

    if metadata:
        print("Extracted Metadata:")
        print(metadata)  # Print the entire metadata dictionary

        markdown_entry = generate_markdown_entry(metadata)

        # Update Difficulty README
        difficulty_dir = os.path.join(DIFFICULTY_README_DIR, metadata["difficulty"])
        os.makedirs(difficulty_dir, exist_ok=True)  # Ensure directory exists
        update_readme(difficulty_dir, "README.md", markdown_entry)
        print(f"Added '{metadata['title']}' to '{difficulty_dir}/README.md'")

        # Update Topic READMEs
        for topic in metadata["topics"]:
            if topic:  # Ensure the topic string is not empty
                topic_dir = os.path.join(TOPIC_README_DIR, topic)
                os.makedirs(topic_dir, exist_ok=True)  # Ensure topic directory exists
                update_readme(topic_dir, "README.md", markdown_entry)
                print(f"Added '{metadata['title']}' to '{topic_dir}/README.md'")
            else:
                print(f"Warning: Encountered an empty topic for '{metadata['title']}'.")
    else:
        print(f"Could not extract metadata from '{filepath}'.")
