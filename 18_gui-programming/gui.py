#!/usr/bin/env python

import wx

def sayHello(event):
	#print "hello world!"
	#textArea.SetValue("hello World!")
	labelValue = myLable.GetValue()
	textArea.AppendText(" Hello "+labelValue)
app = wx.App()

frame = wx.Frame(None, title="hello world!", size=(400,400))
frame.Show()

helloButton = wx.Button(frame, label='say hello!', pos=(160,20), size=(80,20))
helloButton.Bind(wx.EVT_BUTTON, sayHello)

textArea = wx.TextCtrl(frame, style=wx.TE_MULTILINE, pos=(20,100), size=(360, 250))

myLable = wx.TextCtrl(frame, pos=(10,40), size=(140,20))


app.MainLoop()