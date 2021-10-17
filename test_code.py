# -*- coding: utf-8 -*-
#!/usr/bin/env python

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Feb 26 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################


from MacLabelPrint import MyLabel as pl
import wx

#
# ###########################################################################
# ## Class MyPrint
# ###########################################################################
#



class MyLabel(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Label Creator", pos=wx.DefaultPosition,
                          size=wx.Size(400, 400), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        bSizer9.Add(bSizer12, 0, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_StaticText1 = wx.StaticText(self, wx.ID_ANY, u"", wx.DefaultPosition)

        bSizer13.Add(self.m_StaticText1, 0, wx.ALIGN_LEFT, 5)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 300), wx.TAB_TRAVERSAL)

        self.m_panel4.SetBackgroundColour(wx.Colour(254, 254, 254))

        bSizer13.Add(self.m_panel4, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer9.Add(bSizer13, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        bSizer9.Add(bSizer14, 0, wx.EXPAND, 5)

        bSizer8.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_button_print = wx.Button(self.m_panel3, wx.ID_ANY, u"Create Label", wx.DefaultPosition, wx.DefaultSize, 0)

        bSizer11.Add(self.m_button_print, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel3.SetSizer(bSizer11)

        self.m_panel3.Layout()

        bSizer11.Fit(self.m_panel3)

        bSizer10.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        bSizer8.Add(bSizer10, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer8)

        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button_print.Bind(wx.EVT_BUTTON, self.make_label)
        self.Show()



    def make_label(self, event):

        label_width = 400
        label_height = 200

        # format is, lines: label text to print, lbl_x, lbl_y, font_size, font_weight
        label_data = {
            "l1":["+",15,15,30,wx.FONTWEIGHT_NORMAL],
            "l2": ["Line 1 at x=60 y=20 font=18 Bold", 60, 25, 18, 700],
            "l3": ["line 2 at x=60 y=60 font=16 Normal", 60, 60, 16, wx.FONTWEIGHT_NORMAL],
            "l4": ["Line 3 at x=20 y=100 font=10 Normal", 20, 100, 10, wx.FONTWEIGHT_NORMAL],
            "l5": ["Line 4 at x=20 y=120 font=8 Normal", 20, 120, 8, wx.FONTWEIGHT_NORMAL],
            "l6": ["Line 5 at x=20 y=160 font=12 Normal", 20, 160, 12, wx.FONTWEIGHT_NORMAL],
        }

        pl(None, label_data, label_width, label_height)
        # pl(None, label_data)


if __name__ == '__main__':
    app = wx.App()
    frame = MyLabel(None)
    app.MainLoop()

