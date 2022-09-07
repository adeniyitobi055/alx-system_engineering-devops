This directory generally contains shell permission basic commands:
1 - Switches user to betty
2 - Prints current username of user
3 List all groups current user is part of
4 - Changes the owner of hello file to betty
5 - Creates an empty file name hello
6 - Add execute permission to owner of file and write permission to group owner and other users
7 - Add execute permission to owner and group owner and write permission to other users
  7 - Read + Write + Execute
  6 - Read + Write
  5 - Read + Execute
  4 - Read
  3 - Write + Execute
  2 - Write
  1- Execute
  0 - No permission
 - Sets the mode of permission of hello same as olleh
chmod a+x */ - Adds execute permission to owner, group owner, other users of subdirectories
chmod 751 - Adds all permission to owner, Read + Write to group owner, Execute permission to other users
mkdir -m 751 my_dir - Creates a directory with permission 751
chgrp school hello - Changes group owner to school for hello file
chown vincent:staff * - Changes owner to vincent, group owner to staff for all files and directories in the current working directory
chown -h vincent:staff _hello - SAME AS (chown vincent:staff *) but with a symbolic link
chown --from=guillaume hello - Changes the owner only if it is owned by the user guillaume
telnet link-of-video  - plays the link of a video from the terminal
