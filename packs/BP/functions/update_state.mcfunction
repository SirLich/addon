

# Handle the live cells
execute @e[family=live,scores={gol=!2..3}] ~ ~ ~ function dead

# Handle dead cells
execute @e[family=dead,scores={gol=3}] ~ ~ ~ function live

# Reset
scoreboard players set @e[family=block] gol 0




