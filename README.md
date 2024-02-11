## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required modules.

```
pip install opencv-python
pip install python-magic (optional, for the png verification function)
pip install numpy
```

## Usage

```
In the main.py file, choose which function you would like to use, checker or applier, by commenting the other and then execute the script.
You will be asked to enter the source picture, just type in its name if it's in the same directory, otherwise, its source path. (For the example I used, I would type raid.jpg)
P.s : checker would just check if the picture meets the asked requirements and applier does add the necessary modification so that any picture may be used 
```

## My Thought process

```
At first, some of the instructions seemed a bit vague (especially the "happy" colors one), but after much thought and analysing the purpose of the code, I was able to deliver the following functions.
--  For the shape verification, everything is trivial, no need to dive into details.
--  For the colors verification, I had to open a color pallet and note down the RGB color code for the ones I considered happy, perhaps I'd find a pattern or something they all had in common. Finally, I came to the conclusion that the sum of the R,G and B values were considerably high (except for some shades of grey) and I chose 400 as a threshold value in order to consider a pixel "happy" and then I chose 65% as the happy pixels ratio in order to consider the whole picture colors "happy"
I also read online that another way to measure that happiness was throughout the picture's saturation level (the higher it is, the more vibrant the colors of the picture) and that's what I tried to do if a picture failed to pass the previous happiness test, in order to be able to use it, without distorting the colors as much.
--  The circle detection gave me the most trouble out of all the other functions. I had to look through the OpenCv documentation as well as some online forums to figure something out. The initial solutions detected weird and multiple circles and sometimes it would just draw an arc. But, by tweaking the circle radius parameters and only taking the circles whose origin is in the center of the image, I managed to obtain something that is rather acceptable.
Transforming the image into a circle however was a much lighter task, since all I had to do is define the circle myself and then make all the pixels outside of it transparent.

Overall, this was a fun and challenging task and I hope you will be happy with the result.
```