# Represents the `skills` object in a resume.json format json file
import json


class Skill:
    def __init__(self, name, level, keywords):
        self.name = name
        self.level = level
        self.keywords = keywords


class Skills:
    def __init__(self, skills_json):
        skills = from_json(skills_json)
        self.skills = [Skill(**skill) for skill in skills]



