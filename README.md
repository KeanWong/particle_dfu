# Particle_DFU
This program discovers any connected (single) [Particle](Particle.io) board, and forces it into DFU mode.

It uses the USB "serial" port. Weird configuration changes on the Particle board and application code might break the functionality.

## Installation
1. ```cp particle_dfu.py particle_dfu```
2. ```chmod +x particle_dfu```
3. Move the ```particle_dfu``` file to whatever directory you want to run it from.
4. Add the directory into your shell's $PATH

## Testing
This was tested under python 3.7 on a Mac, using a USB serial connection to a Particle Argon board.

