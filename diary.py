filename = "diary.txt"

file = open(filename, "x")
file.close()

file = open(filename, "w")
file.write("My Diary\n")
file.write("May 1, 2026\n")
file.write("Today I made my first diary file. I'm happy.\n")
file.close()

print("Diary created successfully!")