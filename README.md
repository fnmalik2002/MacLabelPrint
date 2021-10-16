# MacLabelPrint
 Create a formatted label and print it using MacOS and Python 3

 Call this label creator from inside your python code.
 
 You can put the code to create this label, inside a button click method in you python gui app.
 
## Import and contstruct label object to print

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
 
In both methods one can contruct default label constructor
 
