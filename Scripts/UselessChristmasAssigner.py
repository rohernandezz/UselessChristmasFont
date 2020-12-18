names = ["Ro", "Zrinka", "Caro Giovagnoli", "Laura García", "Sandra Morales", "Andrea Buendía", "Alejandra Hernández", "Zaira", "Constanza", "Manuel López", "Federico", "Adriana", "Monica", "Tina", "Yorch", "José Luis Coyolt", "Sandra García", "Karla Pasten", "Juan Villanueva", "Ana Michel", "Ximena", "Tamara", "Pulpo", "Victor Manuel"]
names.sort()
glyphs = "ABDEFGHIJKLMNOPQRSTUVWXYZ.,:¿?!¡&®"


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