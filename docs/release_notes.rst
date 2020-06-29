#############
Release Notes
#############

*****************************************************************
[0.1.1] Fix analyzer class internal attribute logic. (2020-06-29)
*****************************************************************

Previously, analyzer classes attached internal-use attributes to the class
itself. Now, these attributes are instance attributes as expected.


******************************************
[0.1.0] Initial beta release. (2020-06-28)
******************************************

Release initial beta version of `pcap-analysis` package with analyzers for the
following protocols:

* ARP
* BOOTP
* DHCP
* ICMP (Pings Only)
