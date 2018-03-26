# Python 3.6.3

"""
NOTE:
The line of code "app.setLabel("Tip Total", app.getEntry("Tip") * app.getEntry("Bill") / 100)"
is executed once to insure the proper calculation is made and then twice to format that
calculation using the dollars_and_cents function.
"""


from appJar import gui


def dollars_and_cents(x):
    currency = '${:,.2f}'.format(x)
    return currency


def decrement(btn):
    app.setEntry("Tip", app.getEntry("Tip") - 1)
    app.setLabel("Tip Total", app.getEntry("Tip") * app.getEntry("Bill") / 100)  # calculation
    app.setLabel("Bill Total", dollars_and_cents(app.getEntry("Bill") + app.getLabel("Tip Total")))
    app.setLabel("Tip Total", dollars_and_cents(app.getEntry("Tip") * app.getEntry("Bill") / 100))  # formatting


def increment(btn):
    app.setEntry("Tip", app.getEntry("Tip") + 1)
    app.setLabel("Tip Total", app.getEntry("Tip") * app.getEntry("Bill") / 100)  # calculation
    app.setLabel("Bill Total", dollars_and_cents(app.getEntry("Bill") + app.getLabel("Tip Total")))
    app.setLabel("Tip Total", dollars_and_cents(app.getEntry("Tip") * app.getEntry("Bill") / 100))  # formatting


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
app.addLabel("Tip Total", 0, 1, 2)
app.addLabel("Total", "Total", 2, 2)
app.addLabel("Bill Total", 0, 3, 2)

app.go()
