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

![func1](https://github.com/eners49/DomainColoring/assets/32853967/3a821276-f693-41cc-a468-d99f1a38bce7)
![func2](https://github.com/eners49/DomainColoring/assets/32853967/79558dbf-4294-4f24-b4e6-5fbd21df469d)
![func3](https://github.com/eners49/DomainColoring/assets/32853967/80921b3a-4ece-446a-afe6-45e6517f6745)
![func4](https://github.com/eners49/DomainColoring/assets/32853967/44eacd46-79a8-4ecf-b1a8-05f88626b86b)
![func5](https://github.com/eners49/DomainColoring/assets/32853967/d752a91a-dfe9-4557-b223-a66ab7303661)
![func6](https://github.com/eners49/DomainColoring/assets/32853967/6050e3a2-5c3d-4694-abfd-eb80aea6f195)
![func7](https://github.com/eners49/DomainColoring/assets/32853967/53198cb2-1231-49e2-92c8-23c6ea4595f0)
![func8](https://github.com/eners49/DomainColoring/assets/32853967/a198fa52-dd92-4e08-b243-baaa7428b6f7)
