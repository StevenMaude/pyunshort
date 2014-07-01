# pyunshort_me

Python module to access the [expandurl API](http://expandurl.me) for
unshortening of URLs. `unshort()` takes a URL as a string and returns
the unshortened form as a string.

## Usage

### Single URL
If you want to unshorten a single URL:

`unshort.py https://some.shortened.url`

### Multiple URLs
If you want to unshorten several URLs, put them in a CSV in a`url`
column, one per row, and run as:

`unshort.py input_file.csv`

The CSV needs to have a header with a column called `url`. For example:

```
blah,url
something,http://some.long.url
another thing,http://another.long.url
```

Copyright 2013-2014 ScraperWiki and licenced under the BSD licence
(see LICENCE).
