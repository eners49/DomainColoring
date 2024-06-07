# DomainColoring

Graphing calculator for complex functions.

## Context

The number 𝑖 is defined as the square root of -1. Since 𝑖 doesn't exist anywhere on the number line, if we want to represent it, we need to create a separate axis for it, known as the imaginary axis. A number that contains i is called a complex number, having both a real and an imaginary part. Thus, we can use a two-dimensional space to represent one. We'll denote the real and imaginary axes as ℜ𝔢(x) and ℑ𝔪(x):

![mapping](https://github.com/eners49/DomainColoring/assets/32853967/c1ecf1b8-72c9-4855-b526-2c609360f040)

## How will we graph a complex function?

A function f(x): ℂ → ℂ can be effectively seen as taking in two arguments, the real and imaginary parts of x, and spitting out two arguments, the real and imaginary parts of the output. This means that we effectively need four dimensions to map a function. Since we don't have that many dimensions to work with, one alternative is to use domain coloring. By doing this, we "map" a complex number to a set of RGB values that corresponds to whatever the output of the function is.

One way to convert a complex number to a set of RGB values is to use the abs() and arg() complex functions. abs(x) takes the absolute value of x, while arg(x) denotes the angle between the positive real axis and x. This effectively stores a complex number in polar form. Since arg(x) ranges from 0 to 2π, we can represent it using the color wheel. Since abs(x) can range from 0 to ∞, we can use lightness to represent it. This means we can use a simplified form of the HSL color model to represent a complex number.

This program has two forms of graphing abs(x): "linear" mode and "continuous" mode. In "linear" mode, the color's lightness is directly proportional to the value, so a high value will have a lightness of 100%, while half that value will have a lightness of 50%, and so on. The program automatically calibrates the scale for this based on the range of the function. In "continuous" mode, the program uses the arctan function to assign a color for every number from 0 to infinity. 0 will have a brightess of 0%, 1 will have a brightness of 50%, and ∞ will have a brightness of 100%. "Continuous" mode is best used when "linear" mode doesn't fully capture the geometry of a function.

## Analysis

Below can be seen the graph of y = x² for real numbers and for complex numbers in "linear" graphing mode. The parabola from the first graph is still present in the second graph, but it's seen in the brightness of the pixels. The dark area in the center represents a low value, while the bright red near the ends of the real axis represent a high positive value and the bright blue near the ends of the complex axis represent a high negative value, with various complex numbers appearing everywhere else in the graph.

![image](https://github.com/eners49/DomainColoring/assets/32853967/9e31c21c-02bd-4bee-9243-75eccfb87480)

All in all, graphing functions like this isn't very useful a lot of the time, but graphing more complex functions can lead to really pretty graphs. These graphs can also be pieced together and used to create "trippy" animations.

## Gallery
