#! /usr/bin/env python3

from nts.argument_parse import collect
import toml
import os

def config(config_file):
    config_file_path = collect.Arguments(os.path.dirname(__file__) + '/../' + config_file)
