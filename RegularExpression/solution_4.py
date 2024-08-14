# Count all backslashes in a doc
import re
doc = "\n we have \ backslashes \\"

result = re.findall("[\\\]", doc)
print(result)