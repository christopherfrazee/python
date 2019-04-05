
import argparse
import boto
import boto.route53
import re
import sys
from optparse import OptionParser
desc="AWS ADD / CHANGE / DELETE CNAME TOOL"
pVersion = "Version 1.0 Internal"

parser = OptionParser(description=desc, version=pVersion)
parser.add_option('-C', "--create",
          action="store_true", dest="Create", default=False,
          help="Create a CNAME")
parser.add_option('-D', "--delete",
          action="store_true", dest="Delete", default=False,
          help="Delete a CNAME")
parser.add_option("-n", dest="hostname", help="the hostname you want to use in cname")
parser.add_option("-d", dest="domainName", help="the domain name to use in cname")
parser.add_option("-p", dest="publicName", help="the public name of the ec2 instance name")
parser.add_option("-z', dest="hostedZoneId", help="the AWS zone ID assigned to the domain")

(options, args) = parser.parse_args()
cnameRecord = options.hostname
domainName = options.domainName
ec2_public_name = options.publicName 
fqdn = cnameRecord + "." + domainName + "."


lead_dot_domain = re.compile('^\.[a-z]+\.janrain\.com')
no_lead_dot_domain = re.compile('^[a-z]+\.janrain\.com')
if no_lead_dot_domain.match(domainName):
   t = "janrain.com huh. . ."
   print t
elif lead_dot_domain.match(domainName):
   t = "removing leading dot in zone name"
   print t
   domainName = domainName.lstrip('.')
   s = "domainName huh. . ."
   print s
else:
   t = "sorry invalid domain. . ."
   print t
   sys.exit(1)
conn = boto.connect_route53(host='route53.amazonaws.com', debug=0)
changes = boto.route53.record.ResourceRecordSets(conn, hostedZoneId)

if options.Create: 
   change = changes.add_change("UPSERT", fqdn, "CNAME")
   print 'Ok, Creating: {} IN CNAME {}'.format(fqdn, ec2_public_name)
elif options.Delete:
   change = changes.add_change("DELETE", fqdn, "CNAME" ) 
   print 'Ok, Deleting: {} IN CNAME {}'.format(fqdn, ec2_public_name)
else:
   t = "Sorry you need to specify -C (create) or -D (delete)"
   print t
   sys.exit(1)
change.add_value(ec2_public_name)
result = changes.commit()
t = 'Done.'
print t



