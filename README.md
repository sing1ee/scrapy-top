scrapy-top
==========

simple tools like linux top command to view scrapy status

###Requests
1. telnetlib default in python distribution
2. prettytable https://code.google.com/p/prettytable/

###Install

```python
python setup.py install
```

maybe you need **sudo**

###Run
For now, you can scrapy-top -i 2 -h localhost -p 6023

1. -i: interval seconds, defaut 2 secs
2. -h: host, default localhost
3. -p: port scrapy default telnet port 6023

###Output
| Key                                  | Value                        |
| ----------------------------------- | --------------------------- |
| log_count/DEBUG                      | 27                           |
| request_depth_max                    | 4                            |
| start_time                           | 2014-04-01 02:12:42.619696   |
| log_count/INFO                       | 6                            |
| downloader/request_method_count/GET  | 28                           |
| scheduler/dequeued/redis             | 28                           |
| downloader/request_bytes             | 12160                        |
