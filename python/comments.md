# unique string.ipynb
## Efficiency
+ https://docs.python.org/2/library/string.html#string.count counts the occurrences of a substring in string. 
In the worst case we'll have to call this function `N` times as `N` is the length of the input string.
Then the complexity of the function `unique(string)` will be `O(N^2)` which is not efficient.
We expect the complexity `O(N)`.
+ `string[i] in seen:` the complexity of checking whether an item belongs to a list is `O(N)`.
If we replace the data type of variable `seen` from List to Set, the complexity would become only `O(1)`.
Reference: https://wiki.python.org/moin/TimeComplexity

## Coding style
+ A more pythonic way to loop through all characters of a string: `for character in string:`
+ `if string[i] in seen:` not `if string[i] in seen :`, there's no empty space between the last character `n` and the colon `:`
+ `if unique2(string2) == False:` is usually written as `if not unique2(string2):`
