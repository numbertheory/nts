#! /usr/bin/env python3
# Handle argument parsing in one place
import argparse
import yaml
import os

def store_translate(default):
    if default:
        return "store_false"
    else:
        return "store_true"

class Arguments:
    def __init__(self, config):
        with open(os.path.dirname(__file__) + '/../' + config) as f:
            config_args = yaml.safe_load(f)
        self.parser = argparse.ArgumentParser(description=config_args.get("description"))
        self.arguments = config_args.get("arguments")
        for arg in self.arguments:
            if arg.get("type") == "string":
                type_of_argument = str
            if arg.get("type") == "integer":
                type_of_argument = int
            if arg.get("multiple"):
                nargs_value = "+"
            else:
                nargs_value = 1
            if arg.get("type") in ["string", "integer"]:
                self.parser.add_argument(
                    "-{}".format(arg.get("flags")[0]),
                    "--{}".format(arg.get("flags")[1]),
                    dest=arg.get("name"),
                    type=type_of_argument,
                    nargs=nargs_value,
                    required=arg.get("required")
                )
            if arg.get("type") == "boolean":
                self.parser.add_argument(
                    "-{}".format(arg.get("flags")[0]),
                    "--{}".format(arg.get("flags")[1]),
                    dest=arg.get("name"),
                    action=store_translate(arg.get("default")),
                    required=arg.get("required")
                )

    def value(self, dest):
        return getattr(self.parser.parse_args(), dest)
