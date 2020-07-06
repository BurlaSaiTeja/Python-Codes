"""
 Given the following dictionary: 
inventory={‘gold’:500, 
                  'pouch' : ['flint', 'twine', 'gemstone'], 
                 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'] } 
Write a function ‘change(inventory)’, that returns the dictionary inventory{} after the following changes: 
Add a key to inventory called 'pocket'. 
Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'. 
Sort the items in the list stored under the 'backpack' key. 
Remove('dagger') from the list of items stored under the 'backpack' key. 
Add 50 to the number stored under the 'gold' key. 
"""

import pprint

inventory={'gold':500,
            'pouch' : [
              'flint', 
              'twine', 
              'gemstone'
              ],
            'backpack' : [
              'xylophone',
              'dagger', 
              'bedroll',
              'bread loaf'
              ] 
          }

def change(a): 
  a['pocket'] = ['seashells', 'strange berry', 'lint']
  newlist = list(a['backpack'])
  newlist.remove('dagger')
  newlist.sort()
  a['backpack'] = newlist
  a['gold'] = 50 + int(a['gold'])
  return a

print("Before:")
pprint.pprint(inventory)
change(inventory)
print("\nAfter:")
pprint.pprint(inventory)

"""
Output:
Before:
{'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
 'gold': 500,
 'pouch': ['flint', 'twine', 'gemstone']}

After:
{'backpack': ['bedroll', 'bread loaf', 'xylophone'],
 'gold': 550,
 'pocket': ['seashells', 'strange berry', 'lint'],
 'pouch': ['flint', 'twine', 'gemstone']}
"""
