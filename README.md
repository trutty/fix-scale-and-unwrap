fix-scale-and-unwrap
====================

This is a simple add-on to fix the scale and unwrap multiple object with a single click of a button.
As I did not found any blender functionality which fulfilled these need (macros did not do the job) and also I had a lot of object to apply the stated operations on, I wrote this add-on.

What it does
------------

It will perform the following steps in order:

1. Set active object to the one selected. If multiple objects are selected it will iterate over every item.
2. Apply fix scale to the active object
3. Open the object in edit mode
4. Select the whole mesh
5. Unwrap everything (seams should already be marked)
6. Go back in object mode
7. If multiple objects are selected, go back to step 1
8. Report if every item was processed

Feedback
--------

As this is my first Blender add-on and therefore may not represents the best implementation, I am thankful for every feedback and best practices on the style, implementation and the code itself.
