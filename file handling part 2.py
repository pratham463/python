# Open the file in read mode

file_read = open('codingal.txt', 'r')

print("File in read mode:")

print(file_read.read())

file_read.close()

# Open the file in write mode

file_write = open('codingal.txt', 'w')

# Write to the file

file_content = """Hi, my name is penguine. I am in grade 1

My hobby is chess and gaming."""

file_write.write(file_content)

file_write.close()

file_append = open('codingal.txt', 'a')
file_append.write = ("""file in append mode""")
file_append = """Hi, my name is penguine. I am in grade 1

My hobby is chess and gaming."""
file_write.close()