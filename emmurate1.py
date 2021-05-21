# enumerate  function
food=["chocolate","noodles","pasta","drinks"]
i=1
# if you dont want noodles & drinks
#for item in food:
#   if i%2 == 0:
#      print(f"please buy this one {item}")
#     i+=1

# above program in short by using enumerate function
for index,item in enumerate(food):
    if index%2==0:
        print(f"buy this {item}")