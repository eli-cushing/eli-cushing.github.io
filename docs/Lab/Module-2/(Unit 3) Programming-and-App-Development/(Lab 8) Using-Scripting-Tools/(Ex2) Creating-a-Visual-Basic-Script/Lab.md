---
Module: 2: Using Apps and Databases
Unit: 3: Programming and App Development
Lab: 8:  Using Scripting Tools
Exercise: 2: Creating a Visual Basic Script
---

# Lab 8

## Overview

In this exercise, you will create and test a Visual Basic script.

## Instructions

1. Press **START**, type notepad and then press **ENTER**.

2. In the Untitled – Notepad window, type the following text:

    ```vbscript
    for i = 1 to 5
        wscript.echo i
    next
    ```

    - This program creates a simple loop and uses the `echo` statement to show the current value of the variable `i` as the loop executes.

3. From the **File** menu, select **Save As**.

4. n the **Save as type** list, click **All Files**.

5. In the **File name** box, type
    `Test.vbs`.

6. In the navigation pane, click **Documents**.

7. Click **Save**.

8. Open Windows Explorer and navigate to your **Documents** folder.

9. Double-click the `Test.vbs` file.

10. The script runs and a new window opens that displays the number 1. Click **OK**, and then number 2 displays in a new window. Continue until 5 has displayed.

11. Click **Start**, scroll down and expand **Windows System**, and then click **Command Prompt**.

12. In the command prompt window, type the following then press **ENTER**:

    `cscript documents\test.vbs`

13. The script runs from the command line and displays each number in sequence.

14. Switch to the Notepad window and update the script to read as shown below:

    ```vb
    iHigh = 50
    iLow = 10
    for i = 1 to 5
        randomize
        iDisplay = int((iHigh - iLow + 1) * rnd + iLow)
        wscript.echo iDisplay
    next
    ```

15. Save the file.
    - This script uses some additional integer variables and built-in VBscript functions to return a random number between 10 and 50 during each iteration of the loop.

16. In the command prompt window, type the following then press enter:

    `cscript documents\test.vbs`

    > Five random numbers between 10 and 50 display.

17. What part of the code would you change to show 10 random numbers?

18. Edit this line and save the file:

    ```vb
    for i = 1 to 10
    ```

19. Run the script again.

20. Switch to the Notepad window and update the script to read as shown below:

    ```vb
    iHigh = 50
    iLow = 10
    iCount = 0
    sTitle = "Number count"
    for i = 1 to 10
        randomize
        iDisplay = int((iHigh - iLow + 1) * rnd + iLow)
        wscript.echo iDisplay
        if iDisplay > 25 then
            iCount = iCount + 1
        end if
    next
    sMsg = cstr(iCount) + " numbers are greater than 25"
    msgbox sMsg,vbOK,sTitle
    ```

21. Save the file.

    These modifications introduce several key features:

    - **Branching Statements**:
        - A branch increments a variable (`iCount`) if another variable exceeds a certain value.
        - The branching statements are **nested**, allowing for more complex logic within the loop.

    - **String-Type Variables and Conversion**:
        - The integer variable `iCount` is converted to a string using a function for use in a message box.
        - String variables are essential for creating readable and user-friendly output.

    - **Use of `vbOK`**:
        - `vbOK` is a **constant** used in the message box function.
            - It defines the type of message box to display (one with just an OK button).

22. In the command prompt window, run the script.

23. Close all open apps and windows.
