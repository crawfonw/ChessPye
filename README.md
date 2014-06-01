ChessPye
=======
ChessPye is a simple Chess engine written in Python. It was designed with the idea that it should be extendible to easily create variations on the "vanilla" game. Ideally this could be useful in an education setting for teaching OOP, software design, basic AI (i.e. search), etc. So unlike the other Chess engine I am working on, this one is not suited for playing good Chess fast. Smaller games are better for demos with the current AI and rule checks.

The code is currently in a working state. And by that I mean you can play a game of Chess with Human/Human, Human/AI (if you are patient enough or pick the bad AI), or AI/AI through a GUI or CLI.

There are still many things that need to be done before I step completely away from the project:

* Proper API
 * Right now you can extend and call classes, but it needs to be cleaned/be more well-structured
* Base AI inprovements
 * Permanent brain
 * Better base scoring function
* GUI Enhancements
 * AI selector
 * Show AI search paths/thinking patterns
 * Move history list
 * Relative material balance graph
* Clean up/optimise rules engine (maybe)

There are also some out of scope ideas I would like but probably won't do:
* PNG loading/exporting
* Timer
