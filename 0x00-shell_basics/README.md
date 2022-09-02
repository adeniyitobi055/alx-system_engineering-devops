#!/bin/bash
Shell navigation basic commands
pwd -Prints the current working directory
ls - This command list directory and files in the current working directory
ls -l - List current directory content in long format (details)
ls -all - List all current directory content including hidden files
ls -al - List all current directory files including hidden files in long format.
mkdir - Creates a directory
mv - Move a file or directory
rm -r - Deletes a files or directory
cd -     - Navigate to previous directory
ls -al . .. /boot - List all files in current working directory including /boot directory in long format
file /tmp/iamafile - Prints the type of file in /tmp directory
ls -s /bin/ls --ls--   - Creates a symbolic link
cp -rua *.html /tmp - Copies all non-existing html files to /tmp directory from working directory
mv [[upper:]]* /tmp/u - Move all files starting with uppercase to /tmp/u directory
rm -r *~ - Deletes all files that end with the character ~
mkdir -p welcome/to/school - Creates the directories welcome/, welcome/to/, welcome/to/school
ls -map|sort -d  - List files in the current working directory separated by commas (,)
