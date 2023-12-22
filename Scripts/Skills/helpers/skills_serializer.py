import sys
from typing import List

from errors.serializer_error import SerializerError
from json_serializer import deserialize_json, serialize_json
from models.skills import Skills


class SkillsSerializer:
    JSON_KEY = 'skills'

    @classmethod
    def deserialize_skills(cls, skills_json: str) -> Skills:
        """
        Takes a JSON string and returns a list of strings representing skill names.

        :param skills_json: A JSON string representing a skills object.
        :return: A list of strings representing skill names.
        :rtype: List[str]
        """
        assert isinstance(skills_json, str)

        skills_object: List[str] = deserialize_json(skills_json, cls.JSON_KEY)
        skills_model: Skills = Skills(skills_object)
        return skills_model

    @classmethod
    def serialize_skills(cls, skills_model: Skills) -> None:
        """
        Serializes a Skills object into a JSON string.

        :param skills_model: The Skills object to serialize.
        :return: The serialized JSON string representing the Skills object.
        :raises SerializerError: If an error occurs during serialization.
        """
        assert isinstance(skills_model, Skills)
        try:
            j_s = serialize_json(skills_model)
        except SerializerError as e:
            sys.stderr.write(f"Error serializing skills: {e.msg}\n")
            sys.exit(1)
        print(j_s)
