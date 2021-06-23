import os


def change_dir(path, autocreate=True):
    """Change current directory of app.

    Args:
        path (str): Path to working directory with files.
        autocreate (bool): Create folder if it doesn't exist.

    Raises:
        RuntimeError: if directory does not exist and autocreate is False.
    """

    if autocreate and not os.path.exists(path):
        os.makedirs(path)

    if not os.path.exists(path):
        raise RuntimeError("The directory {} does not exist".format(path))

    try:
        os.chdir(path)
    except RuntimeError as e:
        print("Error: " + str(e))


def get_files(path):
    """Get info about all files in working directory.

    Returns:
        List of dicts, which contains info about each file. Keys:
        - name (str): filename
        - create_date (datetime): date of file creation.
        - edit_date (datetime): date of last file modification.
        - size (int): size of file in bytes.
    """

    # change_dir(path, autocreate=False)
    # os.listdir(path='.')
    files_info = []
    _, _, files = next(os.walk(path))

    for one_file in files:
        files_info.append(get_file_data(one_file))

    return files_info


def get_file_data(filename):
    """Get full info about file.

    Args:
        filename (str): Filename.

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
    with open(filename) as f:
        file_content = f.read()
    info_dict = {'name': filename,
                 'content': file_content,
                 'create_date': os.path.getctime(filename),
                 'edit_date': os.path.getmtime(filename),
                 'size': os.path.getsize(filename)}

    return info_dict


def create_file(filename, content=None):
    """Create a new file.

    Args:
        filename (str): Filename.
        content (str): String with file content.

    Returns:
        Dict, which contains name of created file. Keys:
        - name (str): filename
        - content (str): file content
        - create_date (datetime): date of file creation
        - size (int): size of file in bytes

    Raises:
        ValueError: if filename is invalid.
    """

    with open(filename, "w") as f:
        f.write(content)


def delete_file(filename):
    """Delete file.

    Args:
        filename (str): filename

    Raises:
        RuntimeError: if file does not exist.
        ValueError: if filename is invalid.
    """

    try:
        os.path.isfile(filename)
    except RuntimeError:
        print("{} does not exists or not a file".format(filename))
    os.remove(filename)
