import json

if __name__ == "__main__":
  print(json.dumps([json.dumps({"first": 1, "second": 2}, separators=(",",":")), json.dumps({"first": 3, "second": 4}, separators=(",",":"))], separators=(",", ":")))
