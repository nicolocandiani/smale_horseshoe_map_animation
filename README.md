# Animation of Smale's Horseshoe map
Smale's Horseshoe map is a rather important example in the study of dynamical systems. 
This repository contains the code for the animation of the forward and backward iterates of the map, showing the evolution of the invariant set after $n$ iterations.



## Usage
The animation uses the [Manim](https://www.manim.community) library.
To install all required dependencies for installing Manim (namely: ffmpeg, Python, and some required Python packages), run:
```
brew install py3cairo ffmpeg
```
On Apple Silicon based machines, you might need to install some additional dependencies:
```
brew install pango scipy
```
Finally, to install Manim, run:
```
pip3 install manim
```
You can now run the animation. Feel free to change the number of iterations in the code itself.
To render the animation as a video, simply run:
```
manim -pqh final_scene.py
```
For further rendering options, please check the Manim documentation [here](https://docs.manim.community/en/stable/index.html).

---

Note: the point generation of the geometrical objects in the animation can definitely be further improved, with faster rendering and less memory consumption. Feel free to fork the project and improve it with your own ideas.  
