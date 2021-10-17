# MacLabelPrint

---
Create a formatted label and print it on macOS and Python 3. You can control label size, text size, text location on label and text weight using this module.
The newly constructed modules will be displayed on your screen alongside a print button which will print the label to your Mac's default printer without opening   printer options dialogue box.

 Call this label creator from inside your python code.
 
 You can put the label constructor code inside a button click method in your python gui app.
 
## Import and construct label object to print

### Method 1
```

from MacLabelPrint import MyLabel as pl

pl(None, lable_data_as_dictionary, label_width, label_height)

or

pl(None, lable_data_as_dictionary)
```
### Method 2
```

import MacLabelPrint as pl

pl.MyLabel(None, lable_data_as_dictionary, label_width, label_height)

or

pl.MyLabel(None, lable_data_as_dictionary)

```
 
## What should be in label_data dictionary?

Each key:value pair represents one line of text on label

key can be any string but value has to be a list with items in this order "label text string", string distance from left, string distance from top, font size, font weight

font weight can be just the number 400 for normal text or wx.FONTWEIGHT_NORMAL without quotes around it

font weight can be just the number 700 for bold text or wx.FONTWEIGHT_BOLD without quotes around it
###
```

label_data = {

    "ln1" : ["line 1 bold text here", 20, 20, 16, 700]
    "ln2" : ["line 2 bold here", 20, 40, 16, wx.FONTWEIGHT_BOLD]
    "ln3" : ["line 3 normal text here", 20, 60, 16, 400]
    "ln4" : ["line 4 normal here", 20, 80, 16, wx.FONTWEIGHT_NORMAL]

}

```
 ## IMPORTANT
 
 Make sure if you set label sizes to be width=400 and height=600 then in your printer settings page (using Safari on localhost:631) change defaults to paper size 4.00 x 6.00
 
 ## Sample Label
 ![image of sample label](https://github.com/fnmalik2002/MacLabelPrint/blob/main/images/sample.png)
