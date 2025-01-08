from graph_scripts.make_graphs import Plots, all_paths
import subprocess
import shutil
import os
import sys

def generate_tests():
    '''Runs the generate_tests.py script to generate test files'''
    print("Generating test files...")
    subprocess.run(["python3", "generate_tests.py"])

def run_tests():
    '''Runs the run_tests.py script to execute the tests and save results'''
    subprocess.run(["python3", "run_tests.py"])

def generate_plots():
    plots = Plots(all_paths)
    plots.make_graphs()

def clean():
    '''Deletes the tests and results directories'''
    directories = ["tests", "results"]
    for directory in directories:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"Deleted {directory} directory.")
        else:
            print(f"{directory} directory does not exist.")

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