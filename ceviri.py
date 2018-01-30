from appJar import gui
from textblob import TextBlob
import time
app = gui()

def press(button):
    if button == 'Translate':
         
        
        if not app.getEntry('Text:')== '':
            tx = app.getEntry('Text:')
            blob = TextBlob(tx)
            opt = app.getOptionBox('Options')
            text = blob.translate(to=opt) 
            app.infoBox('OK',text)
            
            app.addGridRow('g1',[tx,text])
    else:
        app.stop()
app.addLabelOptionBox('Options',['tr','en'],2,0)
app.addEntry('Text:',1,0)
app.addButton('Translate', press, 1, 1)
app.setEntrySticky('Text:','news')
app.addGrid('g1',[['Text','Translated']],3,0)
app.go()
