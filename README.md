# Code_Optimization
## Aim
The aim of this code was a personal project to be able to write code with shorter runtime.
`I do not have any prior experience or coursework in algorithms, nor do I have any experience in code optimization.`
This is just my personal way of trying to write cleaner and better code by eliminating repetitions and adhering to the DRY principle.

## Problem Statement
This code attempts to perform only one task: `Take a number and convert it into its Roman Numeral equivalent.`

## Approaches

### Approach 1
Subtract the number from the highest possible (In this case we are limiting the number 3999) Roman Numeral value which is distinct. 
Here it is 1000 which is denoted by M. Then we subsequently move to the lower digits by recursive calls and doing the same.
All the time we traverse a set dictionary with the `{key : value}` being the `{Numeral : Roman Numeral}`.

### Approach 2
I break the number into its constituent digits, put it into a dictionary which holds the numeral value with a key denoting its place.
Say in 2300 --> {1000: 2, 100: 3, 10: 0, 1: 0}.
The converter then takes values from the dictionary and quickly assigns it to the building string. 

## Result
On an average the second approach was 32% more efficient than the first. 

## Note
I am still a python novice, and trying to pick up as many tips and suggestions as possible to improve my coding efficiency.
Any and all suggestions are welcome.
