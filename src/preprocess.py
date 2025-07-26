# Removes comments
# Removes whitespace
# Packages all source files into one

import os

def preprocess(project):
    source_dir = os.path.normpath(os.path.dirname(project.path) + "/" + project.source_path)
    source_files = os.scandir(source_dir)

    # Combine source files into one giant string
    for source_file in source_files:
        file = open(source_file.path)
        project.source += file.read() + "\n"
        file.close()

    # Remove comments
    while project.source.__contains__("/*"):
        project.source = project.source.replace(project.source[project.source.find("/*"):project.source.find("*/", project.source.find("/*"))+2], "")

    while project.source.__contains__("//"):
        project.source = project.source.replace(project.source[project.source.find("//"):project.source.find("\n", project.source.find("//"))], "")

    # Remove whitespace
    iterator = project.source.splitlines()
    for line in iterator:
        project.source = project.source.replace(line, line.strip())
    project.source = project.source.replace("\n", "")
    while project.source.__contains__("  "):
        project.source = project.source.replace("  ", " ")
    project.source = project.source.replace(" (", "(")
    project.source = project.source.replace(") ", ")")

    print(project.source)
    return project