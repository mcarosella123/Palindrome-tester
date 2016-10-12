# Project 04 - A "Quick" Project

Objectives:  

1. Continue to work with Git and GitHub to manage the development of a software project
2. Utilize the Stack ADT to determine whether or not a given string is a palindrome
  
This project is worth 15 points.  This project is based on [LM] Project 2, pp. 208.

Please note this is an **_INDIVIDUAL_** project, and not a group project. Note that this project is classified as a *Quick* project. It is meant to require a relatively small amount of code, that you can complete in a relatively small amount of time.  (As an example of a similar (but not equivalent) project, you might review [LM]'s `brackets.py` program on pp. 176-177.)

## Task 1: Create a new branch
Create a new branch to track your work on this project after accepting the repository. Do *not* commit changes to the 'master' branch.  

You may wish to create additional branches as you solve the following tasks, but that is up to you. (If you do so, you'll want to merge your branches into a single branch before submitting your work as noted below...if you do so, be certain **not** to merge the changes into the 'master' branch!)

*For instructor use only:*

Task 1          |  Notes
------          |  --------------------------
Branch creation | 

## Task 2: Create a plaindrome tester
Add a new file named `palcheck.py` to your project. In this file, construct a Python program that uses a stack to determine whether or not a user supplied string is a *palindrome*.

A palindrome is a sequence of words that reads the same as the sequence in reverse: for example, *noon*. Your program should ignore whitespace in the given string. It should also make no distinction between upper-and lower-case in the input string.

Prompt the user for the following items:

1. A string to check
2. The type of stack to use (either "array"-based or "linked"-based).

Your program should then use the type of stack specified to determine whether or not the supplied string is a palindrome, and should report the results to the user.  An example session might look like:

```
Enter a string: Able was I ere I saw Elba
Type of stack: array

YES! "Able was I ere I saw Elba" IS a palindrome.

Again? Y
Enter a string: It is hot
Type of stack: linked

NO! "It is hot" is NOT a palindrome.
Again? N

Thanks for playing!
```

You will find complete definitions of the Stack classes/hieararchy in this repository for your use.  Do **not** modify any of the given files; simply create a new file named `palcheck.py`.

Task 2          |  Notes
------          |  --------------------------
Main program | 


## Submitting your work via 'pull request'
Once you have made the required additions above to the various project files, and you have tested them to your satisfaction, create a **pull request** ([https://help.github.com/articles/creating-a-pull-request/]()) to request that I merge them into the 'master' branch. Do **not** complete the merge yourself; I want to look at your code before committing it to the repository. Make certain to add a comment associated with the pull request and give me an @ mention (@BergProfJ) in it, so that I know you've completed these tasks.

Project 04 Marking Criteria | Notes
------ | -----
Program properly imports required modules (1 pt possible) | 
Program correctly prompts user for string and stack type (2 pts possible) |
Program correctly parses string, ignoring whitespace and capitalization (2 pts possible) |
Program correctly instanties and updates a stack of the required type (3 pts possible) |
Program uses stack to determine whether or not string is a palindrome and reports results (3 pts possible) |
Program asks user whether they wish to continue (1 pt possible) |
Program correctly commented and well-organized, and follows Python style conventions (3 pts possible) |
