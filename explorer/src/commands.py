from typing import List
from .filesystem import FileSystem
from .utils import format_error, search, top_n, bottom_n, pretty_print_tree, get_help

class CommandHandler:
    def __init__(self, fs: FileSystem):
        self.fs = fs

    def execute(self, tokens: List[str]) -> str:
        if not tokens:
            return format_error("No command given.")

        cmd, *args = tokens

        try:
            if cmd == 'cr':
                name = args[0]
                is_dir = '-d' in args
                return self.fs.create(name, is_dir)

            elif cmd == 'dl':
                name = args[0]
                return self.fs.delete(name)

            elif cmd == 'cd':
                name = args[0] if args else None
                return self.fs.change_dir(name)

            elif cmd == 'lc':
                return self.fs.get_cwd()

            elif cmd == 'rd':
                name = args[0]
                lines = int(args[1]) if len(args) > 1 else None
                content = self.fs.read_file(name, lines)
                return '\n'.join(content) if isinstance(content, list) else content

            elif cmd == 'wr':
                name = args[0]
                content = args[1]
                append = '-a' in args
                return self.fs.write_file(name, content, append)

            elif cmd == 'fd':
                name = args[0]
                is_dir = '-d' in args
                results = search(self.fs.current_dir, name, is_dir)
                return '\n'.join(results) if results else "No matches found."

            elif cmd == 'tp':
                n = int(args[0]) if args and args[0].isdigit() else 1
                by_date = '-d' in args
                results = top_n(self.fs.current_dir, n, by_date)
                return '\n'.join(results)

            elif cmd == 'bt':
                n = int(args[0]) if args and args[0].isdigit() else 1
                by_date = '-d' in args
                results = bottom_n(self.fs.current_dir, n, by_date)
                return '\n'.join(results)

            elif cmd == 'ls':
                path = args[0] if args else None
                return '\n'.join(self.fs.list_dir(path))

            elif cmd == 'tr':
                path = args[0] if args else None
                node = self.fs._resolve_path(path) if path else self.fs.current_dir
                if not node or node.type != 'directory':
                    return format_error("Invalid directory for tree.")
                return '\n'.join(pretty_print_tree(node))

            elif cmd == 'hp':
                target = args[0] if args else None
                return get_help(target)

            elif cmd == 'ex':
                if '!' not in args:
                    self.fs.save_state()
                print("Goodbye!")
                exit(0)

            else:
                return format_error(f"Unknown command: {cmd}")

        except IndexError:
            return format_error("Missing argument(s).")
        except ValueError:
            return format_error("Invalid argument type.")
        except Exception as e:
            return format_error(str(e))
