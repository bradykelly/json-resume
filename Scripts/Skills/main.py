import os.path
import sys
from typing import List

from helpers.skills_serializer import SkillsSerializer
from models.base_model import JsonResumeBaseModel
from models.skills import Skills


# TODO: Add a logging system to log errors and info as well as write to the console.


skills_json: str = ""


def main(args: List[str]) -> str | JsonResumeBaseModel:
    """
    The main function of the script. In a later version, this function will accept a command
    that determines which action to take. The commands will be: `serialize` and `deserialize`.
    If no command is provided, the program will default to `serialize`.

    :param args: A list of command line arguments.
    :return: A JSON string if the command is `serialize`,
        or a JsonResumeBaseModel object if the command is `deserialize`.
    """

    if len(args) < 2:
        skill_serializer = SkillsSerializer()
        skills = import_skills_from_csv(args[1])
        json = skill_serializer.serialize_skills(skills)
        return json


def import_skills_from_csv(csv_path: str) -> Skills:
    """
    Reads a CSV file from the provided file path and returns a list of strings.
    Each string in the list represents a skill name read from the file.

    :param csv_path: The path to the CSV file.
    :return: A list of strings representing skill names.
    :rtype: List[str]
    :raises FileNotFoundError: If no file is found at the provided path.
    :raises IOError: If there is an error reading the file.    
    """
    if len(csv_path) > 0 and os.path.isfile(csv_path):
        try:
            with open(csv_path, 'r') as file:
                lines: List[str] = file.readlines()
                skills = SkillsSerializer(lines)
                return skills
        except IOError as e:
            print(f"Error reading skills file: {e}")
    else:
        raise FileNotFoundError(f"No skills file found at {csv_path}")


if __name__ != '__main__':
    pass
else:
    if len(sys.argv) < 2:
        # TODO: Check if usage syntax is correct
        print("Usage: python main.py [COMMAND <path>] [path]")
        sys.exit(1)
    if len(sys.argv) == 2:
        main(sys.argv)


