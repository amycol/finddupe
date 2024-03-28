import subprocess

filenames = []

proc = subprocess.run("find .", capture_output=True, text=True, shell=True)
files = proc.stdout.split("\n")
for i in files:
    tmparr = i.split("/")
    filename = tmparr[-1]
    if filename != "" or filename != " ":
        if filename in filenames:
            print(i)
        else:
            filenames.append(filename)