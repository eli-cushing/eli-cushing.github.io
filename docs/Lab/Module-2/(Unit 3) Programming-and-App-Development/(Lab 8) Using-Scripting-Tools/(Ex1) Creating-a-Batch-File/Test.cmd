@echo off
ipconfig /all > report.txt
echo Press a key to view report
pause > nul
notepad report.txt