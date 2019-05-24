import datetime

format = "%Y-%m-%d %H:%M:%S %Z%z"

timestamp = datetime.datetime.now()

string =str(timestamp.astimezone())
obj = datetime.datetime.utcnow()
obj1 = datetime.datetime.fromisoformat(string)

print(string)
print(obj)
print(type(obj1))


