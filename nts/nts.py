#! /usr/bin/env python3

from nts.argument_parse import collect
import toml
import os
import json

class Config:
    def __init__(self, args_file):
        self.args = os.path.dirname(__file__) + '/../' + args_file
        self.file_path = os.path.expanduser(collect.Arguments(self.args).value("config"))
        self.journal = collect.Arguments(self.args).value("journal")
        self.debug = collect.Arguments(self.args).value("debug")
        self.action = collect.Arguments(self.args).value("action")
        self.list = collect.Arguments(self.args).value("list")
        try:
            self.storage_path = os.path.dirname(os.path.dirname(toml.load(self.file_path).get(self.journal).get("journal_path")))
        except AttributeError:
            self.storage_path = os.path.expanduser("~/.local/share/nts")
        self.notebody = collect.Arguments(self.args).value("notebody")
        self.subject = collect.Arguments(self.args).value("subject")
        try:
            self.default_subject = toml.load(self.file_path).get(self.journal).get("default_subject")
        except AttributeError:
            self.default_subject = None
        try:
            self.time_format = toml.load(self.file_path).get(self.journal).get(
                "time_format", "%m/%d/%Y, %H:%M:%S")
        except AttributeError:
            self.time_format = "%m/%d/%Y, %H:%M:%S"


    def values(self):
        return toml.load(self.file_path)


def check_for_configuration(config):
    if os.path.isfile(config.file_path):
        return config.values()
    else:
        default_journal_path = "{}/default/journal.json".format(config.storage_path)
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

def check_for_journal(journal):
    journal_path = journal.get("journal_path", "")
    if os.path.isfile(journal_path):
        return True
    else:
        print("Creating journal at {}".format(journal_path))
        try:
            os.makedirs(os.path.dirname(journal_path))
        except FileExistsError:
            pass
        blank_journal = {"posts": []}
        with open(journal_path, "w") as journal_file:
            journal_file.write(json.dumps(blank_journal))
        return True

def run_cli(args):
    config_set = check_for_configuration(args)
    if config_set.get(args.journal):
        if args.debug:
            debug_output(config_set, args)
        journal_check = check_for_journal(config_set.get(args.journal))
        if journal_check:
            return [journal_check, 0]
        else:
            print("Error creating journal at {}".format(args.journal))
            return False
    else:
        print("Journal not found: {}".format(args.journal))
        return False


def add_notebook(args):
    current_notebooks = toml.load(args.file_path)
    new_notebook = input("New notebook name: ? ")
    if new_notebook:
        current_notebooks[new_notebook] = {
            "journal_path": "{}/{}/journal.json".format(args.storage_path, new_notebook)}
    with open(args.file_path, "w") as config_file:
        config_file.write(toml.dumps(current_notebooks))
    return [0, 0]
