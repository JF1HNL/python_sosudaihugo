# coding: UTF-8
import sympy
import random

def primarity_test(text):
  if not text.isdecimal():
    return "数字ではありません"
  q = int(text)
  if sympy.isprime(q) is True:
    response_string = str(q) + "は素数"
  elif q == 57:
    response_string = "グロタンカット！"
  elif q == 1729:
    response_string = "革命！"
  else:
    response_string = str(q) + "=" + str(sympy.factorint(q))
  return response_string