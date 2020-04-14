# Lenk
A programming language with very little functionality

##Basic usage
Command
Command : Argument
Command ; Command
Command : Argument ; Command : Argument

##Functionality

#text
This can be used to mirror input
  Arguments : string
  Input | text : Hello
  Output | Hello

#blank
This can be used to get a newline 
  Input | blank
  Output | \n

#numeric
  This can be used to evaluate mathmatical expressions
  Arguments : math expression
  Input | numeric : 23 * 3
  Output | 69
  
#version
  Returns the current version
  Arguments: only, if given will return only the version
  input | version
  Output | Lenk Version: x.x.x
  
##Planned features
  #if
  do comparisons between variables
  #for
  repeat a code block for x times
  #set
  set a variable
