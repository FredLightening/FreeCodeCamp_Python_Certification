TOWER OF HANOI SOLVER (Python)

This project solves the tower of Hanoi puzzle optimally in (2^n)-1 moves, where n is the number of disks.
It does this by:
*Checking if the number of disks are even or odd and changing the starting move based on it.
*Checking rod states in the while loop and determines whether a disk can be moved from the rod in question.
*Validating the moves using a custom move validation function that checks even/odd parity to determine where the disks can go.

Tech Stack:
*Language: Python 3.14.5
*Key concepts: Memory aliasing vs copying, identity operators, loop guards, array manipulation.

Debugging journey and bug log:

1. The invisible Win-Condition Trap (List Aliasing):
*Symptom: The algorithm solved the puzzle visually but the while loop ran forever.
*Cause: Setting *"rod_one=initial"* created an alias(reference to the same object in memory) rather than a copy of it. This caused every disk that was removed from rod_one to also be silently removed from initial,making the while loop condition never true.
*Cure: Explicitly cloning the *initial* list using the *.copy()* method so that the list remained static.

2.  The Forced Illegal move (If/Else statements):
*Symptom: The algorithm did not complete the puzzle and kept stopping after moving 2 disks from rod_one to the other two disks.
*Cause: Not being specific enough about the condition for the if statements. Using *"if rod_one and rod_one[-1]!=prev"* instead of *"if rod_one and rod_one[-1]!=prev and ((not rod_two or not rod_three) or (rod_one[-1]<rod_two[-1] or rod_one[-1]<rod_three[-1]))"* caused the condition to always be true and allow consistent looping.
*Cure: Explicitly specifying the condition for the if/else statements to avoid it being true when it is not supposed to be.

3. Motion without Direction (Missing Decision Engine):
*Symptom: The algorithm was just randomly throwing disks from one rod to the other without any direction.
*Cause: There was no move validator to tell the program what the optimal moves are.
*Cure: Creating a custom *move checker* function that uses even/odd parity to determine the optimal move.
