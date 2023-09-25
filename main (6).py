def linearSearchProduct(productList,targetProduct):
  indices=[]
  for index,product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices
product=["shoes","boot","loafer","shoes","sandel","shoes"]
target="shoes"
result=linearSearchProduct(product,target)
print(result)

      
      