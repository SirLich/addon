import json
import sys

LIFE_CELL_LOCATION ='RP/particles/life_cell.json'
LIFE_TIMER_LOCATION ='RP/particles/life_timer.json'
PATTERN_LOCATION='data/pattern.txt'

def create_cell_color(cell, size):
	color = ""
	for x in range (0, size):
		for z in range(0, size):
			color += "v.cell.x == {x} && v.cell.z == {z} ? {{return t.o{x}_{z};}};".format(x=x,z=z)

	color += "return 0;"
	cell['particle_effect']['components']['minecraft:particle_appearance_tinting']['color'][0] = color

def create_timer_preinit(particle, size):

	pattern = open(PATTERN_LOCATION, 'r')

	data = ""
	for x in range (0, size):
		line = pattern.readline()

		for z in range(0, size):
			try:
				alive = line[z].strip()
			except:
				alive = '0'

			if alive == '':
				alive = '0'

			data += f"t.p{x}_{z} = {alive};t.o{x}_{z} = {alive};"

	particle['particle_effect']['components']['minecraft:emitter_initialization']['creation_expression'] = data

def create_timer_expression(particle, size):
	data = ""
	open = '{'
	close = '}'

	for x in range (0, size):
		for z in range(0, size):
			data += \
f"""
t.o{x}_{z} = t.p{x}_{z};
t.p{x}_{z} = 0;
""".replace("\t", "").replace("\n", "")


	for x in range (0, size):
		for z in range(0, size):
			data += \
f"""
t.p{x}_{z} = t.p{x}_{z} + t.o{(x-1) % size}_{(z-1)% size};
t.p{x}_{z} = t.p{x}_{z} + t.o{(x-1) % size}_{(z)% size};
t.p{x}_{z} = t.p{x}_{z} + t.o{(x-1) % size}_{(z+1)% size};
t.p{x}_{z} = t.p{x}_{z} + t.o{(x) % size}_{(z-1)% size};
t.p{x}_{z} = t.p{x}_{z} + t.o{(x) % size}_{(z+1)% size};
t.p{x}_{z} = t.p{x}_{z} + t.o{(x+1) % size}_{(z-1)% size};
t.p{x}_{z} = t.p{x}_{z} + t.o{(x+1) % size}_{(z)% size};
t.p{x}_{z} = t.p{x}_{z} + t.o{(x+1) % size}_{(z+1) % size};
""".replace("\t", "").replace("\n", "")


	for x in range (0, size):
		for z in range(0, size):
			data += \
f"""
t.o{x}_{z} == 1 ? {open}
	t.p{x}_{z} = (t.p{x}_{z} == 2 || t.p{x}_{z} == 3) ? 1 : 0;
{close} : {open}
	t.p{x}_{z} = (t.p{x}_{z} == 3) ? 1 : 0;
{close};
""".replace("\t", "").replace("\n", "")




	particle['particle_effect']['events']['gol']['expression'] = data

def main():
	# Handle settings
	settings = json.loads(sys.argv[1])
	size = settings.get('size', 1)


	# ========================== LIFE CELL ==========================
	# Load
	with open(LIFE_CELL_LOCATION, 'r') as file_:
		life_cell = json.loads(file_.read().replace("\t", "").replace("\n", ""), strict=False)

	# Logic generation
	create_cell_color(life_cell, size)

	# Save
	with open(LIFE_CELL_LOCATION, 'w') as file_:
		json.dump(life_cell, file_, indent=4)

	# ========================== LIFE TIMER ==========================
	# Load
	with open (LIFE_TIMER_LOCATION, 'r') as file_:
		life_timer = json.loads(file_.read().replace("\t", "").replace("\n", ""), strict=False)
	
	# Logic generation
	create_timer_preinit(life_timer, size)
	create_timer_expression(life_timer, size)

	# Save
	with open(LIFE_TIMER_LOCATION, 'w') as file_:
		json.dump(life_timer, file_, indent=4)


main()


