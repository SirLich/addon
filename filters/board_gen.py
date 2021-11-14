import json
import sys

PATTERN_LOCATION='data/pattern.txt'

def create_start_function(size):
	function = open('BP/functions/start.mcfunction', 'w')

	for i in range(size):
		for j in range(size):
			function.write(f'summon sirlich:block {i} 95 {j} dead block\n')

	function.close()

def main():
	# Handle settings
	settings = json.loads(sys.argv[1])
	size = settings.get('size', 1)

	create_start_function(size)

main()