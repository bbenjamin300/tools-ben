#!usr/bin/python

# sec_converter.py
# input seconds, get hh:mm:ss.sss

sec_in = float(raw_input("\n    Time, in seconds: "))


hh = sec_in / 3600
mm = (hh-int(hh)) * 60
ss = (mm-int(mm)) * 60

print "    hh:mm:ss.sss", "-->", "{0:02d}".format(int(hh))+":{0:02d}".format(int(mm))+":{0:.3f}".format(ss)+"\n"