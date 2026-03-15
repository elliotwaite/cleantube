"""Builds the extension for both Manifest V2 and V3."""

import os
import zipfile
import shutil
import tempfile

CUR_DIR = os.path.join(os.path.dirname(__file__))
EXTENSION_DIR = os.path.abspath(os.path.join(CUR_DIR, "extension"))
EXTENSION_V3_DIR = os.path.abspath(os.path.join(CUR_DIR, "extension-files-for-manifest-version-3"))
BUILD_DIR = os.path.abspath(os.path.join(CUR_DIR, "build"))
PACKAGE_V2_PATH = os.path.abspath(os.path.join(BUILD_DIR, "cleantube-v2.zip"))
PACKAGE_V3_PATH = os.path.abspath(os.path.join(BUILD_DIR, "cleantube-v3.zip"))
EXCLUDED_FILENAMES = [".DS_Store"]


def create_temp_dir_with_overrides(source_dir, override_dir):
    """Create a temporary directory with files from source_dir, overridden by files from override_dir."""
    temp_dir = tempfile.mkdtemp()
    
    # First, copy all files from source_dir.
    print(f"Copying base files from {source_dir}")
    for dir_path, dir_names, filenames in os.walk(source_dir):
        for filename in filenames:
            source_path = os.path.join(dir_path, filename)
            relative_path = os.path.relpath(source_path, source_dir)
            target_path = os.path.join(temp_dir, relative_path)
            
            # Create target directory if it doesn't exist.
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            
            # Copy the file.
            shutil.copy2(source_path, target_path)
            print(f"  Copied: {relative_path}")
    
    # Then, apply overrides from override_dir.
    print(f"\nApplying overrides from {override_dir}")
    for dir_path, dir_names, filenames in os.walk(override_dir):
        for filename in filenames:
            override_path = os.path.join(dir_path, filename)
            relative_path = os.path.relpath(override_path, override_dir)
            target_path = os.path.join(temp_dir, relative_path)
            
            # Create target directory if it doesn't exist.
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            
            # Copy the override file.
            shutil.copy2(override_path, target_path)
            print(f"  Overrode: {relative_path}")
    
    return temp_dir


def zip_dir(source_dir, output_path, excluded_filenames=None):
    """Create a zip file from the source directory."""
    if not excluded_filenames:
        excluded_filenames = []
    
    print(f"Zip source path: {source_dir}")
    print(f"Zip output path: {output_path}")
    print("Zipped files:")
    
    with zipfile.ZipFile(output_path, "w") as z:
        for dir_path, dir_names, filenames in os.walk(source_dir):
            for filename in filenames:
                if filename not in excluded_filenames:
                    path = os.path.join(dir_path, filename)
                    path_in_zip = path[len(source_dir):]
                    print(f"  {path_in_zip}")
                    z.write(path, path_in_zip)
    
    print()


def main():
    # Create build directory.
    os.makedirs(BUILD_DIR, exist_ok=True)
    
    # Build Manifest V2 version (default).
    print("\nBuilding Manifest V2 version...")
    zip_dir(EXTENSION_DIR, PACKAGE_V2_PATH, EXCLUDED_FILENAMES)
    
    # Build Manifest V3 version (with overrides).
    print("\nBuilding Manifest V3 version...")
    # Create a temporary directory with V3 overrides.
    temp_v3_dir = create_temp_dir_with_overrides(EXTENSION_DIR, EXTENSION_V3_DIR)
    try:
        # Zip the temporary directory.
        zip_dir(temp_v3_dir, PACKAGE_V3_PATH, EXCLUDED_FILENAMES)
    finally:
        # Clean up the temporary directory.
        shutil.rmtree(temp_v3_dir)
    
    print("\nBuild completed!")
    print(f"Manifest V2 package: {PACKAGE_V2_PATH}")
    print(f"Manifest V3 package: {PACKAGE_V3_PATH}")


if __name__ == "__main__":
    main()
