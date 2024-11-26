import subprocess
import os

def build_doc(language):
    os.environ["current_language"] = language
    subprocess.run("git checkout", shell=True)
    os.environ['SPHINXOPTS'] = "-D language='{}'".format(language)
    subprocess.run("make html", shell=True)    

def move_dir(src, dst):
  subprocess.run(["mkdir", "-p", dst])
  subprocess.run("mv "+src+'* ' + dst, shell=True)

os.environ["build_all_docs"] = str(True)
os.environ["pages_root"] = "https://mrfcoelho.github.io/eir" 

build_doc("en")
move_dir("./_build/html/", "./pages/en/")
build_doc("pt_PT")
move_dir("./_build/html/", "./pages/")
