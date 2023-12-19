# Represents the `skills` object in a resume.json format json file
import json


class Skill(json_resume):
    def __init__(self, name, level, keywords):
        self.name = name
        self.level = level
        self.keywords = keywords


class Skills:
    def __init__(self, skills):
        self.skills = [Skill(**skill) for skill in skills]

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data['skills'])
