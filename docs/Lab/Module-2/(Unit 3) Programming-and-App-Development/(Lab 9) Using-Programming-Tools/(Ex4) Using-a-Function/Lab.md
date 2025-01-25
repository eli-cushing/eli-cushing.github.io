---
Module: 2: Using Apps and Databases
Unit: 3: Programming and App Development
Lab: 9: Using Programming Tools
Exercise: 4: Using a Function
---

# Lab 9

# Overview

We have used a few of Python's built-in functions to write our program. Functions are self-contained routines designed to accomplish a specific task. Functions can often be reused in different parts of the overall program.

While using this basic program, you may have noticed that some of the output is not grammatical. Rather than state "You are the 2 person I've met today," it would be better for the output to state "You are the 2nd person I've met today." To do this, we can use a function that returns the correct ordinal suffix ("th," "st," "nd," or "rd") for a given cardinal integer.

# Instructions

1. From the **File** menu, select **Open**. Click the **Documents** object, then double-click the **Python02** file.
   - The program code is opened in an editor window.

2. You can see the new function has been added in the first ten lines.
    - Note the use of `def` to declare the function and the use of indents to show which statements belong to the function
    - Other languages are more likely to use brackets to delimit the statements belonging within a function.
    The previous code has been assigned to the `main()` function.
    - The last line of code calls this `main()` function if the script is executed directly. This structure allows the file containing these functions to be imported by another module without necessarily running the `main()` code.

    > [!NOTE] You might think of `main()` as more procedure-like than function-like, but Python doesn't distinguish between functions and procedures. A Python function does not have to return a value. It's simply a means of defining a block of code.

3. Note that **line 1** contains a comment (`#`) with attribution for the source code that this function is derived from.

    >[!NOTE]The original function is more concise than this version. We've added an additional step to illustrate the use of some different code operations.

4. In **line 16**, note the way that the `ordinal_suffix()` function is called.
   - The function expects an integer as input (an argument).
   - The `main()` function is passing the value of the integer variable `counter` to the `ordinal_suffix()` function.

5. In **line 2**, we use an array-like construction to store the list of ordinal suffixes associated with 1, 2, and 3.
   - This type of Python list is called a **dictionary**.
   - Note that the list is declared outside of any function definition, making it available to any code in the same module.

6. Look at **line 3**.
   - The function assigns its own variable (`i`) to the integer value.
   - Note that `ordinal_suffix()` does not manipulate the value of the `counter` variable.

7. Look at the `if` conditional blocks in **lines 4-9** and make sure you understand what they do:

   - **First `if` statement**:
     - Checks whether the integer is over two digits long. If it is, it truncates it, using functions to convert between integer and string and back.
     - For example, if the value of `i` is 112, this statement will convert it to 12.
     - The code snippet `[-2:]` is a slice, which is the method used in Python to return part of a string (in this case, the last two characters). This is done because only the values from 0 to 99 need to be evaluated to determine the appropriate suffix.

   - **Second `if` statement**:
     - Checks whether `i` has the value of 11, 12, or 13 because in these special cases, the suffix is "th" (not "11st" or "12nd").
     - The code uses the comparison operator `less than (<)` to accomplish this.

   - **Else statement**:
     - Returns the correct suffix in any other case.
     - It uses the **mod operator (%)**, which returns the remainder after division. For example:
       - If `i` is 2, then the remainder after division by 10 is also 2.
       - If `i` is 22, the remainder is still 2.
     - The `get()` function is used to look up this remainder value in the `SUFFIX_DICT` list. If the value is not found (e.g., if it is 0 or 4), "th" is returned by default.

8. Use **F5** to run the new program and test that it returns correctly formatted suffixes in the output.

9. Change the value of `range(1,3+1,1)` to test different integers. For example, try `range(109,124,1)`.

10. Close all open windows and apps.
