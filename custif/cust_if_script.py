#!/usr/bin/env python3

#Test if, elif, and else statements

mastery = float(input("How many champions do you have mastery 6 or 7?"))

if mastery < 5:
    print("Play more champions, OTP is not as great as it is made to seem")
elif mastery < 20:
    print("You've got a good pool going. Maybe try a new role and find some exciting champs there!")
elif mastery < 50:
    print("You clearly know your way around Summoner's Rift. I challenge you to master your least favorite role!")
elif mastery <150: 
    print("Ok you're outrageous. How can you be that good with that many champions?")
elif mastery < 169:
    print("There aren't that many champs kiddo. Stop trolling")
else:
    print("You need to play more! Try focusing on a single champ at a time.")



print("Thank you for checking in")

