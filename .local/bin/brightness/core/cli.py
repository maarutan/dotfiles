import sys
from argparse import ArgumentParser
from core.render import Render


class Cli:
    def __init__(self):
        self.render = Render()
        self.parser = ArgumentParser()
        self.parser.add_argument("--up", action="store_true", help="Increase volume")
        self.parser.add_argument("--down", action="store_true", help="Decrease volume")

    async def run(self):
        args = self.parser.parse_args()

        if args.up:
            await self.render.add_brightness("+")
        elif args.down:
            await self.render.add_brightness("-")
        else:
            self.parser.print_help()
            sys.exit(1)
