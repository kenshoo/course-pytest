from tempfile import mkdtemp
from os import path


def generate_file(name, contents):    
    full_path = path.join(_create_temp_dir(), name)

    with open(full_path, 'w') as f:
        f.write(contents)

    return full_path


def _create_temp_dir():
    dir_path = mkdtemp()
    return dir_path
