from nts import nts


config = nts.Config("arguments.yaml")

print(config.file_path)
print(config.values())
