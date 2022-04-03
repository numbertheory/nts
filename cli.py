#! /usr/bin/env python3
from nts import nts
import os


args = nts.Config("arguments.yaml")

def debug_output(config_set, args):
    print(config_set.get(args.journal))

def run_cli():
    config_set = nts.check_for_configuration(args)
    if config_set.get(args.journal):
        if args.debug:
            debug_output(config_set, args)
        journal_check = nts.check_for_journal(config_set.get(args.journal))
        if journal_check:
            return [journal_check, 0]
        else:
            return ["Error creating journal at {}".format(args.journal), 1]
    else:
        return ["Journal not found: {}".format(args.journal), 1]


if __name__ == "__main__":
    command = run_cli()
    print(command[0])
    exit(command[1])
