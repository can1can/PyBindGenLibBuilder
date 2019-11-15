#!/usr/bin/env python
import os
import sys
from distutils.core import setup, Extension
from typing import List

import pybindgen

from utils import get_insides, get_match_by_full_paths


class Builder:
    def __init__(self, path_to_c_files, lib_name, source_h ="src/*.h", source_c = "src/*.cpp", path_to_save = "./"):
        self.path_to_c_files = path_to_c_files
        self.lib_name = lib_name
        self.type = ".cpp" if source_c.endswith(".cpp") else ".c"
        self.source_h = source_h
        self.source_c = source_c
        self.path_to_save = path_to_save + "build" if path_to_save.endswith('/') else path_to_save + "/build"
        self.mod = pybindgen.Module(self.lib_name)

    def build(self):
        insides = get_insides(self.path_to_c_files)
        h_match = get_match_by_full_paths(insides, self.path_to_c_files + "/" + self.source_h)
        c_match = get_match_by_full_paths(insides, self.path_to_c_files + "/" + self.source_c)

        try:
            os.mkdir(self.path_to_save)
        except OSError:
            pass
        module_fname = os.path.join(self.path_to_save, self.lib_name + "-binding" + self.type)
        with open(module_fname, "wt") as file_:
            print("Generating file {}".format(module_fname))
            self.add_include(h_match)
            self.add_func("MyModuleDoAction", "int", [])
            self.add_func("printer", "void", [])
            #  add func you wont to get in lib
            self.mod.generate(file_)

        module = self.get_module(module_fname, c_match)

        setup(name=self.lib_name + "^^",
              version="0.0",
              author='xxx',
              author_email='yyy@zz',
              ext_modules=[module],
              script_args = ["build"]
             )

    def get_module(self, module_fname, c_matchs:List[str]):
        sources = c_matchs
        print(sources)
        sources.append(module_fname)
        module = Extension(self.lib_name,
                             sources=sources,
                             include_dirs=['.'])
        return module


    def add_include(self, h_match:List[str]):
        for h in h_match:
            self.mod.add_include(f'"{h}"')

    def add_func(self, func_name: str, return_type: str, args_type: List[str]):
        self.mod.add_function(func_name, return_type, args_type)


path = "/home/ivan/workspace/projects/cpp/tests/PyBindTest"
a = Builder(path,"test_lib")
a.build()