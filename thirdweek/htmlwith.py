
import webbrowser
import os
f = open('index4.html', 'r')
f.read()
f.close()

filename = 'file:///'+os.getcwd()+'/' + 'index4.html'
webbrowser.open_new_tab(filename)
