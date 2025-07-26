# TODO: Converts the processed source code into separate .mcfunction files (stored as strings!!)
# TODO: Sets flags for the create process to make advancements or predicates or tags or what have you.

def parse(project):
    # Put all functions into a list, which can be SORT OF easily compiled into .mcfunction files by reading instructions line by line
    project.functions = {}

    for char in project.source:
        print(char)

    return project