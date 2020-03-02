from termcolor import colored
import os
import sys
import optparse
from collections import Counter
from isort import SortImports


import_lines_prefixes = [
    'import ',
    'from '
]


def main(options, target_dir):
    imports_by_file = {}

    for root, dirs, files in os.walk(target_dir, topdown=False):
        for name in files:
            
            if not name.endswith('.py'):
                continue

            filepath = os.path.join(root, name)

            print(colored(f'\n{filepath}', 'green'))

            with open(filepath, 'r') as target_file:
                # https://github.com/timothycrosley/isort/wiki/isort-Settings
                sorter = SortImports(
                    file_contents=target_file.read(),
                    force_alphabetical_sort=True,
                    lines_after_imports=0,
                    lines_between_types=0
                )

                new_contents = sorter.output

            with open(filepath, 'w') as target_file:
                target_file.write(new_contents)

     
if __name__ == '__main__':
    parser = optparse.OptionParser()
    (options, args) = parser.parse_args()

    if len(args) < 0:
        print(colored('Provide target directory as first arg!', 'red'))
        sys.exit(1)
    else:
        main(options, args[0])
        print()
