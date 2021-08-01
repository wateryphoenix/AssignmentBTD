tall = int(input("อยากให้ต้นไม้สูงแค่ไหน : "))
blank = tall
for Hight in range(1):
    for tree in range(tall):
        blank -= 1
        tree += (1*(tree+1))
        print(" "*blank,"*"*tree)
