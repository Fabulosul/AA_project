#!/bin/bash

# Script to delete all __pycache__ directories in the current directory and subdirectories

echo "Searching for __pycache__ directories..."

find . -type d -name "__pycache__" -exec rm -rf {} +

echo "All __pycache__ directories have been deleted."
