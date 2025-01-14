# Define Python interpreter
PYTHON=python3

.PHONY: build run plots clean

build:
	@echo "Generating test files..."
	@$(PYTHON) -c "from testing_scripts.generate_tests import generate_all_tests; generate_all_tests()"
	@$(MAKE) clean_pycache

run:
	@echo "Running tests..."
	@$(PYTHON) -c "from testing_scripts.run_tests import run_main; run_main()"
	@$(MAKE) clean_pycache

plots:
	@echo "Generating plots..."
	@$(PYTHON) -c "from graph_scripts.make_graphs import Plots, root; plots = Plots(root); plots.make_graphs(); plots.make_overlapped_graphs(); plots.make_welsh_and_greedy()"
	@$(MAKE) clean_pycache

clean:
	@echo "Cleaning test and results directories..."
	@if [ -d "../tests" ]; then rm -r ../tests && echo "Deleted ../tests directory."; else echo "../tests directory does not exist."; fi
	@if [ -d "results" ]; then rm -r results && echo "Deleted results directory."; else echo "results directory does not exist."; fi
	@$(MAKE) clean_pycache

clean_pycache:
	@echo "Cleaning __pycache__ directories..."
	@find . -name "__pycache__" -type d -exec rm -r {} + && echo "Deleted all __pycache__ directories." || echo "No __pycache__ directories found."
