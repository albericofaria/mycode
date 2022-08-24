#!/usr/bin/env python3
## create file object in "r"ead mode
lines = 0
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    lines = lines + 1
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(lines)
