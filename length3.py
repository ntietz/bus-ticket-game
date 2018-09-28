import solve

LENGTH = 6
all_puzzles = list(solve.all_puzzles(LENGTH))
solvable_puzzles = list(solve.solvable_puzzles(LENGTH, target=100))
total_possible = len(all_puzzles)

#for puzzle in all_puzzles:
#    if puzzle not in solvable_puzzles:
#        print(puzzle)

print(f'Found {len(solvable_puzzles)} puzzles which are solvable (of {total_possible}).')

