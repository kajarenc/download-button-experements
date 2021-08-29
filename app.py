import io
import os

import streamlit as st

from pathlib import Path
from zipfile import ZipFile


def get_all_file_paths(directory_path):
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory_path):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


def main():
    x = st.slider("Slider for interactivity", 0, 100, 55)
    st.write(x)

    zip_buffer = io.BytesIO()

    generate_zip_file_clicked = st.button("Generate ZIP file")

    if generate_zip_file_clicked:
        # path to folder which needs to be zipped
        directory_path = Path("files_for_zipping")

        # calling function to get all file paths in the directory
        file_paths = get_all_file_paths(directory_path)

        # printing the list of all files to be zipped
        print('Following files will be zipped:')
        for file_name in file_paths:
            print(file_name)

        # writing files to a zipfile
        with ZipFile(zip_buffer, 'w') as zip_file:
            # writing each file one by one
            for file in file_paths:
                zip_file.write(file)

        print('All files zipped successfully!')

        st.download_button("Download ZIP file!", zip_buffer, "my_archive.zip")


if __name__ == "__main__":
    main()

