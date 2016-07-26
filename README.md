The piece of code is kept under a GNU license for anyone else to use as well. The api being used can be found here: https://holidayapi.com

Steps to run the code

1. Go to the repository holding the file dategetter.py
2. Initialize python 2.7 (untested on Python 3, but should work)
3. import * from holidaygetter
4. Initialize an object of class Hollidaygetter()
5. run method main on the initialized object with country code and list of years required

eg: after running python-

from holidaygetter import *
h =  Holidaygetter()
h.main('GB',['2015','2016'])


Country Codes:
GB : Great Britain
US : United states
CA : Canada
IN : India

More country codes can be found on the api documentation at https://holidayapi.com 