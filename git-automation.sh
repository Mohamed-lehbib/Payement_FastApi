#!/bin/bash

# Check if two arguments are given
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <commit_message> <branch>"
    exit 1
fi

# Assigning arguments to variables
commit_message="$1"
branch="$2"

# Executing Git commands
git add .
git commit -m "$commit_message"
git push origin "$branch"

echo "Git operations completed."
