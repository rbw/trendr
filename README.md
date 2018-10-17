# trendr
Pure-python SVG graph generator built using the Python standard library (no deps).

Usage
---
```
SVG trend graph generator

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
SVG files are generated with on-hover effects and a tooltip (open in separate tab to test). 
![Example Graph](./examples/output.svg)



Author
---
Robert Wikman \<rbw@vault13.org\>
