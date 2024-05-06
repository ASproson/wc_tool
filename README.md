# Unix Style wc Tool

Implementation of the unix `wc` functionality using Python. `wc` in unix allows the user to pass or pipe a file to see that file's word, line, character, and byte count.

## Installation

Please clone the repo below:

`git clone https://github.com/ASproson/wc_tool.git`

When in the repo directory you can run the following commands on the test file:

> `python ccwc.py test.txt`

> `python ccwc.py test.txt -h`

> `python ccwc.py test.txt --help`

> `python ccwc.py test.txt -w`

> `python ccwc.py test.txt --words`

> `python ccwc.py test.txt -l`

> `python ccwc.py test.txt --lines`

> `python ccwc.py test.txt -m`

> `python ccwc.py test.txt --characters`

Alternatively you can pipe in a specific file to the script itself and make use of the same commands above:

> `cat test.txt | python ccwc.py`
