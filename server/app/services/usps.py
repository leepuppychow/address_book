import os
import requests
import urllib.parse
from xml.etree import ElementTree
from utils.xml import search_xml_tree

class UspsService():
  def __init__(self, street, city, state):
    self.street = street
    self.city = city
    self.state = state
    self.base_url = 'https://secure.shippingapis.com'

  def get_zipcode(self):
    path = "/ShippingAPI.dll?API=ZipCodeLookup"
    xml = """
    <ZipCodeLookupRequest USERID="%s">
      <Address>
      <Address1></Address1>
      <Address2>%s</Address2>
      <City>%s</City>
      <State>%s</State>
      </Address>
    </ZipCodeLookupRequest>
    """ % (os.environ['USPS_USER_ID'], self.street, self.city, self.state)
    url = self.base_url + path + "&XML=" + urllib.parse.quote(xml) 
    response = requests.get(url)
    root = ElementTree.fromstring(response.content)
    return search_xml_tree(root, "Zip5"), search_xml_tree(root, "Zip4")