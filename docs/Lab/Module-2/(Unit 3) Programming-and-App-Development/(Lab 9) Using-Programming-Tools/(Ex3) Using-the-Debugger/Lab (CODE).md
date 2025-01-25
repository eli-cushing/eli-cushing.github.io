---
Module: 2: Using Apps and Databases
Unit: 3: Programming and App Development
Lab: 9: Using Programming Tools
Exercise: 3: Using the Debugger
Env: VSCode
---

# Lab 9

## Overview

When your program doesn't work as expected, it is helpful to "debug" it. Debugging means stepping through your code to see how the program is running and check the values of variables at different points in the program. VS Code provides an easy-to-use debugger to help you with this process.

## Instructions

1. **Open your Python file in VS Code**:
   Launch **VS Code** and open the Python file you want to debug (the file containing the code with the issue).

2. **Set breakpoints**:
   Breakpoints allow the program to pause at certain points so you can inspect its behavior.
   - Find the **line 5** where the `for` loop starts. Click in the left margin next to line 5. A red dot will appear, indicating a breakpoint.
   - Now, find **line 7**, which is the last line inside the loop. Click in the left margin next to line 7 to add another red dot (breakpoint).

3. **Open the Run and Debug Panel**:
   - Click on the **Run and Debug** icon on the left side Activity Bar (the sidebar on the left) or press `Ctrl + Shift + D` to open the Debug panel.
   - In the dropdown at the top of the Debug panel, select **Python: Current File**.

4. **Start debugging**:
   - Press **F5** or click the green play button in the Debug panel. This will run the program in debugging mode.
   - The program will pause at the first breakpoint (on line 5).

5. **Step through the code**:
   - Once the program is paused at line 5, click the **Step Over** button (a curved arrow). This lets the program execute one line at a time without entering any functions.
   - As you step through the code, the **VARIABLES** pane will show the current values of the variables (e.g., `user_name` and `counter`).

6. **Respond to input prompts**:
   - If the program pauses at an input prompt (for example, asking "What’s your name?"), switch to the terminal at the bottom of VS Code.
   - Type your response (e.g., your name) and press **ENTER** to continue.

7. **Observe the variables**:
   - While stepping through the code, keep an eye on the **VARIABLES** pane in the Debug panel. This shows the current values of variables like `user_name` and `counter`.
   - This is useful for understanding how the program is changing as it runs.

8. **Continue debugging**:
   - Use the **Step Into** button (a downward arrow) if you want to go inside a function to see how it works.
   - If you're done with a function and want to return to the main program, click the **Step Out** button (an upward arrow).

9. **Fix the range issue in the loop**:
   If the loop doesn't run the right number of times, you can adjust the range. Modify the loop like this:

   ```python
   for counter in range(1, 4, 1):  # This will loop 3 times (1, 2, 3)
   ```

   - This will make the loop run 3 times instead of just 2.
   - After making the change, **save the file** by pressing `Ctrl + S`.

10. **Re-run the debugger**:
    - Press **F5** again to restart debugging and see if the loop runs the correct number of times.
    - Use **Step Over** to check if the program behaves as expected.

11. **Review debugging tools**:
    Here are the main debugging actions you can use:
    - **Go**: Continue running the program normally, stopping only at breakpoints.
    - **Step Into**: Move through the next line of code, entering functions.
    - **Step Over**: Move through the next line of code without entering functions.
    - **Step Out**: Exit the current function and return to the main program.

12. **Close VS Code**:
    When you're done with debugging, close VS Code.

## Notes

- **Breakpoints**: Use breakpoints to pause the program at specific lines for closer inspection.
- **Variables Pane**: Watch the **VARIABLES** pane to see how the values of variables change as you step through the code.
- **Terminal Interaction**: When the program asks for input (like a name), respond directly in the terminal at the bottom of VS Code.

VS Code provides a much more modern and flexible debugging experience compared to IDLE. You can use this tool to understand your code better and catch logic errors early.
