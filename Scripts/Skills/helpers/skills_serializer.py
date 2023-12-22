import sys
from typing import List

from helpers.json_serializer import deserialize_json, serialize_json
from models.skills import Skills

from errors.serializer_error import SerializerError


class SkillsSerializer:
    JSON_KEY = 'skills'

    def __init__(self, skills: List[str]):
        """
        Initializes a SkillsSerializer object.

        :param skills: A list of strings representing skill names.
        :type skills: List[str]
        """
        assert isinstance(skills, list)
        self.skills = skills

    @classmethod
    def deserialize_skills(cls, skills_json: str = None) -> Skills:
        """
        Takes a JSON string and returns a list of strings representing skill names.

        :param skills_json: A JSON string representing a skills object.
        :return: A list of strings representing skill names.
        :rtype: List[str]
        """

        assert isinstance(skills_json, str)

        if (skills_json is not None) and (len(skills_json) > 1):
            skills_object: List[str] = deserialize_json(skills_json, cls.JSON_KEY)
            skills_model: Skills = Skills(skills_object)
            return skills_model
        else:
            raise ValueError("No JSON string provided for 'skills_js' parameter.")

    @classmethod
    def serialize_skills(cls, skills_model: Skills) -> str:
        """
        Serializes a Skills object into a JSON string.

        :param skills_model: The Skills object to serialize.
        :return: The serialized JSON string representing the Skills object.
        :raises SerializerError: If an error occurs during serialization.
        """
        assert isinstance(skills_model, Skills)
        try:
            s_json = serialize_json(skills_model)
        except SerializerError as e:
            sys.stderr.write(f"Error serializing skills: {e.msg}\n")
            sys.exit(1)
        return s_json
