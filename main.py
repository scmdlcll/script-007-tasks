#!/usr/bin/env python2


def commandline_parser():
    """Command line parser.

    Parse port and working directory parameters from command line.

    Returns:
        argparse.ArgumentParser
    """

    pass


def command_change_dir():
    """Change current directory of app.

    Raises:
        RuntimeError: if directory does not exist and autocreate is False.
    """

    pass


def command_get_files():
    """Get info about all files in working directory.

    Returns:
        List of dicts, which contains info about each file. Keys:
        - name (str): filename
        - create_date (datetime): date of file creation.
        - edit_date (datetime): date of last file modification.
        - size (int): size of file in bytes.
    """

    pass


def command_get_file_data():
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

    pass


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

    pass


def command_delete_file():
    """Delete file.

    Raises:
        RuntimeError: if file does not exist.
    """

    pass


def main():
    """Entry point of app.

    Get and parse command line parameters and configure web app.

    Command line options:
    -f --folder - working directory (absolute or relative path, default: current app folder).
    -h --help - help.
    """

    pass


if __name__ == '__main__':
    main()
