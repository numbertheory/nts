#! /usr/bin/env python3
from nts import nts
import os


args = nts.Config("arguments-init.yaml")

def debug_output(config_set, args):
    print(config_set.get(args.journal))

if __name__ == "__main__":
    command = nts.run_cli(args) # check for a config and create if needed
    if (args.action == "add"):
        command = nts.add_notebook(args)
    exit(command[1])
