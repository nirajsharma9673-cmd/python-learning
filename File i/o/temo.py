import tempfile 
for_temporary= tempfile.TemporaryFile()
for_temporary.write(b"hii niraj after changing the file of temp file ")
for_temporary.seek(0)
print(for_temporary.read())