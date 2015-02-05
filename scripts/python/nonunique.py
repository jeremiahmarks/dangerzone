def nonunique(alist):
  for item in alist:
    if (alist.count(item)==1):
      alist.remove(item)
  return alist
