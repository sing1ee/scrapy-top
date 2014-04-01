import telnetlib
import datetime
from prettytable import PrettyTable
import os
import time
import sys
import getopt


def main():
    HOST = 'localhost'
    PORT = 6023
    INTERVAL = 2
    opts, args = getopt.getopt(sys.argv[1:], "i:h:p:")
    for op, value in opts:
        if op == "-i":
            INTERVAL = int(value)
        elif op == "-h":
            HOST = value
        elif op == "-p":
            i = os.system("clear")
    try:
        tn = telnetlib.Telnet()
        tn.open(HOST, PORT)
    except:
        print "Can't connect to %s:%d" % (HOST, PORT)
        sys.exit()
    while True:
        try:
            tn = telnetlib.Telnet()
            tn.open(HOST, PORT)
            tn.write('stats.get_stats()' + '\r\n')
            ret = tn.read_until('}').splitlines()[3]
            data = eval(ret)
            x = PrettyTable(['Key', 'Value'])
            for k, v in data.items():
                x.add_row([k, v])
            print x
            time.sleep(INTERVAL)
            i = os.system("clear")
        except:
            print "Can't connect to %s:%d" % (HOST, PORT)
            sys.exit()

if __name__ == "__main__":
    main()
