# -*- coding: utf-8 -*-
#!/usr/bin/env python

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Feb 26 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import pyscreeze as pyscreeze
import subprocess


###########################################################################
## Class MyPrint
###########################################################################

class MyLabel(wx.Frame):

    def __init__(self, parent, line={"lin1": ["Default Label", 150, 85, 16, wx.FONTWEIGHT_NORMAL]},lbl_w=400, lbl_h=200, ln1_x=20, ln1_y=10):
        self.__lbl_w = lbl_w
        self.__lbl_h = lbl_h
        self.__ln_x = ln1_x
        self.__ln_y = ln1_y
        self.__line = line

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Label", pos=wx.DefaultPosition,
                          size=wx.Size(self.__lbl_w + 100, self.__lbl_h + 100), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        bSizer9.Add(bSizer12, 0, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_StaticText1 = wx.StaticText(self, wx.ID_ANY, u"", wx.DefaultPosition)

        bSizer13.Add(self.m_StaticText1, 0, wx.ALIGN_LEFT, 5)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(self.__lbl_w, self.__lbl_h), wx.TAB_TRAVERSAL)

        self.m_panel4.SetBackgroundColour(wx.Colour(254, 254, 254))

        bSizer13.Add(self.m_panel4, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer9.Add(bSizer13, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        bSizer9.Add(bSizer14, 0, wx.EXPAND, 5)

        bSizer8.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_button_print = wx.Button(self.m_panel3, wx.ID_ANY, u"Print Label", wx.DefaultPosition, wx.DefaultSize, 0)

        bSizer11.Add(self.m_button_print, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel3.SetSizer(bSizer11)

        self.m_panel3.Layout()

        bSizer11.Fit(self.m_panel3)

        bSizer10.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        bSizer8.Add(bSizer10, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer8)

        self.Layout()

        wx.CallLater(100, self.__create_labels)

        self.Centre(wx.BOTH)
        self.Show()

        # Connect Events
        self.m_button_print.Bind(wx.EVT_BUTTON, self.__on_print)


    def __create_labels(self):
        global dc
        dc = wx.ClientDC(self.m_panel4)
        dc.SetTextForeground((0, 0, 0))
        dc.SetPen(wx.Pen(wx.BLACK, 2))
        dc.DrawRectangle(10, 10, self.__lbl_w - 20, self.__lbl_h - 20)
        self.__add_lines()
        # required to close the program in clean manner. without it the program crashes when its main window is closed or destroyed
        dc.Destroy()


    def __add_lines(self):
        for i in self.__line.keys():
            dc.SetFont(wx.Font(self.__line[i][3], wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, self.__line[i][4], False))
            dc.DrawText(self.__line[i][0], self.__line[i][1], self.__line[i][2])


    def __on_print(self, event):
        event.Skip()
        #take a screenshot of the label area
        pos_x, pos_y = self.m_panel4.GetScreenPosition()
        w, h = self.m_panel4.GetSize()
        print("Label location : ", self.m_panel4.GetScreenPosition(), "    |    Label Size : ", self.m_panel4.GetSize())
        box = pos_x, pos_y, w, h
        wx.Yield()
        im = pyscreeze.screenshot(region=(box))
        im.save('screenshot.png')
        im.close()

        #send this captured screenshot to default printer on MacOS
        lpr = subprocess.Popen(['/usr/bin/lpr', u'screenshot.png'])  # prints picture
        lpr.communicate()  # required
        self.Destroy()


    def __del__(self):
        pass




