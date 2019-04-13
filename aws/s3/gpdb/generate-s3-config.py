#!/usr/bin/env python

#~ Generates an s3 configuration file to be distributed
#~ across all Greenplum segment servers

#~ Enables S3 access via GPDB readable/writable external tables

import getpass

file = '/home/gpadmin/s3.conf'

accesskey = getpass.getpass('Enter accesskey: ')
secretkey = getpass.getpass('Enter secretkey: ')

with open(file, 'w') as f:
    output = '[default]\n'
    output += 'accessid="{0}"\n'.format(accesskey)
    output += 'secret="{0}"\n'.format(secretkey)
    output += 'autocompress=false\n'
    output += 'threadnum = 8\n'
    output += 'chunksize = 67108864\n'
    output += 'low_speed_limit = 10240\n'
    output += 'low_speed_time = 60\n'

    f.write(output)
