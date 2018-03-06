from appJar import gui


def dollars_and_cents(x):
    currency = '${:,.2f}'.format(x)
    return currency


def decrement(btn):
    """
    NOTE:
    Bill total prints the correct format however the tip is still
    returning a float.
    """
    app.setEntry("Tip", app.getEntry("Tip") - 1)
    app.setLabel("Tip Total", app.getEntry("Tip") * app.getEntry("Bill") / 100)
    app.setLabel("Bill Total", dollars_and_cents(app.getEntry("Bill") + app.getLabel("Tip Total")))


def increment(btn):
    """
    NOTE:
    Bill total prints the correct format however the tip is still
    returning a float.
    """
    app.setEntry("Tip", app.getEntry("Tip") + 1)
    app.setLabel("Tip Total", app.getEntry("Tip") * app.getEntry("Bill") / 100)
    app.setLabel("Bill Total", dollars_and_cents(app.getEntry("Bill") + app.getLabel("Tip Total")))


app = gui("Tip Calculator", "800x400")
app.setFont(30)

app.addLabel("Bill", "Bill")
app.setLabelAlign("Bill", "left")
app.addNumericEntry("Bill")
app.setEntryAlign("Bill", "center")
app.addLabel("Tip", "Tip %")
app.setLabelAlign("Tip", "left")
app.addNumericEntry("Tip")
app.setEntry("Tip", 15)
app.setEntryAlign("Tip", "center")
app.addButtons(["-", "+"], [decrement, increment])
app.setButtonFont(20, font=None)
app.addLabel("Amount to tip", "Tip Amount", 0, 2)
app.addLabel("Tip Total", str(0), 1, 2)
app.addLabel("Total", "Total", 2, 2)
app.addLabel("Bill Total", str(0), 3, 2)

app.go()