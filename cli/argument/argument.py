
# the main argument executor
# for executing the commands

class ArgumentParser():
    def __init__(self, command, name):
        self.command = command
        self.parameter = name

        print(f"Params = {self.command}")