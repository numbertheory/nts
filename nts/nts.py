#! /usr/bin/env python3

from nts.argument_parse import collect
import toml
import os

class Config:
    def __init__(self, args_file):
        self.args = os.path.dirname(__file__) + '/../' + args_file
        self.file_path = os.path.expanduser(collect.Arguments(self.args).value("config"))
        self.journal = collect.Arguments(self.args).value("journal")

    def values(self):
        return toml.load(self.file_path)


def check_for_configuration(config):
    if os.path.isfile(config.file_path):
        return config.values()
    else:
        default_journal_path = os.path.expanduser("~/.local/share/nts/default/journal.json")
        default_toml = {"default": {"journal_path": "{}".format(default_journal_path)}}
        user_set_path = input("Set path for config: [{}] ?".format(config.file_path))
        if not user_set_path:
            user_set_path = config.file_path
        try:
            os.makedirs(os.path.dirname(user_set_path))
        except FileExistsError:
            pass
        with open(user_set_path, "w") as config_file:
            config_file.write(toml.dumps(default_toml))
            print("Configuration created.")
        return Config("arguments.yaml").values()
