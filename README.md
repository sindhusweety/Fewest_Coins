# Fewest_Coins

Find a minimum number of coins from a list of coins.
The Sum of minimum numbers must equal the target value.

Used BackTracking technique that explores all the possibilities(solutions)
to choose an optimal solution from all possible solutions

ALGORITHMS' STEPS
create empty result list obj and deep copy the coins to another obj
write base case and sub-function must move toward to base case.
sub-function must have a base case and it must call itself
In sub-function, minus min value (min value found in coins &
min value that closes to target) from target recursively
till it gets the base case.

pylint change_test.py

pytest change_test.py

python3 change_test.py
