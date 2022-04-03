#! /usr/bin/env python3

from nts.argument_parse import collect
import os

def config(config_file):
    return collect.Arguments(os.path.dirname(__file__) + '/../' + config_file)
