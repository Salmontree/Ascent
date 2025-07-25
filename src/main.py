# TODO: Loads the raw project data into a Project class, then runs it through the pipeline.

from re import sub
import toml
import sys
import os

class Project:
    def __init__(self) -> None:
        self.name = "Test"
        self.description = "Description"
        self.authors: tuple[str] = ("Me!",)
        self.version = "0.1"
        self.data_format = "80" # 1.21.7
        self.res_format = "60"  # 1.21.7

        self.source_path = "src"
        self.output_path = ""

        self.source = ""

##############
# Load project
##############

# Make sure arguments are valid
if len(sys.argv) != 2: print("ERROR: Invalid amount of arguments, 1 must be passed"); sys.exit(1)
if not (os.path.exists(sys.argv[1]) and os.path.isfile(sys.argv[1])): print("ERROR: Couldn't find project"); sys.exit(1)

# Put .mcproject data into Project class
project = Project()
toml_project = toml.load(open(sys.argv[1]))
try:
    project.name = toml_project["project"]["name"]
    project.description = toml_project["project"]["description"]
    project.authors = tuple(toml_project["project"]["authors"])
    project.version = toml_project["project"]["version"]
    project.output_path = toml_project["minecraft"]["output_path"]
except KeyError: pass

# Default values
if project.output_path == "": project.output_path = "../" + project.name + " Datapack"

# Convert to kebab-case, will need this for later
# '-'.join(sub(r"(\s|_|-)+"," ", sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+", lambda mo: ' ' + mo.group(0).lower(), project.name)).split())

print(project.__dict__)