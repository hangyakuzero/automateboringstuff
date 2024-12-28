# what is the enumerate function in python?
# it is used to enumerate (two iterables) over a collection
li = ["apple", "strawberry", "madmax", "batman", "king", "warrior"]
di = {"john": 24, "jack": 30, "daniels": 45, "jhonnie": 50, "walker": 30}
for index, value in enumerate(
    li, start=1
):  # will start from one, but it still will count from the beginning of the list
    print(index, value)

print("\n")
for index, value in enumerate(li):
    print(index, value)
for test, (name, age) in enumerate(di.items()):
    print(f"index:{test}, name:{name}, age:{age}")
print("\n")
for name, age in di.items():
    print(f"name:{name}, age:{age}")
