def supprimeDoublon(liste)
  initList = []
  for el in liste:
    if el not in initList:
      initList.append(el)
  return initList