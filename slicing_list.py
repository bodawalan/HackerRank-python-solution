


from sys import argv
from os.path import exists

# read the WYSS section for how to run this
script,fromfile ,to_file = argv

print(f"we copy file {fromfile} to {to_file}")

indata=open(fromfile).read()


print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
