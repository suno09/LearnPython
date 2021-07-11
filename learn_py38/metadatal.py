from importlib import metadata


print(metadata.version("pip"))
pip_metadata = metadata.metadata("pip")
print(list(pip_metadata))
