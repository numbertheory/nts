from nts import nts


config = nts.config("arguments.yaml")

print(config.value("config"))
