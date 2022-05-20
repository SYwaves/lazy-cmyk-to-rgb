# LAZY APPROXIMATE CMYK TO RGB CONVERSION

This is a loosely weighted method of converting from CMYK to RGB while maintaining some semblance of perceptual similarity.

Traditional 'naive' formula I see on the internet is as follow:

> The red (R) color is calculated from the cyan (C) and black (K) colors:
> 
> R = 255 × (1-C) × (1-K)
> 
> The green color (G) is calculated from the magenta (M) and black (K) colors:
> 
> G = 255 × (1-M) × (1-K)
> 
> The blue color (B) is calculated from the yellow (Y) and black (K) colors:
> 
> B = 255 × (1-Y) × (1-K)

Which incorrectly maps the smaller CMYK gamut 1:1 with the larger RGB gamut, typically resulting in conversion into colors that the original CMYK format can not actually display.

This is not meant for any sort of serious work, as accuracy cannot be achieved without an ICC profile.
