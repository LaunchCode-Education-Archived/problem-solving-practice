# Shapes

These problems are variations on a theme. Each will have you return a string that consists of a shape built out of `#` (hash) characters.

1. Write a function `line(n)` that returns a line with exactly `n` hashes.
    ```python
    print(line(5))
    ```
    **Output:**
    ```
    #####
    ```
1. Write a function `square(n)` that returns an `n` by `n` square of hashes. Use your `line` function to do this.
    ```python
    print(square(5))
    ```
    **Output:**
    ```
    #####
    #####
    #####
    #####
    #####
    ```
1. Write a function `rectangle(width, height)` that returns a rectangle with width and height given by the parameters. Use your `line` function to do this.
    ```python
    print(rectangle(5, 3))
    ```
    **Output:**
    ```
    #####
    #####
    #####
    ```
    Now, go back and rewrite `square` to use `rectangle`.
1. Write a function `stairs(n)` that prints the pattern shown below, with height `n`. Use your `line` function to do this.
    ```python
    print(stairs(5))
    ```
    **Output:**
    ```
    #
    ##
    ###
    ####
    #####
    ```
1. Write a function `space_line(spaches, hashes)` that returns a line with exactly the specified number of spaces, followed by the specified number of hashes.
    ```python
    space_line(3, 5)
    ```
    **Output:**
    ```
       #####
    ```
1. Write a function `stairs_reverse(n)` that works like your `stairs` function, but returns the mirror image.
    ```python
    print(stairs_reverse(5))
    ```
    **Output:**
    ```
        #
       ##
      ###
     ####
    #####
    ```
1. Write a function `sideways_triangle(n)` that returns a sideways triangle with height `n`.
    ```python
    print(sideways_triangle(5))
    ```
    **Output:**
    ```
    #
    ##
    ###
    ####
    #####
    ####
    ###
    ##
    #
    ```
1. Write a function `triangle(n)` that returns an upright triangle of height `n`.
    ```python
    print(triangle(5))
    ```
    **Output:**
    ```
        #
       ###
      #####
     #######
    #########
    ```
1. Write a function `diamond(n)` that returns a diamond where the triangle formed by the top portion has height `n`. Notice that this means the diamond has `2n - 1` rows.
    ```python
    print(diamond(5))
    ```
    **Output:**
    ```
        #
       ###
      #####
     #######
    #########
     #######
      #####
       ###
        #
    ```
