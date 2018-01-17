from appJar import gui
from textblob import TextBlob
app=gui()
app.setBg("green")
app.setFont("10")

def press(button):
    if button=='ok':
        tx=app.getEntry('Ceviri:')
        blob=TextBlob(tx)
        opt=app.getOptionBox("Options")
        text=blob.translate(to=opt)
        print text 
        app.infoBox('ok', text)
    else:
        app.stop()
app.addLabelOptionBox("Options",["tr","en"])
app.addLabelEntry('Ceviri:')
tx=app.getEntry('Ceviri:')
app.addButtons(['ok','cancel'],press)

app.go()
