import json

if __name__ == "__main__":
  print(json.dumps([{"first": 1, "second": 2}, {"first": 3, "second": 4}], separators=(",", ":")))
