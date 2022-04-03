from nts import nts
import os


args = nts.Config("arguments.yaml")

def run_cli():
    config_set = nts.check_for_configuration(args)
    if config_set.get(args.journal):
        return(config_set.get(args.journal))


if __name__ == "__main__":
    print(run_cli())
