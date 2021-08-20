# My solutions to the Google Foobar Challenge

## Problem 1: Braille Translation

Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions. 
But she never bothered to follow intergalactic standards for workplace accommodations, so those minions 
have a hard time navigating her space station. You figure printing out Braille signs will help them, and - 
since you'll be promoting efficiency at the same time - increase your chances of a promotion.

Braille is a writing system used to read by touch instead of by sight. 
Each character is composed of 6 dots in a 2x3 grid, where each dot can either be a bump or be flat (no bump). 
You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda's 
command can feel the bumps on the signs and "read" the text with their touch. The special printer which can print 
the bumps onto the signs expects the dots in the following order:

```
1 4
2 5
3 6
```

So given the plain text word "code", you get the Braille dots:

```
11 10 11 10
00 01 01 01
00 10 00 00
```

where 1 represents a bump and 0 represents no bump. Put together, code becomes the output string 100100101010100110100010.

Write a function answer(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the 
bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle
capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. 
All signs on the space station are less than fifty characters long and use only letters and spaces.\

### Test Cases:

#### Test Case 1:

Inputs:

```
"code"
```

Outputs:

```
"100100101010100110100010"
```

#### Test Case 2:

Inputs:

```
"Braille"
```

Outputs:

```
"000001110000111010100000010100111000111000100010"
```

### Test Case 3:

Inputs:

```
"The quick brown fox jumped over the lazy dog"
```

Outputs:

```
"000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100100010100110000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
```

## Problem 2: 

When you went undercover in Commander Lambda's organization, you set up a coded messaging system with Bunny Headquarters to allow them to send you 
important mission updates. Now that you're here and promoted to Henchman, you need to make sure you can receive those messages 
- but since you need to sneak them past Commander Lambda's spies, it won't be easy!

Bunny HQ has secretly taken control of two of the galaxy's more obscure numbers stations, and will use them to broadcast lists of numbers. 
They've given you a numerical key, and their messages will be encrypted within the first sequence of numbers that adds up to that key within 
any given list of numbers.

Given a non-empty list of positive integers l and a target positive integer t, write a function answer(l, t) which verifies if there is at 
least one consecutive sequence of positive integers within the list l (i.e. a contiguous sub-list) that can be summed up to the given target 
positive integer t (the key) and returns the lexicographically smallest list containing the smallest start and end indexes where this sequence 
can be found, or returns the array [-1, -1] in the case that there is no such sequence (to throw off Lambda's spies, not all number broadcasts 
will contain a coded message).

For example, given the broadcast list l as [4, 3, 5, 7, 8] and the key t as 12, the function answer(l, t) would return the list [0, 2] because the 
list l contains the sub-list [4, 3, 5] starting at index 0 and ending at index 2, for which 4 + 3 + 5 = 12, even though there is a shorter sequence 
that happens later in the list (5 + 7). On the other hand, given the list l as [1, 2, 3, 4] and the key t as 15, the function answer(l, t) would 
return [-1, -1] because there is no sub-list of list l that can be summed up to the given target value t = 15.

To help you identify the coded broadcasts, Bunny HQ has agreed to the following standards:

* Each list l will contain at least 1 element but never more than 100.
* Each element of l will be between 1 and 100.
* t will be a positive integer, not exceeding 250.
* The first element of the list l has index 0.
* For the list returned by answer(l, t), the start index must be equal or smaller than the end index

Remember, to throw off Lambda's spies, Bunny HQ might include more than one contiguous sublist of a number broadcast that can be 
summed up to the key. You know that the message will always be hidden in the first sublist that sums up to the key, so answer(l, t) 
should only return that sublist.

### Test Cases:
```
Inputs: 
    (int list) l = [4, 3, 10, 2, 8] 
    (int) t = 12
```

```
Output: 
    (int list) [2, 3]
```

```
Inputs: 
    (int list) l = [1, 2, 3, 4] 
    (int) t = 15 
```

```
Output: 
    (int list) [-1, -1]
```

## Problem 3:

Keeping track of Commander Lambda's many bunny prisoners is starting to get tricky. You've been tasked with writing a program to match bunny prisoner IDs to cell locations.

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the prison blocks have an unusual layout. They are stacked in a triangular shape, and the bunny prisoners are given numerical IDs starting from the corner, as follows:

```
| 7
| 4 8
| 2 5 9
| 1 3 6 10
```

Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground. 

For example, the bunny prisoner at (1, 1) has ID 1, the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been taking a LOT of prisoners). 

Write a function answer(x, y) which returns the prisoner ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the prisoner ID can be very large, return your answer as a string representation of the number.

### Test Cases:

``` 
Inputs:
    (int) x = 3
    (int) y = 2
```

```
Outputs:
    (string) "9"
```

```
Inputs:
    (int) x = 5
    (int) y = 10
```

```
Output:
    (string) "96"
```

## Problem 4:

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber 
is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' 
access codes, but only she knows how to figure out which of several lists contains the access codes. You need to find a way to determine which 
list contains the access codes once you're ready to go in. 

Fortunately, now that you're Commander Lambda's personal assistant, she's confided to you that she made all the access codes "lucky triples" in 
order to help her better find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With 
that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready 
to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

Write a function answer(l) that takes a list of positive integers l and counts the number of "lucky triples" of (lst[i], lst[j], lst[k]) where 
i < j < k.  The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The answer fits within a 
signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0. 

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.


### Test Cases:

```
Inputs:
    (int list) l = [1, 1, 1]
```

```
Output:
    (int) 1
``` 

```
Inputs:
    (int list) l = [1, 2, 3, 4, 5, 6]
```

```
Output:
    (int) 3
```

## Problem 5:

Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly.

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.

The fuel control mechanisms have three operations:

1. Add one fuel pellet
2. Remove one fuel pellet
3. Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called answer(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:

```
answer(4) returns 2: 4 -> 2 -> 1  
answer(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
```

### Test Cases:
```
Inputs:
    (string) n = "4"
```

```
Output:
    (int) 2
```

```
Inputs:
    (string) n = "15"
```

```
Output:
    (int) 5
```
