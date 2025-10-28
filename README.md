# INET4031 Add Users Script and User List

## Program Description

The **INET4031 Add Users Script** is a Python-based automation tool that simplifies creating multiple user accounts on a Linux system. Traditionally, a system administrator would have to manually create users by typing several commands for each account, such as:

- `sudo adduser username` — creates a new user account  
- `sudo passwd username` — sets or updates the user’s password  
- `sudo adduser username groupname` — adds the user to a specific group  

Performing these steps for multiple users can be time-consuming and prone to human error. This script automates that same process by reading user information from an input file and using the same commands internally. It automatically creates the accounts, sets their passwords, and assigns users to their groups — all with a single command.  

By automating user creation, this program saves administrators significant time, ensures consistency, and reduces mistakes when managing large numbers of accounts.

---

## Program User Operation

The script reads an input file containing user details, processes each line, and executes the appropriate Linux commands to create accounts. It ignores lines that start with `#` (comments) or any that are formatted incorrectly. During execution, it displays progress messages — such as when it’s creating a user, setting passwords, or adding users to groups.  

Once set up correctly, the program can be used either for a **dry run** (to preview commands) or for actual execution to make real changes to the system.

---

### Input File Format

Each line of the input file must follow this format:

username:password:last:first:groups

# Explanation of Each Field

- `Username` – The name of the account to be created. Example: user04

- `Password` – The password for that user. Example: pass04

- `Last` – The user's last name, used for GECOS information in the system. Example: Last04

- `First` – The user's first name. Example: First04

- `Groups` – A list of one or more groups that the user should belong to. Commas separate multiple groups. Example: group01,group02

If a line begins with a #, it is considered a comment and will not be processed. This is useful for temporarily disabling user entries without deleting them.

If you do not want a user added to any additional groups, use a dash (-) in the groups field. The script recognizes it as “no group.”

If a line does not have exactly five fields separated by colons, it is automatically skipped.

### Command Execution
Before running the program, make sure that the Python file has execute permission. Use this command in the terminal: 
  chmod +x create-users.py

  Once the script is executable, it can be run in two ways:
  ./create-users.py < create-users.input 
  or
  sudo python3 create-users.py < create-users.input (with privileges)
  
The < symbol redirects the contents of the create-users.input file into the script’s standard input (sys.stdin), allowing the program to read each line automatically.

During execution, the script will display progress messages such as:
  ==> Creating account for user04...  
  ==> Setting the password for user04...  
  ==> Assigning user04 to the group01 group...
These messages confirm that each step is being performed in sequence.

### Dry Run

A dry run is a safe test mode that lets you verify the script’s behavior without making real system changes. It is ideal for confirming that your input file is correctly formatted and that the script will execute the intended commands.

To perform a dry run:

Leave the os.system(cmd) lines commented out in the script.

Make sure the print(cmd) lines are uncommented.

This way, the program will display the commands it would run, but not execute them.

Example dry run output:
==> Creating account for user06...
/usr/sbin/adduser --disabled-password --gecos 'First06 Last06,,,' user06
==> Setting the password for user06...
/bin/echo -ne 'pass06\npass06' | /usr/bin/sudo /usr/bin/passwd user06
==> Assigning user06 to the group01 group...
/usr/sbin/adduser user06 group01
==> Assigning user06 to the group02 group...
/usr/sbin/adduser user06 group02





