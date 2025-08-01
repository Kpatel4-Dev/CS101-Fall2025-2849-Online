# Formatting text and numbers using print f-string

## Doing String Interpolation With F-Strings in Python:

 F-strings joined the party in Python 3.6 with PEP 498. Also called formatted string literals, f-strings are string literals that have an f before the opening quotation mark.
  
 They can include Python expressions enclosed in curly braces. Python will replace those expressions with their resulting values. So, this behavior turns f-strings into a string interpolation tool.
  
 In the following sections, you’ll learn about f-strings and use them to interpolate values, objects, and expressions in your string literals.
  
## Interpolating Values and Objects in F-Strings:

 F-strings make the string interpolation process intuitive, quick, and concise. The syntax is similar to what you used with .format(), but it’s less verbose (expressed in more words than are needed). You only need to start your string literal with a lowercase or uppercase f and then embed your values, objects, or expressions in curly brackets at specific places:

name = "Jane"
age = 25

print(f"Hello, {name}! You're {age} years old.")

Output --> 'Hello, Jane! You're 25 years old.'

Look how readable and concise your string is now that you’re using the f-string syntax. You don’t need operators or methods anymore. You just embed the desired objects or expressions in your string literal using curly brackets.
---
## Important Note:

 That Python evaluates f-strings at runtime. So, in this example, both name and age are interpolated into the string literal when Python runs the line of code containing the f-string. Python can only interpolate these variables because you defined them before the f-string, which means that they must be in scope when Python evaluates the f-string.
---
## Embedding Expressions in F-Strings:

You can embed almost any Python expression in an f-string. This allows you to do some nifty things. You could do something pretty straightforward, like the following:

print(f"{2 * 21}")
Output ---> '42'

When Python runs this f-string, it multiplies 2 by 21 and immediately interpolates (insert) the resulting value into the final string.
