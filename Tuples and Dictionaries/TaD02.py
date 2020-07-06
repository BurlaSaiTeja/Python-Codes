"""
For a supermarket, create 2 dictionaries called “stock” and “prices”.  
stock={‘raddish’:5,’apple’:2,’tomato’:3}
prices={‘raddish’:50, ‘apple’:100, ‘tomato’:30}
Create these two dictionaries using a list in the form [k1,k2,k3,k4,v1,v2,v3,v4] passed to this function.  
Create(items_in_a_list), that creates a dictionary d={k1:v1,k2:v2,k3:v3, k4:v4} and returns a dictionary. 
-display(), that displays key along with its price and stock information. 
-compute_bill() that takes a list as an argument of all the items to be purchased, eg. [‘raddish’, ‘apple’]
   Check if stock is greater than 0 for each item
   Add the corresponding price of the item to a variable, ‘total’
   Subtract 1 from the stock dictionary
   Return total
-if_all_sold(item_name), takes the name of the item as an argument, returns “Yes” if item is sold out, i.e. stock is 0 or “No” 
-max_stock(), that displays the product that is in maximum stock. 
-max_price(), that displays the product with maximum price.
"""

stock={}
prices={}

def create(lst):
  l1 = lst[0:len(lst)//2]
  l2 = lst[len(lst)//2:]
  d = dict(zip(l1, l2))
  # code to convert list of form
  #[k1,k2,k3,k4,v1,v2,v3,v4]
  #to dictionary k1:v1, k2:v2, ...   
  return d

def compute_bill(lst):
    
  total = 0.0
  
  for i in lst:
    if stock[i]>0:
      total += prices[i]
      stock[i] -= 1
  # for each item in a list
  # if stock is>0
  # add the item's price to total
  # subtract 1 item from stock.

  return total

stock={}
prices={}

def create(lst):
  l1 = lst[0:len(lst)//2]
  l2 = lst[len(lst)//2:]
  d = dict(zip(l1, l2))
  # code to convert list of form
  #[k1,k2,k3,k4,v1,v2,v3,v4]
  #to dictionary k1:v1, k2:v2, ...   
  return d

def compute_bill(lst):
    
  total = 0.0
  
  for i in lst:
    if stock[i]>0:
      total += prices[i]
      stock[i] -= 1
  # for each item in a list
  # if stock is>0
  # add the item's price to total
  # subtract 1 item from stock.

  return total

def if_all_sold(item_name):
  if stock[item_name] == 0 or None:
    return True
  else:
    return False
    # check if item is sold out
    # return yes or no

def max_stock():
  return max(stock)
    #displays the product that is in maximum stock. 

def max_price():
  return max(prices)
    #displays the product with maximum price.

def display():
  for i in stock.keys():
    print(i, stock[i], prices[i])

#Create dictionary Stock
stock = create(['raddish','apple','tomato',5,2,10])
prices = create(['raddish','apple','tomato',50,100,30])

#call other functions 
print("All Products")
display()
print("Maximum Priced product:",max_price())
print("Maximum stocked product:",max_stock())
print("Bill for Raddish and Apple:", compute_bill(['raddish', 'apple']))
print("Are all the Tomatoes sold?", if_all_sold('tomato'))

"""
Output:
All Products
raddish 5 50
apple 2 100
tomato 10 30
Maximum Priced product: tomato
Maximum stocked product: tomato
Bill for Raddish and Apple: 150.0
Are all the Tomatoes sold? False
"""
