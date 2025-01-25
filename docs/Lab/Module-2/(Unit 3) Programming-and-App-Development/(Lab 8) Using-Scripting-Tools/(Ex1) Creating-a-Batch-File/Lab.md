---
Module: 2: Using Apps and Databases
Unit: 3: Programming and App Development
Lab: 8:  Using Scripting Tools
Exercise: 1: Creating a Batch File
---

# Lab 8

## Overview

In this lab, you will practice creating scripts in three different Windows scripting environments.

## Instructions

In this exercise, you will create a simple batch file to automate the creation of a report of the local host's network configuration.

1. If necessary, start your computer and sign in.

2. Press **START**, type **notepad**, and then press **ENTER**.

3. In the **Untitled – Notepad** window, type the following text:

    ```batch
    @echo off
    ipconfig /all > report.txt
    echo Press a key to view report
    pause > nul
    notepad report.txt
    ```

    **Note the features of the script:**

   1. `@echo off`: Hides command output in the terminal.
   2. `ipconfig /all > report.txt`: Saves network details to `report.txt`.
   3. `echo Press a key to view report`: Displays a prompt to press a key.
   4. `pause > nul`: Waits for a key press, hiding "Press any key to continue...".
   5. `notepad report.txt`: Opens `report.txt` in Notepad.

4. From the **File** menu, select **Save As**.

5. In the **Save as type** list, click **All Files**.

6. In the **File name** box, type `test.cmd`.

7. In the navigation pane, click **Documents**.

8. Click **Save**.

9. Close Notepad.

10. Click **Start**, scroll down and expand **Windows System**, and then click **Command Prompt**.

11. In the command prompt window, type:

    ```cmd
    documents\test.cmd
    ```

    Then press **ENTER**.

12. When prompted to press a key, press **SPACEBAR**.
    - A Notepad window opens and displays the output from the `ipconfig.exe` command that you put in your batch file.

13. Close all open windows and apps.
