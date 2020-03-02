from termcolor import colored
import os
import sys
import optparse
from collections import Counter

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
                for line in target_file.readlines():
                    line = line.replace('\n', '')

                    if any([line.startswith(x) for x in import_lines_prefixes]):
                        print(line)

                        if filepath not in imports_by_file:
                            imports_by_file[filepath] = []
                        imports_by_file[filepath].append(line)

    print(colored(' \n\n==================================== RESULTS ==================================== \n', 'yellow'))
    for filename, imports in imports_by_file.items():
        for import_name, count in Counter(imports).items():
            if count > 1:
                print('%s (%s)' % (
                    colored(f'{count}x imported "{import_name}"', 'red'),
                    filename))


if __name__ == '__main__':
    parser = optparse.OptionParser()
    (options, args) = parser.parse_args()

    if len(args) < 0:
        print(colored('Provide target directory as first arg!', 'red'))
        sys.exit(1)
    else:
        main(options, args[0])
        print()
