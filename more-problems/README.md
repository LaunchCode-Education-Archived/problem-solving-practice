# More Coding Problems

These are rated at level 1-3:

- **Level 1** problems are the least complex. The typically involved 1-2 key concepts and are meant to built up to larger problems.
- **Level 2** problems have medium complexity. They often build on level 1 problems.
- **Level 3** problems are the most complex. They require you to synthesize multiple concepts, and contain multiple sub-problems. Solving these will most often require you to create multiple functions that solve a piece of the overall problem. These will test your problem-solving skills the most.

## String Problems

### Palindromes

- (Level 1) Write a function that takes a single string argument and returns a copy of the string:
    ```python
    # Should print "LaunchCode"
    print(copy("LaunchCode"))
    ```
- (Level 2) Write a function that takes a single string argument and returns the string, reversed:
    ```python
    #Should pring "edoChcnuaL"
    print(reverse("LaunchCode"))
- (Level 3) Write a function that checks whether or not a string is the same backwards as it is forwards.
    ```python
    # Should each print True
    print(is_symmetric("aabbaa"))
    print(is_symmetric("aba"))

    # Should each print False
    print(is_symmetric("abc"))
    print(is_symmetric("abc cbaa"))
    ```

### Filtering

- (Level 2) Write a function that takes two arguments, a string and a character (that is, a string of length 1), and removes all occurances of the character from the string.
    ```python
    # Should print "rdvrk"
    print(filter('aardvarkaaaaa', 'a'))
    ```
    This builds on the level 1 problem in the Palindrome section above.
- (Level 2) Write a function that takes two arguments, a string and a character, and counts the number of times the character occurs in the string.
    ```python
    # Should print 8
    print(count('aardvarkaaaaa', 'a'))
    ```
- (Level 2) Write a function that takes three arguments, a string and two characters. The function should return the result of replacing all occurances of the first character with the second.
    ```python
    # Should print "xxrdvxrkxxxxx"
    print(swap('aardvarkaaaaa', 'a', 'x'))
    ```
## Integer List Problems

- (Level 1) Write a function that takes a list of integers and prints each of the integers on a separate line.
- (Level 1) Write a function that takes three integers and prints the largest.
    ```python
    # Should each print 42
    print(largest_of_three(-1, 5, 42))
    print(largest_of_three(-1, 42, 5))
    print(largest_of_three(42, -1, 5))
    ```
- (Level 2) Write a function that takes a list of integers and prints the average.
- (Level 3) Write a function that takes a list of integers and returns the largest.
    ```python
    # Should print 42
    print(largest([-1, 5, 3, 42, 17, 42, 19]))
    ```

## Positive or Negative

- (Level 1) Write a program that asks the user for an integer and prints if it is positive or negative
- (Level 2) Write a program that prompts the user for 10 integers and prints only the positive ones
- (Level 3) Write a program that prompts the user for 10 integers. I should then ask the user if they want "positive" or "negative", and based on the response, prints the sum of all positive numbers or the sum of all negative numbers

## String Compression (Level 3)

Write a function `compress` that takes a single string argument that "compresses" it according to the following rules:

> When a character is repeated more than 2 times, such as 'aaa', replace it with '3a'.

For example, the string `"aaaaaabbbccccc"` will be compressed to be `"6a3b5c"`.

You may assume that the string doesn't contain any numbers, so that there is no ambiguity in the resulting string.

Then write a funciton `uncompress` that undoes this process. Be sure to run tests like:

```python
uncompressed_str = "aaaaaabbbccccc"
compressed_str = "6a3b5c"

# Should be True
print(uncompress(compress(uncompressed_str)) == uncompressed_str)

# Should also be True
print(compress(uncompress(compressed_str)) == compressed_str)
```

