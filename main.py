from pathlib import Path


def replace_hyphens_with_spaces(folder_path):
    folder_path = Path(folder_path)
    for folder in folder_path.iterdir():
        if folder.is_dir():
            for item in folder.iterdir():
                new_name = item.name.replace('-', ' ')
                new_path = item.with_name(new_name)
                item.rename(new_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    replace_hyphens_with_spaces('C:/Users/memad/Desktop/BatchOperation')
