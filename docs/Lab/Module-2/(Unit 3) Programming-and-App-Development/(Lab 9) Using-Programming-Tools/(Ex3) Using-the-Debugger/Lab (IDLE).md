---
Module: 2: Using Apps and Databases
Unit: 3: Programming and App Development
Lab: 9: Using Programming Tools
Exercise: 3: Using the Debugger
Env: Python IDLE (v3.12.8)
---

# Lab 9

## Overview

If you need to identify a logic error in code, it is often necessary to step through program execution. Using a debugger, you can pause execution and view the values of variables at the time a particular statement is being executed.

## Instructions

1. In the editor window, right-click **line 5** (the first statement in the `for` loop) and select **Set Breakpoint**.
   - The line is highlighted in yellow.
   - A breakpoint means that code execution will always pause at the line when the debugger is active.

2. In the editor window, right-click **line 7** (the last line) and select **Set Breakpoint**.

3. In the shell window, select **Debug > Debugger**.
   - A **Debug Control** window opens, and the shell shows the message "DEBUG ON."

4. In the editor window, press **F5** to run the program.

    Because debug control is active, you now need to start execution manually.

5. In the **Debug Control** window, click the **Step** button.
   - The first line of the program is executed.
   - Note that `user_name` is added to the list of locals (variables).

6. Click the **Step** button.
   - The debugger starts executing the `print()` function, calling an `idlelib.run.write()` function to do so.
   - We don't necessarily need to view every sub-step in this—as a built-in function, we can assume that it works correctly.

7. Click the **Out** button.
   - Using **Step Out** completes processing of the function and advances execution to the next statement (line 3).

8. Click the **Over** button.
   - Using **Step Over** processes the statement without pausing for each part of any functions it contains.
   - Note that program execution is still paused on **line 3**, as the `input()` function is waiting for user input.
   - Note that the debugger buttons are greyed out.

9. Switch to the **shell window**, click at the prompt, type any name, and press **ENTER**.

10. In the **Debug Control** window, note the new value of the `user_name` variable. Click the **Go** button.
    - Program execution is next halted by the breakpoint you set for **line 5**.
    - Note that the `counter` variable is now listed, with the value `1`.

11. Click the **Go** button.

12. Switch to the **shell window**, click at the prompt, type any name, and press **ENTER**.

13. In the **Debug Control** window, click the **Out** button.

14. Switch to the **shell window**, click at the prompt, type any name, and press **ENTER**.

15. In the **Debug Control** window, click the **Out** button.
    - Note the value of `counter` as the program exits the loop and processes **line 7**.

    > Can you explain why the loop only executes twice?
    The Python `range()` function is consistent with zero-based indexing. For example, an array with 10 elements includes the items 0,1,2,3,4,5,6,7,8, and 9 but not 10. The `range()` function is upper-bound exclusive, and the range we have used does not include the value `3`.
    To make the `range()` function work inclusively, you can add one to the stop value. Alternatively, you could set the stop value to `4`, but adding one makes the intent of the code clearer.

16. In the editor window, change the line to read as follows:

    ```python
    for counter in range(1, 3 + 1, 1):
    ```

17. Save the file, then press **F5** to run it again.

18. Step through the program to confirm that the loop executes three times.

    >[!NOTE] Another option would be to define a different variable to store the number of times the program has "met" someone. This might make the code easier to understand at the expense of making it a bit longer.

19. Take a moment to review the use of the debug tools:

    - **Go**: Continue execution normally (unless a breakpoint is hit).
    - **Step**: Advance through statements and functions step-by-step (often referred to as "Step Into").
    - **Over**: Execute the next statement without "following" any function calls.
    - **Out**: Complete any remaining parts within a function and pause at the next statement in the main program flow.

20. Close the Python editor window.

21. In the **shell window**, select **Debug > Debugger**.
    - The debugger is disabled.
