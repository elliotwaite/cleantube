"""Builds the extension."""
import os
import zipfile

CUR_DIR = os.path.join(os.path.dirname(__file__))
EXTENSION_DIR = os.path.abspath(os.path.join(CUR_DIR, 'extension'))
BUILD_DIR = os.path.abspath(os.path.join(CUR_DIR, 'build'))
PACKAGE_PATH = os.path.abspath(os.path.join(BUILD_DIR, 'package.zip'))
EXCLUDED_FILENAMES = ['.DS_Store']


def zip_dir(source_dir, output_path, excluded_filenames=None):
    print(f'Zip source path: {source_dir}')
    print(f'Zip output path: {output_path}')
    print(f'Zipped files:')
    with zipfile.ZipFile(output_path, 'w') as z:
        for dir_path, dir_names, filenames in os.walk(source_dir):
            for filename in filenames:
                if filename not in excluded_filenames:
                    path = os.path.join(dir_path, filename)
                    path_in_zip = path[len(source_dir) :]
                    print(f'  {path_in_zip}')
                    z.write(path, path_in_zip)
    print()


def main():
    os.makedirs(BUILD_DIR, exist_ok=True)
    zip_dir(EXTENSION_DIR, PACKAGE_PATH, EXCLUDED_FILENAMES)


if __name__ == '__main__':
    main()
