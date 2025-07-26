# TODO: Removes comments
# TODO: Removes whitespace
# TODO: Packages all source files into one

import os

def preprocess(project):
    source_dir = os.path.normpath(os.path.dirname(project.path) + "/" + project.source_path)
    source_files = os.scandir(source_dir)

    # Combine source files into one giant string
    for source_file in source_files:
        file = open(source_file.path)
        project.source += file.read() + "\n"
        file.close()

    # Remove whitespace
    project.source = project.source.replace("    ", "\t")
    iterator = project.source.splitlines()
    for line in iterator:
        project.source = project.source.replace(line, line.lstrip(" ").rstrip(" \t"))

    print(project.source)
    return project