#!/usr/bin/env python2
import argparse
import os

from server.FileService import change_dir, create_file, delete_file, get_file_data, get_files


def commandline_parser():
    """Command line parser.

    Parse port and working directory parameters from command line.

    Returns:
        argparse.ArgumentParser
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', help="Files directory", default=os.getcwd())
    return parser


def command_change_dir(path, autocreate=True):
    """Change current directory of app.

    Raises:
        RuntimeError: if directory does not exist and autocreate is False.
    """

    change_dir(path, autocreate)


def command_get_files():
    """Get info about all files in working directory.

    Returns:
        List of dicts, which contains info about each file. Keys:
        - name (str): filename
        - create_date (datetime): date of file creation.
        - edit_date (datetime): date of last file modification.
        - size (int): size of file in bytes.
    """

    return get_files(os.getcwd())


def command_get_file_data(filename):
    """Get full info about file.

    Returns:
        Dict, which contains full info about file. Keys:
        - name (str): filename
        - content (str): file content
        - create_date (datetime): date of file creation
        - edit_date (datetime): date of last file modification
        - size (int): size of file in bytes

    Raises:
        RuntimeError: if file does not exist.
        ValueError: if filename is invalid.
    """

    return get_file_data(filename)


def command_create_file():
    """Create a new file.

    Returns:
        Dict, which contains name of created file. Keys:
        - name (str): filename
        - content (str): file content
        - create_date (datetime): date of file creation
        - size (int): size of file in bytes

    Raises:
        ValueError: if filename is invalid.
    """

    filename = raw_input("Enter file name: ")
    content = raw_input("Add file content: ")
    return create_file(filename, content)


def command_delete_file(filename):
    """Delete file.

    Raises:
        RuntimeError: if file does not exist.
    """

    delete_file(filename)


def main():
    """Entry point of app.

    Get and parse command line parameters and configure web app.

    Command line options:
    -f --folder - working directory (absolute or relative path, default: current app folder).
    -h --help - help.
    """

    parser = commandline_parser()
    params = parser.parse_args()
    work_dir = str(params.dir)
    command_change_dir(work_dir)

    print("Expected working directory: " + work_dir)

    while True:
        command = raw_input("Waiting for a command. For exit type 'exit': ")
        if command == 'create':
            command_create_file()
        elif command == 'list':
            command_get_files()
        elif command == 'get':
            command_get_files()
        elif command == 'delete':
            command_delete_file()
        elif command == 'exit':
            break
        else:
            print('Wrong command')


if __name__ == '__main__':
    main()
