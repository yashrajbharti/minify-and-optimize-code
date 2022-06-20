import fileinput
import sys

sys.stdout = open('/Users/yashraj/Desktop/optimize/empty.txt', 'w')
with open('/Users/yashraj/Desktop/optimize/Affected_Areas.txt') as f:
    contents = f.read()
new = "".join(contents.split())

sys.stdout.write(new)

f.close()
sys.stdout.close()