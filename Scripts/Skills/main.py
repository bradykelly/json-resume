import io
import os.path
import sys
from typing import List

from models.base_model import JsonResumeBaseModel
from models.skills import Skills


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main(args: List[str]) -> str | JsonResumeBaseModel:
    # TODD: Accept a command that determines which action to take
    pass


# TODO: Move to a SkillsEdit class
def deserialize_skills(skills_list: List[str]) -> Skills:
    # Convert a list of strings to a Skills object
    assert isinstance(skills_list, List)


# TODO: Move to a SkillsEdit class
def read_skills_json(json_path: object) -> List[str]:
    # Read a list of strings from the skills.json file
    if len(json_path) > 0 and os.path.isfile(json_path):
        try:
            with open(json_path, 'r') as file:
                skills_list: List[str] = file.readlines()
                return skills_list
        except IOError as e:
            print(f"Error reading skills file: {e}")
    else:
        raise FileNotFoundError(f"No skills file found at {json_path}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        # TODO: Check if usage syntax is correct
        print("Usage: python main.py [COMMAND <path>] [path]")
        sys.exit(1)
    json = read_skills_json(sys.args[1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
