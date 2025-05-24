import sys
import shlex
from .filesystem import FileSystem
from .commands import CommandHandler

class Explorer:
    def __init__(self):
        self.fs = FileSystem()
        self.cmd_handler = CommandHandler(self.fs)

    def run(self):
        print("Welcome to EXPLORER. Type 'hp' for help. Use 'ex' to exit.")
        while True:
            try:
                cwd = self.fs.get_cwd()
                user_input = input(f"{cwd} >> ").strip()
                if not user_input:
                    continue
                tokens = shlex.split(user_input)
                output = self.cmd_handler.execute(tokens)
                if output:
                    print(output)
            except (EOFError, KeyboardInterrupt):
                print("\nUse 'ex' to exit cleanly.")
            except Exception as e:
                print(f"Unexpected error: {str(e)}")

if __name__ == '__main__':
    Explorer().run()
