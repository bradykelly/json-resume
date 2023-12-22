import json
import sys
from json import JSONDecodeError
from typing import TypeVar

from errors.serializer_error import SerializerError

T = TypeVar('T')


def deserialize_json(json_string: str, json_key: str = None) -> T:
    """
    Deserializes a JSON string into a Python object.

    :param json_string: The JSON string to deserialize.
    :param json_key: The name of the key in the JSON string that holds the object to deserialize.
                        If None or empty, the entire JSON string will be deserialized.
    :return: The deserialized Python object.
    """
    try:
        data_object = json.loads(json_string)
    except json.decoder.JSONDecodeError as e:
        raise SerializerError(f"Error deserializing JSON: {e.msg}", e)
    if json_key is None or len(json_key) == 0:
        return data_object
    else:
        return data_object[json_key]


def serialize_json(data_object: T, indent_json: bool) -> str:
    """
    Serializes a Python object into a JSON string.

    :param indent_json:
    :param data_object: The Python object to serialize.
    :return: The serialized JSON string.
    """
    try:
        output_json: str = json.dumps(data_object, indent=2)
    except TypeError or OverflowError or JSONDecodeError as e:
        raise SerializerError(f"Error serializing JSON: {e.message}", e)
    return output_json
