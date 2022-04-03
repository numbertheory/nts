#! /usr/bin/env python3
from nts import nts
import os


args = nts.Config("arguments.yaml")

def debug_output(config_set, args):
    print(config_set.get(args.journal))

if __name__ == "__main__":
    command = nts.run_cli(args)
    print(command[0])
    exit(command[1])
