#############
API Reference
#############

.. contents::
   :local:

.. automodule:: pcap_analysis

*******
Classes
*******

PacketAnalyzer
==============

.. autoclass:: pcap_analysis.PacketAnalyzer

    .. py:attribute:: arp

        Address resolution protocol (ARP) analyzer accessor.

    .. py:attribute:: bootp

        Bootstrap protocol (BOOTP) analyzer accessor.

    .. py:attribute:: dhcp

        Dynamic host configuration protocol (DHCP) analyzer accessor.

    .. py:attribute:: icmp

        Internet control message protocol (ICMP) analyzer accessor.

*********
Analyzers
*********

Access analyzer class instances through the ``PacketAnalyzer`` class. They
should not be instantiated directly and used standalone!

ARP
===

.. autoclass:: pcap_analysis._analyzers.arp.Arp
   :members:

BOOTP
=====

.. autoclass:: pcap_analysis._analyzers.bootp.Bootp
   :members:

DHCP
====

.. autoclass:: pcap_analysis._analyzers.dhcp.Dhcp
   :members:

ICMP
====

.. autoclass:: pcap_analysis._analyzers.icmp.Icmp
   :members:
