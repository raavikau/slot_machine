## Slot Machine Game implement in python
### Initial State
* User input first deposit valid amount more than 0.
* Choose number of lines to bet on 1-3 and bet amount on each line.
### Running State
* Generate a random slot machine spin. Create columns of symbols based on their symbol frequency and row-column dimensions.
* To check winnings, iterates over chosen lines to see all symbols in line match.
* If match found player earn money based on symbol value which multiplies with bet amount.
* Player balance is update every time based on total winning minus bet amount.
### Terminal State
* Game end when balance amount is zero.
* Repeatedly allow the player to spin until they choose to quit.
