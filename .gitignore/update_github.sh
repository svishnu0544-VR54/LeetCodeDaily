#!/bin/bash

echo "Adding all new files..."
git add .

echo "Enter commit message (example: Day 5 LeetCode Binary Search)"
read message

echo "Committing changes..."
git commit -m "$message"

echo "Pushing to GitHub..."
git push

echo "Done! Your code is now on GitHub."