from pathlib import Path


class FileTreeGenerator:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir).resolve()
        self.ignored_dirs = {
            '__pycache__', '.git', '.idea', 'venv', '.venv', 'env',
            '.vscode', 'assets', 'static', 'templates', 'node_modules', 'instance'
        }
        self.ignored_files = {'*.pyc', '*.pyo', '*.pyd', '.DS_Store'}
        self.max_depth = 20
        self.show_hidden = False

    def should_ignore(self, path):
        name = path.name
        if not self.show_hidden and name.startswith('.'):
            return True
        if path.is_dir() and name in self.ignored_dirs:
            return True
        if path.is_file() and any(name.endswith(ext) for ext in self.ignored_files):
            return True
        return False

    def build_tree(self, directory=None, prefix=''):
        if directory is None:
            directory = self.root_dir

        contents = []
        try:
            contents = sorted(
                [item for item in directory.iterdir() if not self.should_ignore(item)],
                key=lambda x: (not x.is_dir(), x.name.lower())
            )
        except PermissionError:
            pass

        for index, path in enumerate(contents):
            is_last = index == len(contents) - 1

            # Current item prefix
            if is_last:
                connector = '└── '
                new_prefix = prefix + '    '
            else:
                connector = '├── '
                new_prefix = prefix + '│   '

            print(f"{prefix}{connector}{path.name}")

            # Recursively process directories
            if path.is_dir():
                self.build_tree(path, new_prefix)

    def generate(self):
        if not self.root_dir.exists():
            print(f"Error: Path '{self.root_dir}' does not exist")
            return

        print(f"File Tree for: {self.root_dir}")
        print(".")
        self.build_tree()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Generate visual file tree structure.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('path', type=str, help='Root directory to scan')
    parser.add_argument('--hidden', action='store_true', help='Show hidden files/directories')
    args = parser.parse_args()

    generator = FileTreeGenerator(args.path)
    generator.show_hidden = args.hidden
    generator.generate()
