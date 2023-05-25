Learn C The Hard Way
=======

Exercise 23
----

Meet Duff's Device



The Plan
====

Learn the most evil awesome hack ever:

Duff's Device



The Code
====

Remember that this is *bad* code.
It's very interesting though, so struggle with it.



The Analysis
====

Before you continue, try to figure out what this does.
Consider it a debugging problem.



Clues
====

* Print this code out so that you can write on some paper.
* Write each of the variables in a table as they  look when they get initialized right before the ``switch-statement``.
* Follow the logic to the switch, then do the jump to the right case.
* Update the variables, including the ``to``, ``from``, and the
  arrays they point at.



Clues
====

* When you get to the ``while`` part or my ``goto`` alternative,  check your variables, and then follow the logic either back to the  top of the ``do-while`` or to where the ``again`` label is  located.
* Follow through this manual tracing, updating the variables, until you're sure you see how this flows.



Pause!
=====

I will then show you the solution so pause if you do
*NOT* want to see it yet.



Solving It
====

Watch me walk through how this works to see if it matches what you did.

>[code run on pythontutor](https://pythontutor.com/visualize.html#code=%23include%20%3Cstdio.h%3E%0A%23include%20%3Cstring.h%3E%0A%0A%0Aint%20normal_copy%28char%20*from,%20char%20*to,%20int%20count%29%20%7B%0A%20%20%20%20int%20i%20%3D%200%3B%0A%0A%20%20%20%20for%20%28i%20%3D%200%3B%20i%20%3C%20count%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20%20%20%20%20to%5Bi%5D%20%3D%20from%5Bi%5D%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20return%20i%3B%0A%7D%0A%0Aint%20duffs_device%28char%20*from,%20char%20*to,%20int%20count%29%20%7B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20int%20n%20%3D%20%28count%20%2B%207%29%20/%208%3B%0A%0A%20%20%20%20%20%20%20%20switch%28count%20%25%208%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20case%200%3A%20do%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20case%207%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20case%206%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20case%205%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20case%204%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20case%203%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20case%202%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20case%201%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%20while%28%20--n%20%3E%200%29%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%0A%20%20%20%20return%20count%3B%0A%7D%0A%0A%0Aint%20zeds_device%28char%20*from,%20char%20*to,%20int%20count%29%20%7B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20int%20n%20%3D%20%28count%20%2B%207%29%20/%208%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20switch%28count%20%25%208%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20case%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20again%3A%20%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20case%207%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20case%206%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20case%205%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20case%204%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20case%203%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20case%202%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20case%201%3A%20*to%20%2B%2B%20%3D%20*from%20%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20%28--n%20%3E%200%29%20goto%20again%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%0A%20%20%20%20return%20count%3B%0A%7D%0A%0Aint%20valid_copy%28char%20*data,%20int%20count,%20char%20expects%29%20%7B%0A%20%20%20%20int%20i%20%3D%200%3B%0A%20%20%20%20for%20%28i%20%3D%200%3B%20i%20%3C%20count%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20%20%20%20%20if%20%28data%5Bi%5D%20!%3D%20expects%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20printf%28%22%5B%25d%5D%20%25c%20!%3D%20%25c%22,%20i,%20data%5Bi%5D,%20expects%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20return%200%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%0A%20%20%20%20return%201%3B%0A%7D%0A%0A%0Aint%20main%28int%20argc,%20char%20*argv%5B%5D%29%20%7B%0A%20%20%20%20char%20from%5B31%5D%20%3D%20%7B'a'%7D%3B%0A%20%20%20%20char%20to%5B31%5D%20%3D%20%7B'c'%7D%3B%0A%20%20%20%20int%20rc%20%3D%200%3B%0A%0A%20%20%20%20//%20setup%20the%20from%20to%20have%20some%20stuff%0A%20%20%20%20memset%28from,%20'x',%2031%29%3B%0A%0A%20%20%20%20//%20set%20it%20to%20a%20failure%20mode%0A%20%20%20%20memset%28to,%20'y',%2031%29%3B%0A%0A%20%20%20%20valid_copy%28to,%2031,%20'y'%29%3B%0A%20%20%20%20//%20use%20normal%20copy%20to%0A%20%20%20%20//%20rc%20%3D%20normal_copy%28from,%20to,%2031%29%3B%0A%20%20%20%20//%20valid_copy%28to,%2031,%20%22x%22%29%3B%0A%20%20%20%20%0A%20%20%20%20//%20reset%0A%20%20%20%20memset%28to,%20'y',%2031%29%3B%0A%0A%20%20%20%20//%20duffs%20version%0A%20%20%20%20rc%20%3D%20duffs_device%28from,%20to,%2031%29%3B%0A%20%20%20%20//%20valid_copy%28to,%2031,%20%22x%22%29%3B%0A%0A%0A%20%20%20%20//%20reset%0A%20%20%20%20memset%28to,%20'y',%2031%29%3B%0A%0A%20%20%20%20//%20my%20version%0A%20%20%20%20rc%20%3D%20zeds_device%28from%20,%20to,%2031%29%3B%0A%20%20%20%20//%20valid_copy%28to,%2031,%20%22x%22%29%3B%0A%20%20%20%20return%201%3B%0A%7D&cumulative=false&curInstr=120&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=c_gcc9.3.0&rawInputLstJSON=%5B%5D&textReferences=false)

Extra Credit
====

* Never use this again.
* Go look at the Wikipedia entry for Duff's device and see if you can  spot the error.  Read the article, compare it to the version I have here, and try to understand why the Wikipedia code won't work for you  but worked for Tom Duff.
>[Duff's device on wiki](https://en.wikipedia.org/wiki/Duff%27s_device)
* Create a set of macros that lets you create any length of device like this. For example, what if you wanted to have 32 case statements and didn't want to write out all of them? Can you do a macro that lays down eight at a time?



Extra Credit
====

* Change the ``main`` to conduct some speed tests to see which one is  really the fastest.
* Read about ``memcpy``, ``memmove``, and ``memset``, and also compare  their speed.
* Never use this again!



End Of Lecture 23
=====



<!--  -->
## references
