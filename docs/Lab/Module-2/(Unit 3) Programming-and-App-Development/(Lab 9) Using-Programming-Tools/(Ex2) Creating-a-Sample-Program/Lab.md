---
Module: 2: Using Apps and Databases
Unit: 3: Programming and App Development
Lab: 9: Using Programming Tools
Exercise: 2: Creating a Sample Program
---

# Lab 9

## Overview

In this exercise, you will use the shell and editor windows of Python's Integrated Development Environment (IDLE). You will also identify some basic code constructs in a simple program.

## Instructions

1. Click in the **Instant Search** box and type `idle`. From the search results, click **IDLE (Python 3.x 32-bit)**.
   - The Python shell window opens. The shell window is used to interpret and run Python scripts and programs during development.

2. Type the following function. As you type, note how tooltips appear to help you complete the statement and how color-coding is used to validate your syntax (purple for the function name and green for the string input):

   ```python
   print('Hello World')
   ```

3. Press **ENTER** to execute the statement.
   - The string "Hello World" is "printed" as output to the shell.

4. From the **File** menu, select **Open**. Click the **Documents** object, then double-click the **Python01** file.

5. Take a few moments to identify what each line of this program does. The line position of the cursor is shown in the status bar, or you can press **ALT+G** to select a particular line:
   - **Line 1**: Declares a variable (`user_name`) and sets it to the string value `"World."`
   - **Line 2**: Uses the `print()` function we saw earlier, but the output is constructed from both static strings and the variable we declared.
     - Note the use of the **+** sign to concatenate (join together) string literals and variables.
     - Double quotes (`"`) are used to delimit the literal strings. This allows the single quote (`'`) to be used as an apostrophe within the string.
   - **Line 3**: Uses the `input()` function to set the variable to a value entered by the user.
   - **Line 4**: Sets up a loop using the `for` statement. A variable named `counter` is used to track progress through the loop. The `range()` function sets an initial value of 1, an exit value of 3, and a step value of 1.
     - The intention is to run the loop three times, but as we shall see, the current code might not accomplish that.
     - Note the use of a colon (`:`) to complete the line containing the `for` statement. While "For" type constructs in general are common to all programming languages, this statement syntax is specific to Python.
     - It will often be the case that you may understand the general operation of logic components but will need to learn the specific syntax of different development languages.
   - **Lines 5 and 6**: Executed during the loop. These lines are indented, as Python uses indentation to structure code, which is critical to compilation and execution.
     - In many other programming languages, indentation is used for clarity but whitespace is ignored by the interpreter or compiler.
     - In **line 5**, note the use of the `str()` function to convert the integer variable `counter` to a string data type.
   - **Line 7**: Executed once the loop has completed and is the final statement in the procedure.

6. Press **F5** to execute the program.

7. In the shell window, respond to the prompts by typing any names you wish and pressing **ENTER**.

8. Count how many times the loop executes—is this a surprise?

9. Leave all the Python windows open.
