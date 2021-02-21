except FileNotFoundError:
name = self.inputbox1.get()
print(name)
with open("file.txt", "w") as f:
    f.write(name)
    f.close()