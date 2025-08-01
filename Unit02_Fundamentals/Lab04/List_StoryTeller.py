'''

Lists in Python

Description: Using Lists in Python (and past topics like looping, strings, etc.) to understand and practice. Also to tell stories!

Developer Name(s): FIRST+LAST NAMES <EMAIL>,  ...

Date: MM/DD/YYYY

'''
##########################################
# IMPORTS:
#   modules needed for program
##########################################



##########################################
# FUNCTIONS:
#   functions useful to main program
##########################################
def print_typewriter(text):
  '''
  Given some text, prints each character one at a time,
  with a small pause in between (like if someone were
  typing on a typewriter).
  '''
  #code here!

def print_story(lines):
  '''
  Given a list of lines, prints each line like a typewriter
  on its own line and one at a time.
  '''
  #code here!

##########################################
# MAIN PROGRAM:
#   beginning of running program
##########################################
title = "Title Goes Here"
story = ["This is the introduction sentence.",
          "This is the body sentence.",
          "This is the conclusion!"]

print_typewriter(title.center(50))
print() #print blank line
print_story(story)
print() #print blank line
print_typewriter("F I N".center(50))
