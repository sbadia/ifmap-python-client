#
# Copyright 2011, Infoblox, All Rights Reserved
#
# Open Source, see LICENSE

# Module with ID factories for creating IF-MAP Identifiers.
# Identifiers are used, for example, when publishing to an IF-MAP server, to represent an IP address.
# The XML for such the IP address identifier would be generated by ifmap.id.IPAddress
# example:
#  >>> print ifmap.id.IPAdress('10.0.0.1')

from util import attr

class ifmapIDFactory:
    pass


class IPAddress(ifmapIDFactory):
	"""
	XML Factory for an IP Address IF-MAP Identifier
	"""
	def __init__(self, ip_address, type=None, administrative_domain=None):
		self.__ip_address = ip_address
		self.__type = type
		self.__administrative_domain = administrative_domain

	def administrative_domain(self):
		return self.__administrative_domain

	def ip_address(self):
		return self.__ip_address

	def type(self):
		return self.__type

	def __str__(self):
		_attr = attr({'value':self.__ip_address,'type':self.__type,'administrative-domain':self.__administrative_domain})
		return '<ip-address %s' % _attr + '/>'

class MACAddress(ifmapIDFactory):
	"""
	XML Factory for a MAC Address IF-MAP Identifier
	"""

	def __init__(self, mac_address, administrative_domain=None):
		self.__mac_address = mac_address
		self.__administrative_domain = administrative_domain
		return None;

	def administrative_domain(self):
		return self.__administrative_domain

	def mac_address(self):
		return self.__mac_address

	def __str__(self):
	    _attr = attr({'value':self.__mac_address,'administrative-domain':self.__administrative_domain})
	    return '<mac-address %s' % _attr + '/>'


class Device(ifmapIDFactory):
	"""
	XML Factory for a Device IF-MAP Identifier
	"""

	def __init__(self, name, aik_name=None):
		self.__name = name
		self.__aik_name = aik_name
		return None;

	def aik_name(self):
		return self.__aik_name

	def name(self):
		return self.__name

	def __str__(self):
		self.__XML = "<device>"
		self.__XML += '<name>'+self.__name+'</name>'
		# aik_name is optional
		if self.__aik_name:
			self.__XML += '<aik-name>'+self.__aik_name+'<aik-name>'
		self.__XML += "</device>"
		return self.__XML

class AccessRequest(ifmapIDFactory):
	"""
	XML Factory for an Access Request IF-MAP Identifier
	"""

	def __init__(self, name, administrative_domain=None):
		self.__name = name
		self.__administrative_domain = administrative_domain
		return None;

	def administrative_domain(self):
		return self.__administrative_domain

	def name(self):
		return self.__name

	def __str__(self):
		self.__XML = "<access-request"
		self.__XML += ' name="'+self.__name+'"'
		# administrative_domain is optional
		if self.__administrative_domain:
			self.__XML += ' administrative-domain="'+self.__administrative_domain+'"'
		self.__XML += " />"
		return self.__XML

class Identity(ifmapIDFactory):
	"""
	XML Factory for an IF-MAP Identifier
	"""

	def __init__(self, name, type=None, other_type=None, administrative_domain=None):
		self.__name = name # required
		self.__type = type # "aik_name"|"distinguished_name"|"dns_name"|"email_address"|"kerberos_principal"|"username"|"sip_uri"|"tel_uri"|"hip_hit"|"other"
		self.__other_type = other_type # vendor-specific type
		self.__administrative_domain = administrative_domain
		return None;

	def administrative_domain(self):
		return self.__administrative_domain

	def name(self):
		return self.__name

	def type(self):
		return self.__type

	def other_type(self):
		return self.__other_type

	def __str__(self):
		self.__XML = "<identity"
		self.__XML += ' name="'+self.__name+'"'
		# type and administrative_domain are optional
		if self.__type:
			self.__XML +=' type="'+self.__type+'"'
		if self.__other_type:
			self.__XML +=' other-type="'+self.__other_type+'"'
		if self.__administrative_domain:
			self.__XML += ' administrative-domain="'+self.__administrative_domain+'"'
		self.__XML += " />"
		return self.__XML


class CustomIdentity(ifmapIDFactory):
	"""
	XML Factory for an Custom IF-MAP Identifier with namespace prefix or URL
	"""

	def __init__(self, name, ns_prefix="", namespace="", attributes=None):
		self.__name = name # required
		self.__ns_prefix = ns_prefix # see ifmap.namespaces
		self.__namespace = namespace # a namespace IRI/URI
		self.__attributes = attributes # additional attributes in a dictionary (eg. {key1: value1, key2: value2})
		return None;

	def attributes(self):
		return self.__attributes

	def name(self):
		return self.__name

	def ns_prefix(self):
		return self.__ns_prefix

	def namespace(self):
		return self.__namespace

	def __str__(self):
		self.__XML = "<custom-identifier>"


		if self.__ns_prefix:
			self.__ns_prefix = self.__ns_prefix +':'

		self.__XML += '<'+self.__ns_prefix+self.__name

		if self.__namespace:
			self.__namespace=' xlmns='+self.__ns_prefix+self.__namespace

		self.__XML += self.__namespace

		if self.__attributes and (type(self.__attributes) == type({})) and self.__attributes.items():
			for key, attribute in self.__attributes.items():
				self.__XML += ' '+key+'="'+attribute+'"'
		self.__XML += " /></custom-identifier>"
		return self.__XML
