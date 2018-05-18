# UNSW CSE Material Download Script :frog:
![Travis](https://img.shields.io/badge/build-passing-blue.svg)
![Language](https://img.shields.io/badge/language-Python%203.6-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
----
#### Warning this script just can grab the course on WebCMS3

## How to use :gun:

1. Download the project or use **git clone**
```
git clone git@github.com:lmcmz/UNSW-CSE-material-download.git
```

2. Go to the folder and install requirement packages
```
pip3 install -r requirements.txt
```

3. Run **webcms3.py** with arguments 
```
python3  webcms3.py -c [courses] -a [zid] -p [zPassword]
```

## Sample :pizza:

```
python3  webcms3.py -c COMP9417 -a z51025XX -p XXXXXXXXX
```

```
python3  webcms3.py -c COMP9417 COMP9321 COMP9517 -a z51025XX -p XXXXXXXXX
```

## License :icecream:
This code is distributed under the terms and conditions of the MIT license.

```
Copyright (C) 2018 lmcmz.me

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```