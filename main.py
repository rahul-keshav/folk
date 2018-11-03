my_file=open("message.txt","r+")
message=my_file.read()
print(message)
my_file.close()
print(message)

msg=message+str(8765567)
print(msg)