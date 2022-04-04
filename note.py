#! /usr/bin/env python3
from nts import nts, journal
import os


args = nts.Config("arguments.yaml")

def debug_output(config_set, args):
    print(config_set.get(args.journal))

if __name__ == "__main__":
    command = nts.run_cli(args)
    if not command:
        exit(1)
    if args.notebody:
        print("Adding to {}".format(args.journal))
        command = journal.add(args)
    if command:
        exit(0)
    else:
        exit(1)
