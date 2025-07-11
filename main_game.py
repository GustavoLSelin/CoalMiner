#!/usr/bin/env python
import wx

class CoalMiner(wx.Frame):

    carvao = 0

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, "Coal Miner", size = (500,500))
        panel = wx.Panel(self)
        self.quote = wx.StaticText(panel, label=" -=-=-=- Informacoes do estoque -=-=-=-", pos=(10, 20))
        self.quote = wx.StaticText(panel, label="Qtd. Carvao: ", pos=(15, 25))
        self.Show()

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
CoalMiner(None)
app.MainLoop()