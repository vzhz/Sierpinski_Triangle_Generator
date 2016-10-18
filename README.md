# Exploring Sierpinski triangles and pyramids
<a href='http://www.recurse.com' title='Made with love at the Recurse Center'><img src='https://cloud.githubusercontent.com/assets/2883345/11325206/336ea5f4-9150-11e5-9e90-d86ad31993d8.png' height='20px'/></a>

A little visual in Python and PyGame to help me understand recursion using [Sierpinski triangles](https://en.wikipedia.org/wiki/Sierpinski_triangle) and [the Chaos Game method](https://en.wikipedia.org/wiki/Chaos_game).

## The Question
I started with a triangle from three randomly chosen points and then created a pyramid from four randomly chosen points.
![A screenshot of the triangle]() 
![A screenshot of the pyramid](https://github.com/vzhz/exploring_sierpinski_pyramids/blob/master/example_pyramid.png)

After creating this, I realized that I didn't really understand how the triangles were being constructed.  Since understanding recursion was the primary reason to build this, I wanted to slow down the construction of the triangle (just like we all do for online talks we don't understand), so I made a mode that slows the speed of construction and colored the points that are being used to give the new midpoint and the next point in the image.  
![A screenshot of the slower view of the triangle]()

## Installation
This program consists of one Python file that uses [PyGame](http://pygame.org/hifi.html), which you will need to [install](http://pygame.org/wiki/GettingStarted).

Let's get started!

###Clone this repo
Navigate to your home directory <code>/Users/*username*/</code> and clone this repo.

###Find your shell
Find your shell (e.g. you may be using [zshrc]() or bash) and download PyGame with <code>pip install pygame</code>.  You may then run the script by typing <code>python3 /Users/*username*/exploring_sierpinski_pyramids/sierpinski_draw.py</code> and responding to the prompts.

####Troubleshooting
If you aren't running this script on a mac or do not wish you install using pip, you will need to find [an alternative method for installing PyGame](http://pygame.org/wiki/GettingStarted).

Now you are ready to visualize some triangles!

##Find more
If you liked this demo and would like to solve similar problems, check out [Project Euler](https://projecteuler.net/) for over 500 brain-stretching challenges. 

##Contributing
We welcome your contrubutions in pretty much any form.  Create an issue or clone and go to town on a pull request.

##License
exploring_sierpinski_pyramids is released under [the MIT license](https://github.com/vzhz/friendly_terminal/blob/master/LICENSE.txt).

