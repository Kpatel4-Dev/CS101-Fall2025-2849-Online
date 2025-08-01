# Name Game
For context: [Video of Name Game Song](https://youtu.be/5MJLi5_dyn0)

_The name game lyrics:_

Shirley! 
Shirley, Shirley Bo-berley, 
bo-na-na fanna Fo-ferley. 
fee fi mo-merley, Shirley!

Lincoln! 
Lincoln, Lincoln. bo-bincoln
Bo-na-na fanna, fo-fincoln
Fee fi mo-mincoln, Lincoln!

Come on ev'rybody, I say now let's play a game
I betcha I can make a rhyme out of anybody's name
The first letter of the name
I treat it like it wasn't there
But a "B" or an "F" or an "M" will appear
And then I say "Bo" add a "B" then I say the name
Then "Bo-na-na fanna" and "fo"
And then I say the name again with an ""f" very plain
Then "fee fi" and a "mo"
And then I say the name again with an "M" this time
And there isn't any name that I can't rhyme

Arnold! 
Arnold, Arnold bo-barnold
Bo-na-na, fanna fo-farnold
Fee fi m-marnold. Arnold!
...

## Directions

### Step 1
Write a function called name_game that takes a name and print out the Name Game rhyme. 

For example, if the input is "Catherine" then the output should be...

CATHERINE
Catherine, Catherine, bo-Batherine
Banana-fana fo-Fatherine
Fee-fi-mo-Matherine 
Catherine!

```name_game("Nery")``` should produce...

NERY
Nery, Nery, bo-Bery
Banana-fana fo-Fery
Fee-fi-mo-Mery 
Nery!

I gave you the code that will ask the user for a name and then call your function. **Don't change that code**.
---
### Hacker Challenges (Optional)
There are special cases where the above does not work well. Alter your function to account for these special rules.
---
1. If the first letter is a vowel, don't drop the first letter.

Example: 

EARL
Earl, Earl, bo-Bearl
Banana-fana fo-Fearl
Fee-fi-mo-Mearl 
Earl!
---
2. If the first letter is a 'B', 'F', or 'M' do not add the letter back in for that corresponding line.

'B' Example:

BILLY
Billy, Billy, bo-illy
Banana-fana fo-Filly
Fee-fo-mo-Milly
Billy!

'F' Example:
FRANCIS
Francis, Francis, bo-Brancis
Banana-fana fo-rancis
Fee-fi-mo-Mrancis
Francis!

'M' Example:
MOSES
Moses, Moses, bo-Boses
Banana-fana fo-Foses
Fee-fi-mo-oses
Moses!
