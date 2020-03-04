the_simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]

for i in the_simpsons[::-1]:
    print(f"{i} has {len(i)} characters")

print("-------------")

for i in reversed(the_simpsons):
        print(f"{i} has {len(i)} characters")
