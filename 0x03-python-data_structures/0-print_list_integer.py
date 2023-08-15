#!/usr/bin/python

def print_list_integer(my_list=[]):
 integer_list = [item for item in my_list if isinstance(item,int)]
 for integer in integer_list:
  print("{:d}".format(integer))
