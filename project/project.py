import click as CommandArgumentParser
from lol.prompt import Prompt


@CommandArgumentParser.command()
@CommandArgumentParser.argument('command', type=str)
def main(command):
    print("Under work")


if __name__ == "__main__":
    main()