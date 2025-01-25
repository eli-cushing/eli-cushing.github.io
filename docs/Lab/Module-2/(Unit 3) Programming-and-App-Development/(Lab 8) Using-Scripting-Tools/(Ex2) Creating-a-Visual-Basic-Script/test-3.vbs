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