import os


os.makedirs("/tmp/output")

with open("/tmp/output/file1.txt", "w") as file:
  file.write("file1")

with open("/tmp/output/file2.txt", "w") as file:
  file.write("file2")

with open("/tmp/output/file3.txt", "w") as file:
  file.write("file3")

with open("/tmp/output/file4.txt", "w") as file:
  file.write("file4")


