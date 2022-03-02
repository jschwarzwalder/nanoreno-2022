# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


image side jess = "jess.png"

define jessica = Character("Jessica", image="jess")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show jess at left  

    # These display lines of dialogue.

    jessica "You've created a new Ren'Py game."

    jessica "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
