from os import walk, path
from json import dumps
from sys import argv

GAMELOGIC_PATH = '/Users/stoevand/Workspace/gdk-integration/gamelogic'
NEW_VERSION = '5.148.0' + '.RELEASE'
MODULE_EXCEPTIONS = ["slots", "blackjack", "videopoker", "roulette", "three-card-brag", ]

GAMELOGIC_VERSION_ROW_AFTER_PARENT_STR = 3
GAMELOGIC_VERSION_ROW_AFTER_ARTIFACT_ID_STR = 3


def verbose_explain(file_name, line_num, old_line, new_line):
    obj_dict = {
        "file_name": file_name,
        "line_num": line_num,
        "old_line": old_line,
        "new_line": new_line,
    }

    return dumps(obj_dict, indent=4)


def module_exceptions():
    return [f"<artifactId>{m}</artifactId>" for m in MODULE_EXCEPTIONS]


def fix(line, new_content, dir_path, curr_file, i, internal_counter, update, gamelogic_version):
    if internal_counter == GAMELOGIC_VERSION_ROW_AFTER_PARENT_STR:
        if '<version>' in line:
            old_line = line.strip()
            new_line = f"<version>{gamelogic_version}</version>"
            new_content.append(f"\t\t{new_line}\n")
            update = False
            internal_counter = 0
            print(verbose_explain(path.join(dir_path, curr_file), i, old_line, new_line))
        else:
            new_content.append(line)
    else:
        new_content.append(line)

    if update:
        internal_counter += 1

    return internal_counter, update


def init():
    new_counter = []
    internal_counter = 0  # count new lines after "parent" str or after "artifactId" str
    update = False

    return new_counter, internal_counter, update


def traverse_and_update(gamelogic_version):
    for dir_path, dir_names, file_names in walk(GAMELOGIC_PATH):
        for curr_file in file_names:
            if curr_file.endswith(".xml"):

                with open(path.join(dir_path, curr_file), 'r') as file:

                    data = file.readlines()

                    new_content, internal_counter, update = init()

                    for i, line in enumerate(data):
                        if '<parent>' in line:
                            update = True
                        internal_counter, update = fix(line, new_content, dir_path, curr_file, i, internal_counter,
                                                       update, gamelogic_version)

                    updated_content = new_content
                    new_content, internal_counter, update = init()

                    for i, line in enumerate(updated_content):
                        if line.strip() in module_exceptions():
                            update = True
                        internal_counter, update = fix(line, new_content, dir_path, curr_file, i, internal_counter,
                                                       update, gamelogic_version)

                with open(path.join(dir_path, curr_file), 'w') as file:
                    file.writelines(new_content)


new_gamelogic_version = NEW_VERSION

if len(argv) > 0:
    try:
        new_gamelogic_version = argv[1]

        if not new_gamelogic_version.endswith('.RELEASE'):
            new_gamelogic_version = new_gamelogic_version + '.RELEASE'
    except IndexError as ie:
        pass

traverse_and_update(new_gamelogic_version)
