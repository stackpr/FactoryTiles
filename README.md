Scope
=====

FactoryTiles aims to be a complete but minimal graphicsset for RoboRally®.
Complete means that all possible situations can be displayed with these graphics.
Minimal means that there are no graphics not needed to display the original game.

If you want RoboRally®, include FactoryTiles. If you want zombies, fork FactoryTiles.
This also means, your graphics engine needs to support semi-transparency per-pixel and rotation.

Paradigms
=========

* The viewpoint is exactly from above.
* The viewpoint has a finite distance.
* The default motion direction is north to south.
* The default rotation direction is clockwise, starting north.
* All graphics are the full tile size.
* Outlines are 1px wide at 64 px tile size.

Notes on Building
=================

The default rendersize is 64 x 64 pixels per tile and current renderings are part ot the distribution.
Other resolutions can be generated by appending them to the make command, if you need other sizes for debugging or production.
For example, use following to generate images for 32x32, 64x64 and 128x128 tilessize.
    $ make .32 .64 .128

Dependencies
------------

* `make` - dependency-driven creation
* `GNU` - basic folder and file operations
* `Inkscape` - renders the SVGs into PNGs
* `markdown` - renders README.md into README.html (optional)

The Tile Model
==============

Each tile on the playing field has one floor, eventually some properties and up to two robots on it.


Floors - Whatever needs to be rendered first
--------------------------------------------

* abyss - infinitely deep nothing or the brink to it
* concrete - just plain floor
* conveyorBelt - conveyor belts
* expressBelt - express belts
* repair - repairzone
* turntable - turns robots

Properties - Stuff associated with a tile
-----------------------------------------

* checkpoint - marks the route
* laser - damages robots occassionally (rotate as needed)
* laserEmitter - emits laser (ternary naming is for a reason)
* press - destructs robots occassionally (embedded into walls)
* slide - moves robots occassionally
* wall - keeps robots from crossing it (binary naming is for a reason)

Robots - The Counters of RoboRally
----------------------------------

* The eight original robots
* custom robots

Order of Rendering
==================

The order of rendering from background do foreground is as follows:
floor, checkpoint, laser, wall, laser emitter, slide, robot, press

Status
======

<table>
    <thead>
        <tr>
            <td>Component</td> <td>Status</td> <td>Size</td> <td>Comment</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>rekursive make framework</td> <td>done</td> <td></td>
        </tr>
        <tr>
            <td>iterative make framework</td> <td>done</td> <td></td>
        </tr>
        <tr>
            <td>bot/Hammer_Bot</td> <td><b>todo</b></td> <td>1 graphic</td>
        </tr>
        <tr>
            <td>bot/Hulk_X-90</td> <td><b>todo</b></td> <td>1 graphic</td>
        </tr>
        <tr>
            <td>bot/Spin_Bot</td> <td><b>todo</b></td> <td>1 graphic</td>
        </tr>
        <tr>
            <td>bot/Squash_Bot</td> <td><b>todo</b></td> <td>1 graphic</td>
        </tr>
        <tr>
            <td>bot/Trundle_Bot</td> <td><b>todo</b></td> <td>1 graphic</td>
        </tr>
        <tr>
            <td>bot/Twitch</td> <td><b>todo</b></td> <td>1 graphic</td>
        </tr>
        <tr>
            <td>bot/Twonky</td> <td><b>todo</b></td> <td>1 graphic</td>
        </tr>
        <tr>
            <td>bot/Zoom_Bot</td> <td><b>todo</b></td> <td>1 graphic</td>
        </tr>
        <tr>
            <td>floor/abyss</td> <td>done</td> <td>21 graphics</td>
        </tr>
        <tr>
            <td>floor/concrete</td> <td><b>todo<b></td> <td>1 graphic</td>
        </tr>
        <tr>
            <td>floor/conveyorBelt</td> <td>done</td> <td>7 graphics</td>
        </tr>
        <tr>
            <td>floor/expressBelt</td> <td>done</td> <td>7 graphics</td>
        </tr>
        <tr>
            <td>floor/repair</td> <td><b>todo</b></td> <td>2 graphics</td>
        </tr>
        <tr>
            <td>floor/turntable</td> <td><b>todo</b></td> <td>2 graphics</td>
        </tr>
        <tr>
            <td>module/original</td> <td><b>todo</b></td> <td>9 graphics</td>
        </tr>
        <tr>
            <td>property/checkpoint</td> <td><b>todo</b></td> <td>6 graphics</td>
        </tr>
        <tr>
            <td>property/laser</td> <td><b>todo</b></td> <td>9 graphics</td>
        </tr>
        <tr>
            <td>property/laserEmitter</td> <td><b>todo</b></td> <td>3 graphics</td> <td>or would 49 be better?</td>
        </tr>
        <tr>
            <td>property/press</td> <td><b>todo</b></td> <td>3 graphics</td>
        </tr>
        <tr>
            <td>property/slide</td> <td><b>todo</b></td> <td>5 graphics</td>
        </tr>
        <tr>
            <td>property/wall</td> <td>done</td> <td>15 graphics</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td>overall</td> <td>51 %</td> <td>50/98 graphics</td>
        </tr>
    <tfoot>
</table>

Approx amount of time needed to build: 4 minutes / 2,5 GHz

Complexity
----------

Each tile consists of 1 of the 16 abyss not combinable with anything (4 orientations, 64 variants)

or 1 of the 5 abyss, which are combinable with walls as follows:

* bay - 0000, 0010, 0100, 0110, 1000, 1010, 1100, 1110 (4 orientations, 32 variants)
* edge - 0000, 0100 (4 orientations, 8 variants)
* nook - 0000, 0100, 1000, 1100 (4 orientations, 16 variants)
* single - 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111 (16 variants)
* turn - 0000, 0100, 1000, 1100 (4 orientations, 16 variants)

or (

1 of the following floors

* concrete (1 variant)
* conveyorBelt (7 types, 4 orientations, 28 variants)
* expressBelt (7 types, 4 orientations, 28 variants)
* repair (2 types, 4 orientations, 8 variants)
* turntable (2 types, 4 orientations, 8 variants)

and anything of the following

* 0 to 1 checkpoint (6 types, 7 variants),
* 0 to 1 laser (9 types, 10 variants),
* 0 to 2 laserEmitters (non-opposing, 49 variants),
* 0 to 1 press (2 variants),
* 0 to 2 slides (non-opposing, 8 variants) and
* 0 to 1 of the 15 walls (16 variants)

).

That gives us 64 + (32 + 8 + 16 + 16 + 16) + (1 + 28 + 28 + 8 + 8) * 7 * 10 * 49 * 2 * 8 * 16 = 1.164.952 variants per tile.

### Variations for laserEmitters

0000 0001 0002 0003

0010 0011 0012 0013

0020 0021 0022 0023

0030 0031 0032 0033

0100 0110 0120 0130

0200 0210 0220 0230

0300 0310 0320 0330

1000 1001 1002 1003 1100 1200 1300

2000 2001 2002 2003 2100 2200 2300

3000 3001 3002 3003 3100 3200 3300
