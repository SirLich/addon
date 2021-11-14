# Update score count for every cell to reflect number of live cells around it.
# execute @e[family=block] ~-1 ~ ~-1 execute @e[family=live,r=0.1] ~1 ~ ~1 scoreboard players add @s gol 1
# execute @e[family=block] ~-1 ~ ~ execute @e[family=live,r=0.1] ~1 ~ ~ scoreboard players add @s gol 1
# execute @e[family=block] ~-1 ~ ~1 execute @e[family=live,r=0.1] ~1 ~ ~-1 scoreboard players add @s gol 1

# execute @e[family=block] ~ ~ ~-1 execute @e[family=live,r=0.1] ~ ~ ~1 scoreboard players add @s gol 1
# execute @e[family=block] ~ ~ ~1 execute @e[family=live,r=0.1] ~ ~ ~-1 scoreboard players add @s gol 1

# execute @e[family=block] ~1 ~ ~-1 execute @e[family=live,r=0.1] ~-1 ~ ~1 scoreboard players add @s gol 1
# execute @e[family=block] ~1 ~ ~ execute @e[family=live,r=0.1] ~-1 ~ ~ scoreboard players add @s gol 1
# execute @e[family=block] ~1 ~ ~1 execute @e[family=live,r=0.1] ~-1 ~ ~-1 scoreboard players add @s gol 1

execute @e[family=live] ~-1 ~ ~-1 scoreboard players add @e[c=1,r=0.1] gol 1
execute @e[family=live] ~-1 ~ ~ scoreboard players add @e[c=1,r=0.1] gol 1
execute @e[family=live] ~-1 ~ ~1 scoreboard players add @e[c=1,r=0.1] gol 1

execute @e[family=live] ~1 ~ ~-1 scoreboard players add @e[c=1,r=0.1] gol 1
execute @e[family=live] ~1 ~ ~ scoreboard players add @e[c=1,r=0.1] gol 1
execute @e[family=live] ~1 ~ ~1 scoreboard players add @e[c=1,r=0.1] gol 1

execute @e[family=live] ~ ~ ~1 scoreboard players add @e[c=1,r=0.1] gol 1
execute @e[family=live] ~ ~ ~-1 scoreboard players add @e[c=1,r=0.1] gol 1



