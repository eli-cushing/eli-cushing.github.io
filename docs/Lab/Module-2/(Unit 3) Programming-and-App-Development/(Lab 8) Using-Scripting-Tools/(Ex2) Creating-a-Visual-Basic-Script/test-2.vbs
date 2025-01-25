iHigh = 50
iLow = 10
for i = 1 to 5
    randomize
    iDisplay = int((iHigh - iLow + 1) * rnd + iLow)
    wscript.echo iDisplay
next