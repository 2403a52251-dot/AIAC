# Improved version using best practice (with open() block)

with open("data1.txt", "w", encoding="utf-8") as f1, open("data2.txt", "w", encoding="utf-8") as f2:
    f1.write("First file content\n")
    f2.write("Second file content\n")

print("Files written successfully")