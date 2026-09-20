import shutil
import os


def main()-> None:
    root_path = './static'
    copy_root_path = './public'
    remove_and_copy_files(root_path, copy_root_path)


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


if __name__ == "__main__":
    main()
