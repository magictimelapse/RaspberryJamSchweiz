Eggbot
=======

Important notice
-----------------

THE VERSION eggbot-2.8 is currently not working!!!

Installation on ArchLinux
--------------------------

Install these packages (if you don't have your own repository server use -U and the path to the package)
pacman -S sphereobot
pacman -S eggbot


Programm ARDUINO on ArchLinux
------------------------------

Run sphere-o-bot-programmer and programm the connected ARDUINO as usual:
- Add Serial library if not available (Sketch -> Include Library -> Manage Libraries...)
- Board: Arduino Leonardo
- Select correct port.
- Upload the porgramm
- Close the arduino sdk

Configure Inkscape
-------------------

Calibrate pen up/pen down position
- Extensions -> EggBot > Eggbot Control
- Check the settings in "Setup" Tap:
-- Pen up position: 55
-- Pen donw position: 50
-- Action on 'Apply': Toggle pen up/down

Create a drawing
-----------------

- create a new document 32000x800px.
- Extensions -> EggBot > Eggbot Control
- Open "Plot" tab
- Run apply to start drawing
