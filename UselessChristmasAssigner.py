names = ["Ro", "Zrinka", "Tamara", "Gen", "Whoever"]
names.sort()
glyphs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.,:¿?!¡&®"


leftovers = glyphs
print("Useless Christmas Glyph Assignments:")
print("------------------------------------")
    
for g in names:
    glyph = choice(glyphs)
    glyphs = glyphs.replace(glyph,"")
    print(f"{g} --> {glyph}")
    leftovers = glyphs
    
print(" ")
print(f"Leftovers: {leftovers}")