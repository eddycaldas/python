# extend method adds any amount at the end of a list, it will mutate it.

color = ['black', 'red']
print(color)
print()

color.extend(['blue', 'yellow', 'white'])
print(color)
print()

extra_colors = ['pink', 'green', 'purple']
color.extend(extra_colors)
print(color)

print()
# this methos ( + ) will not mutate them:
steak = ['t-bone', 'ribeye']
more_steak = ['ney york strip', 'tenderloid']
print(steak + more_steak)
print()

print(steak)
print(more_steak)