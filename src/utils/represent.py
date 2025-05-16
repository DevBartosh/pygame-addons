from enum import Enum
from collections.abc import Collection, Callable
import hashlib
from typing import Any

import pygame


def get_hash(obj: Any) -> str:
    return hashlib.sha256(get_repr(obj).encode()).hexdigest()

def get_repr(obj: Any) -> str:
    converting_func: Callable[[Any], str] = str
    if isinstance(obj, pygame.Surface):
        converting_func = get_repr_surface
    elif isinstance(obj, list):
        converting_func = get_repr_list
    elif isinstance(obj, set):
        converting_func = get_repr_set
    elif isinstance(obj, tuple):
        converting_func = get_repr_tuple
    elif isinstance(obj, dict):
        converting_func = get_repr_dict
    elif isinstance(obj, Enum):
        converting_func = get_repr_enum
    elif hasattr(obj, "__dict__"):
        converting_func = get_repr_object
    
    return converting_func(obj)

def get_repr_object(obj: Any) -> str:
    repr_string = f"{obj.__class__.__name__}("
    repr_string += ", ".join(map(lambda kvp: f"{kvp[0]}={get_repr(kvp[1])}", obj.__dict__.items()))
    repr_string += ")"

    return repr_string

def get_repr_enum(obj: Enum):
    return f"{obj.__class__.__name__}.{obj.name}"

def get_repr_surface(surface: pygame.Surface) -> str:
    surface_bytes = pygame.image.tobytes(surface, "RGBA")
    return f"Surface({hashlib.sha256(surface_bytes).hexdigest()})"

def get_repr_dict(obj: dict) -> str:
    repr_string = "{"
    repr_string += ", ".join(map(lambda kvp: f"{kvp[0]}: {get_repr(kvp[1])}", obj.items()))
    repr_string += "}"

    return repr_string

def create_collection_repr(start: str, end: str, link: str) -> Callable[[Collection], str]:
    def repr_func(obj: Collection):
        return start + link.join(map(get_repr, obj)) + end
    return repr_func

get_repr_set: Callable[[set | frozenset], str] = create_collection_repr("{", "}", ", ")
get_repr_list: Callable[[list], str] = create_collection_repr("[", "]", ", ")
get_repr_tuple: Callable[[tuple], str] = create_collection_repr("(", ")", ", ")


