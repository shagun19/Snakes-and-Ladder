# N-player Snakes-and-Ladders
* [What is snakes and ladders](https://en.wikipedia.org/wiki/Snakes_and_Ladders)
* Objective: The first player to reach the 100th block wins.
* Rules of the game:
  * Each player rolls a dice in her respective turn.
  * In order to enter the game, one had to roll a six. Untill then you cannot start.
  * Upon rolling a six you get another turn to roll. However three simultaneous sixes cancel each other and you skip your turn. Thus valid rolls can be (6,3), (6,6,4) whereas invalid roll is (6,6,6).
  * Upon landing up on the foot of a ladder, you get to hop on the higher number where the ladder ends. You get an additional turn as well.
  * Landing up on a snake does the exact opposite.
  * You can only exit the game when you land on 100th block through the exact count. Example: if you are on 98th block and get a 5 on your dice then you cannot move. You can move by only when you get 1 or 2.

* How to run the script:
 ```python snakes-ladders.py <num_players>```
