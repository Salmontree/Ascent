# TODO: Loads the raw project data into a Project class, then runs it through the pipeline.

from re import sub
import toml
import sys
import os

from preprocess import preprocess
from parse      import parse
from create     import create

class Project:
    def __init__(self) -> None:
        self.name = "Test"
        self.description = "Description"
        self.authors: tuple[str] = ("Me!",)
        self.version = "0.1"
        self.data_format = "80" # 1.21.7
        self.res_format = "60"  # 1.21.7
        
        self.path = ""
        self.source_path = "src"
        self.output_path = "" # default value is loaded later on in the script

        self.source = ""

########################################################
# Load project
########################################################

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
    project.source_path = toml_project["project"]["sourcepath"]
    project.output_path = toml_project["minecraft"]["outputpath"]
except KeyError: pass # .mcproject file didn't have those values but we don't wanna crash lol

# Default values
project.path = sys.argv[1]
if project.output_path == "": project.output_path = "../" + project.name + " Datapack"

########################################################
# Put the project through the pipeline (the main event!)
########################################################

project = preprocess(project)
project = parse(project)
create(project)