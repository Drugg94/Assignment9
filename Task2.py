# Revision 1 BEGIN/ 24Mar22
## Begin Derek Ruggirello here (24Mar22)

def print_range(start, end):
    if start == end:
        print(start)
        return
    elif start > end:
        print(start)
        start = start - 1
        print_range(start, end)
        return
    else:
        print(start)
        start = start + 1
        print_range(start, end)
        return

print_range(4,2)

# Revision 1 FINAL 24Mar22
## End Derek Ruggirello here
# HALF-LIFE/Ron Bass/John Richards Sr./After-Burner Elite #