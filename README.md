# trendr
Chart generator built using the Python standard library.

Usage
---
```
SVG chart generator

optional arguments:
  -h, --help       show this help message and exit
  --input INPUT    input file containing events
  --output OUTPUT  SVG output file
  --start START    Period start (Unix Timestamp)
  --end END        Period end (Unix Timestamp)
```


**Example**
```
$ python -m trendr --input examples/testdata_large.txt --output test.svg --start 1428997804 --end 1429602499
```

Compatibility
---
Works with python 2 and 3. Use with **pypy** for performance. 


Output
---
Charts are generated with on-hover highlight and tooltip. Example:
![Example Chart](https://raw.githubusercontent.com/rbw/trendr/master/examples/output.svg?sanitize=true)



Author
---
Robert Wikman \<rbw@vault13.org\>
