import sys

textmap = """
..........................................
.......XXXXXXXXXX..........XXXX...........
.......X........X..........X..XXXXX.......
.......X........X.......XXXX......XXXXX...
..XXXXXX........X.......X.............X...
..X.............X......XX.............X...
..X.............X.....XX...........XXXX...
..X........XXXXXX.....X............X......
..X........X..........XXX........XXX......
..XXXX..XXXX............X.......XX........
.....XXXX...............X......XX.........
........................XXX....X..........
..........................XXXXXX..........
"""


def getWorldFromTextMap(textmap):
	worldWidth = len(textmap.strip().split("\n")[0])
	worldHeight = len(textmap.strip().split("\n"))
	textmap = textmap.strip().split("\n")
	world = []
	for i in range(worldWidth):
		world.append([''] * worldHeight)
	for x in range(worldWidth):
		for y in range(worldHeight):
			world[x][y] = textmap[y][x]
	return world


def printWorld(world):
	worldWidth = len(world)
	worldHeight = len(world[0])
	for y in range(worldHeight):
		for x in range(worldWidth):
			sys.stdout.write(world[x][y])
		sys.stdout.write("\n")


def floodFill(world, x, y, oldChar, newChar):
	# The recursive algorithm. Starting at x and y, changes any adjacent
	# characters that match oldChar to newChar.
	worldWidth = len(world)
	worldHeight = len(world[0])
	if oldChar == None:
		oldChar = world[x][y]
	if world[x][y] != oldChar:
		# Base case. If the current x, y character is not the oldChar,
		# then do nothing.
		return
	# Change the character at world[x][y] to newChar
	world[x][y] = newChar
	# Recursive calls. Make a recursive call as long as we are not on the
	# boundary (which would cause an Index Error.)
	if x > 0:  # left
		floodFill(world, x-1, y, oldChar, newChar)

	if y > 0:  # up
		floodFill(world, x, y-1, oldChar, newChar)

	if x < worldWidth-1:  # right
		floodFill(world, x+1, y, oldChar, newChar)

	if y < worldHeight-1:  # down
		floodFill(world, x, y+1, oldChar, newChar)


def main():
	world = getWorldFromTextMap(textmap)
	printWorld(world)
	print()

	floodFill(world, 5, 8, None, 'I')
	printWorld(world)
	print()

	floodFill(world, 25, 8, None, 'I')
	printWorld(world)
	print()

	floodFill(world, 0, 0, None, ' ')
	printWorld(world)
	print()

if __name__ == '__main__':
	main()