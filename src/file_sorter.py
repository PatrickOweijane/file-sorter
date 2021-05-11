from pathlib import Path


def group_files_by_suffix(path: Path, excluded_suffix: set={'.ini', '.lnk'}):
    '''
    This function returns a dictionary that groups different files
    together depending on their suffix.
    This function if NOT case sensitive. Example: .docx and .DOCX are
    treated the same way.
    '''
    excluded_suffix = set(map(lambda string: string.lower(), excluded_suffix))
    files = {}
    for p in path.iterdir():
        if p.is_file() and p.suffix.lower() not in excluded_suffix:
            suffix = p.suffix.lower()
            if suffix in files:
                files[suffix].append(p)
            else:
                files[suffix] = [p]
    return files


def file_sorter(path: Path):
    '''
    Takes a path 
    Returns a list of files that have not been moved
    because their new directories already exist.
    '''
    # Group all files in path by suffix
    files = group_files_by_suffix(path)

    # Iterate through files by group and move them to the correct folder
    files_not_moved = []
    for suffix, grouped_files in files.items():
        curr_dir = path / Path(suffix)
        (curr_dir).mkdir(exist_ok=True)
        for f in grouped_files:
            if (curr_dir / f.name).exists():
                files_not_moved.append(f.name)
            else:
                f.rename(curr_dir / f.name)
    return files_not_moved
        

if __name__ == '__main__':
    PATH = Path(r'C:\Users\patri\Desktop')
    files_not_moved = file_sorter(PATH)
    if files_not_moved:
        print('The files below have not been moved:')
        print('\t', end='')
        print('\n\t'.join(files_not_moved))
