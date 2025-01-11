from graph_scripts.make_graphs import Plots, all_graphs, common_graph_path
from testing_scripts.generate_tests import generate_all_tests
from testing_scripts.run_tests import run_main
import subprocess
import shutil
import os
import sys

def generate_tests():
    '''Runs the generate_tests.py script to generate test files'''
    print("Generating test files...")
    generate_all_tests()
    delete_pycache()

def run_tests():
    '''Runs the run_tests.py script to execute the tests and save results'''
    run_main()
    delete_pycache()

def generate_plots():
    plots = Plots(all_graphs, common_graph_path)
    plots.make_graphs()
    plots.make_overlapped_graphs()
    delete_pycache()

def clean():
    '''Deletes the tests and results directories'''
    directories = ["../tests", "results"]
    for directory in directories:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"Deleted {directory} directory.")
        else:
            print(f"{directory} directory does not exist.")
    delete_pycache()

def delete_pycache():
    '''Deletes __pycache__ directories from all subdirectories'''
    for root, dirs, files in os.walk("."):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            shutil.rmtree(pycache_path)
            print(f"Deleted {pycache_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "build":
            generate_tests()
        elif command == "run":
            run_tests()
        elif command == "plots":
            generate_plots()
        elif command == "clean":
            clean()
        else:
            print(f"Unknown command: {command}")
    else:
        print("Usage: make.py [build|run|clean]\n   build - generates test files\n   run - run the generated tests\n   clean - deletes the tests and results directories")