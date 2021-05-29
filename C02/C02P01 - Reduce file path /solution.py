ROOT = "/"
CURRENT = "."
PARENT = ".."


def reduce_file_path(path):
    # Split will leave empty strings in the list
    # so we need to skip them later
    dirs = path.split("/")
    new_path_list = []

    for directory in dirs:
        if directory == CURRENT or not directory:
            continue
        if directory == PARENT:
            if new_path_list:
                new_path_list.pop()
            continue
        new_path_list.append(directory)

    return ROOT + "/".join(new_path_list)



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
