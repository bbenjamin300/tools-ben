# tester.py

import os
sol = 653
print 'sol: ', sol
dirTest = '/Users/bbenjami/sol/%04d' % sol

try :
    print "  INFO: Creating: ", dirTest
    os.makedirs(dirTest)
except OSError as e:
    print e