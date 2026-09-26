import shutil
import os
from generating_html import (
    remove_and_copy_files,
    generate_pages_recursive
    )

dir_path_static = './static'
dir_path_public = './public'
dir_path_content = './content'
template_path = './template.html'


def main()-> None:
    remove_and_copy_files(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
    print(' - starting server...')


if __name__ == "__main__":
    main()
