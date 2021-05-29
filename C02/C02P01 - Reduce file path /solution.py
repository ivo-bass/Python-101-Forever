ROOT = "/"
EMPTY = ""
CURRENT = "."
PARENT = ".."
PATHS_TO_SKIP = (EMPTY, CURRENT, PARENT)


def reduce_file_path(path):
    dirs = path.split("/")
    new_path = []

    for directory in dirs:
        if directory not in PATHS_TO_SKIP:
            new_path.append(directory)
        if directory == PARENT and new_path:
            new_path.pop()

    return ROOT + "/".join(new_path)


def reduce_file_path_2(path):
    # Defensive programing solution

    dirs = path.split("/")
    new_path = []

    for directory in dirs:
        if directory == CURRENT or not directory:
            continue
        if directory == PARENT:
            if new_path:
                new_path.pop()
            continue
        new_path.append(directory)

    return ROOT + "/".join(new_path)


tests = [
    reduce_file_path("/") == "/",
    reduce_file_path("/srv/../") == "/",
    reduce_file_path("/srv/www/htdocs/wtf/") == "/srv/www/htdocs/wtf",
    reduce_file_path("/srv/www/htdocs/wtf") == "/srv/www/htdocs/wtf",
    reduce_file_path("/srv/./././././") == "/srv",
    reduce_file_path("/etc//wtf/") == "/etc/wtf",
    reduce_file_path("/etc/../etc/../etc/../") == "/",
    reduce_file_path("//////////////") == "/",
    reduce_file_path("/../") == "/",
]

for test in tests:
    print(test)
