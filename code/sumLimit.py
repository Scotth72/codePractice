def solutions(items, limit):
  h = []
  g = {}
  for index, item in enumerate(items):
    g[item] = [index, limit-item]

  def first_pair(g):
    for key in g:
      # check of the second value exist in the hash table for the example the second value is 15 because 15 + 6 = limit
      if g[key][1] in g and key != g[key][1]:
        # since 15 exist within the key of g
        # we need to check the indices of 15
        # if the indeces of 15 > the indeces of 6 then we put the indicies of 15 first
        if g[g[key][1]][0] > g[key][0]:  # If it does make sure to set the higher index first
          h.append([g[g[key][1]][0], g[key][0]])
        else:
          h.append([g[key][0], g[g[key][1]][0]])
    return h
  # now we potentially have a list of arrays that contains two indicies that point to values that sum up to the limit
  c = first_pair(g)
  if len(c) == 0:  # check of list is empty
    return []
  v = c[0]
  for item in c:
    if item[0] < v[0]:
      v = item
  return v
