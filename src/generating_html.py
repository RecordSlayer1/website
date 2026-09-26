import os
import shutil

from pathlib import Path

from markdown_blocks import markdown_to_html_node, extract_title

def remove_and_copy_files(root_path: str, copy_root_path: str)-> None:
    if os.path.exists(copy_root_path):
        shutil.rmtree(copy_root_path)
        print(f' - deleting folder "{copy_root_path}"...')
    os.mkdir(copy_root_path)
    print(f' - creating new folder "{copy_root_path}"...')

    if not os.path.exists(root_path):
        raise ValueError(f'root folder is missing "{root_path}"') 
    
    files = os.listdir(root_path)
    for file in files:
        target_file = os.path.join(root_path, file)
        copy_path = os.path.join(copy_root_path, file)
        if os.path.isfile(target_file):
            shutil.copy(target_file, copy_path)
            print(f' - making copy from "{target_file}" to "{copy_path}"...')
        else:
            remove_and_copy_files(target_file, copy_path)


def generate_page(from_path: str, template_path: str, dest_path: str)-> None:
    print(f' - generating page form {from_path} to {dest_path} using template {template_path}...')
    with open(from_path, 'r') as f:
        markdown_contents = f.read()
        f.close()
    with open(template_path, 'r') as f:
        template_contents = f.read()
        f.close()
    node = markdown_to_html_node(markdown_contents)
    content = node.to_html()
    title = extract_title(markdown_contents)
    page_contents = template_contents.replace('{{ Title }}', title).replace('{{ Content }}', content)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(page_contents)
        f.close()
    print(f' - finished generating page from {from_path} to {dest_path} using template {template_path}...')


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


