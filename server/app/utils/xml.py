def search_xml_tree(root, term):
  result = ""
  for node in root.iter(term):
    result = node.text
    break
  return result