#!/usr/bin/python3

# INET4031
# Your Name
# Data Created
# Date Last Modified

# os: lets the script run system commands like adduser or passwd.
# re: allows searching for patterns in text using regular expressions.
# sys: lets the script read input from stdin (like from a file using "<".

import os
import re
import sys


def main():
    for line in sys.stdin:

        # This checks if the line starts with a '#' character, meaning its a comment line.
        # It looks for the '#' character so the script can skip comment lines and ensures that it will not try to xreate users from them.
        match = re.match("^#",line)

        print("the content of the match variable were: ", match)
        
        # This line removes any extra spaces or newlines from the line, then splits it into parts wherever a colon appears.
        # It does this because each line of the input file uses colons to seperate user info. 

        fields = line.strip().split(':')
    
        print("length of fields was: ", len(fields))

        # This if statement checks where the line is a comment (match) or if it doesn't have exactly five fields. If either condition is true, the script skips that line with continue, so only properly formatted, non comment lines are processed. 

        if match or len(fields) != 5:
            continue

        # These lines take each pieve of user info from the input line.
        # 'username' and 'password' are taken directly from the first two fields.
        # 'gecos' combines the user's first and last name into the format used in the /etc/group file. 
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # This splits the last field (groups) by commas so multiple groups can be handled seperately.
        # Each group name will be processed on by one when assigning the user to groups.
        groups = fields[4].split(',')

        # This print statement shows which user account is currently being created.
        # It helps track the script's progress and confims which username is being processed.
        print("==> Creating account for %s..." % (username))
    
        # This line builds the Linux command used to create a new user account.
        # The variable 'cmd' stores the full command with the user's info and GECOS details included.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

    
        # The first time you run the code, you should leave the 'os.system(cmd' commented out using '#' so you can test the code safely.
        # If left uncommented, the 'os.system(cmd)' line will actually run the system command to create the user account on the computer. 
        #print cmd
        os.system(cmd)

        # This print statement shows which user's password is about to be set. 
        # It helps track progress and confirms the script is moving to the password step for that user. 
        print("==> Setting the password for %s..." % (username))

        # This line builds a command that automatically sets the user's password.
        # It uses 'echo' to send the password twice (for confirmation) into the 'passwd' command through a pipe.
        #The variable 'cmd' holds the full command that updates the user's password in the system.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # The first time you run the code, you should leave the 'os.system(cmd' commented out using '#' so you can test the code safely.
        # If left uncommented, the 'os.system(cmd)' line will actually run the system command to create the user on the computer.
        
        #print cmd
        os.system(cmd)

        for group in groups:
            # This IF statement checks if the group value is not '-' (a placeholder meaning no group).
            # If the group is valid, it assigns the user to that group by running the adduser command.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
               #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
