import json

if __name__ == "__main__":
  print(json.dumps([json.dumsp({"first": 1, "second": 2}, seperators=(",",":")), json.dumps({"first": 3, "second": 4}, seperators=(",",":"))], separators=(",", ":")))
