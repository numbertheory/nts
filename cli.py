from nts import nts
import os


args = nts.Config("arguments.yaml")

def run_cli():
    config_set = nts.check_for_configuration(args)
    if config_set.get(args.journal):
        if args.debug:
            print(config_set.get(args.journal))
        return [nts.check_for_journal(config_set.get(args.journal)), 0]
    else:
        return ["Journal not found: {}".format(args.journal), 1]


if __name__ == "__main__":
    command = run_cli()
    print(command[0])
    exit(command[1])
