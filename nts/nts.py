#! /usr/bin/env python3

from nts.argument_parse import collect
import toml
import os

class Config:
    def __init__(self, config_file):
        self.args_file_path = os.path.dirname(__file__) + '/../' + config_file
        self.file_path = collect.Arguments(self.args_file_path).value("config")

    def values(self):
        return toml.load(os.path.expanduser(self.file_path))
