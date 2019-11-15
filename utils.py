import os
from typing import Set, Dict, List
import fnmatch

def get_insides(path) -> List[str]:
    insides = list()
    first = True
    for dir_info in os.walk(path):
        if first:
            first = False
        else:
            path_to_dir = dir_info[0]
            for file in dir_info[2]:
                insides.append(path_to_dir + "/" + file)
    return insides






def get_match_extension(file_names: Set[str], extension: str)-> Set[str]:
    matches = set()
    splitted_extension = extension.split('.')
    for file_name in file_names:
        splitted_file_name = file_name.split('.')
        if len(splitted_extension) == len(splitted_file_name):
            file_matches = fnmatch.filter([file_name],"*" + extension)
            if file_matches:
                matches.add(file_matches[0])
    return matches


def get_match_extensions(file_names: Set[str], extensions: List[str])-> Set[str]:
    matches = set()
    for extension in extensions:
        matche = get_match_extension(file_names, extension)
        matches.update(matche)
    return matches

def get_match_by_full_paths(full_paths: List[str], extension: str)-> List[str]:
    # matches = set()
    # splitted_extension = extension.split('.')
    # for file_name in full_paths:
    # splitted_file_name = file_name.split('.')
        # if len(splitted_extension) == len(splitted_file_name):
    file_matches = fnmatch.filter(full_paths , extension)
    # if file_matches:
    #     matches.add(file_matches)
    return file_matches


# def get_match_extensions(file_names: Set[str], extensions: List[str])-> Set[str]:
#     matches = set()
#     for extension in extensions:
#         matche = get_match_extension(file_names, extension)
#         matches.update(matche)
#     return matches

