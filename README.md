
# GMC geiger counter data acquisition webservice

# Based on excellent "pygeiger" work

This project is a website compatible with GQ GMC geiger counteris which capable to send data via network.
It stores the measurement pushed by the counter in plain CSV file. Optionally it forwards each measurement to the http://gmcmap.com website.

The GQ counters can produce measurements every minute. The following data are produced:

* CPM : Counts per minute of the geiger counter
* ACPM: Averaged CPM
* usV: value in uSv/h (beware that the device is not energy compensated)

See the [documentation from gq](http://www.gqelectronicsllc.com/GMC-320PlusV5UserGuide.pdf) and [Wikipedia](https://en.wikipedia.org/wiki/Geiger_counter)

## Configuring the device

For you GQ GMC device to work with an instance of this webservice you will need to modify the  **Website** and **URL** as described in the [documentation - Read it !](http://www.gqelectronicsllc.com/GMC-320PlusV5UserGuide.pdf).

In my case I have set:
```
Website: 192.168.8.8
URL: upload
```

This will make the device produce HTTP GET requests like this *http://192.168.8.8/upload?AID=00000&GID=1111111&CPM=18&ACPM=18.2&uSV=0.080*

(!) NOTE: Currently GQ GMC counters does not support the ports other then 80 for HTTP POST requests

## Credits

Many years for Frank Guibert !


## Overview

I tried to utilise the docker container to add flexibility. 
Docker will mount local folder to keep data 

Here is few simple steps to run this service.

# docker-compose

      $ docker-compose build
      $ docker-compose up

# docker
      $ docker build -t gmc .
      $ docker run -d --name gcmcontainer -p 80:80 --mount type=bind,source="/opt/app_data,target=/code/app/app_data,bind-propagation=rshared gmc

There also PHP code which could be in use on the existed WEB server to gather data

You can upload fake data to your local instance using this request:

```
$ curl "http://192.168.8.8/upload?AID=00000&GID=1111111&CPM=18&ACPM=18.2&uSV=0.080"
or (for php)
$ curl "http://your.web.site/upload.php?AID=00000&GID=1111111&CPM=18&ACPM=18.2&uSV=0.080"
```

## LICENSE: The MIT License (MIT)

Copyright © 2023 Vlad Patoka

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
