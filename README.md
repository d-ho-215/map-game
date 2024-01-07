# Map Explorer Game

A map exploring game using text in the terminal. 

### Features to implement
- [x] Print map from array, clear screen after each move, then redraw.
- [x] Move around using WASD
- [ ] Auto add semi-random characters in empty spaces to help visualize movement
- [ ] Player character in moveable location
- [x] Color text to help differentiate / highlight significant cells
- [ ] Notifications / information text to the side or bottom of map window
- [ ] Objects to interact with in space
  - [ ] Treasure objects
  - [ ] Creatures
- [ ] 
- [ ] 

## Map element definitions
- X : Wall, color: white (fg:90) `\x1b[0;90;40m` (not really white... rgb +/- 204,204,204)
- P : Player, color: bright magenta (fg:95) `\x1b[0;95;40m`
- c : Treasure Chest, color: yellow (fg: 33) `\x1b[0;33;40m`
- ' ': Empty Space, color: gray (fg: 90) `\x1b[0;90;40m`

## Resources and References
- [NeuralNine YouTube - Displaying Progress Bar in Terminal](https://www.youtube.com/watch?v=x1eaT88vJUA)
  - using '\r' to return on same line and overwrite
- [ANSI Escape Codes - fnky GitHub](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797)
  - foreground + background color codes + reset
  - text style codes (bold, italic, blink, etc)
- [Wikipedia ANSI Escape Codes](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors)
 - foreground + background color code chart
- [StackOverflow - How do I print colored text to the terminal?](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)
 - example color charts of foreground and background colors combined
 

