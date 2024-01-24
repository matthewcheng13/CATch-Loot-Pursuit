import sqlite3

conn = sqlite3.connect("game_progress.db")
cursor = conn.cursor()

# worlds
cursor.execute("INSERT INTO worlds (world_name, image) VALUES ('Carpeted Comforts', 'images/background/world/carpet.jpg)")
carpet_id = cursor.lastrowid
cursor.execute("INSERT INTO worlds (world_name, image) VALUES ('Gleaming Adobe', 'images/background/world/hard.jpg)")
hard_id = cursor.lastrowid
cursor.execute("INSERT INTO worlds (world_name, image) VALUES ('Urban Jungle', 'images/background/world/city.jpg)")
city_id = cursor.lastrowid
cursor.execute("INSERT INTO worlds (world_name, image) VALUES ('Verdant Meadows', 'images/background/world/grass.jpg)")
grass_id = cursor.lastrowid
cursor.execute("INSERT INTO worlds (world_name, image) VALUES ('Quiet Forest', 'images/background/world/forest.jpg)")
forest_id = cursor.lastrowid
cursor.execute("INSERT INTO worlds (world_name, image) VALUES ('Sandy Shores', 'images/background/world/beach.jpg)")
beach_id = cursor.lastrowid
cursor.execute("INSERT INTO worlds (world_name, image) VALUES ('Deep Abyss', 'images/background/world/ocean.jpg)")
ocean_id = cursor.lastrowid
cursor.execute("INSERT INTO worlds (world_name, image) VALUES ('Icy Expanse', 'images/background/world/snow.jpg)")
snow_id = cursor.lastrowid
cursor.execute("INSERT INTO worlds (world_name, image) VALUES ('Celestial Heights', 'images/background/world/sky.jpg)")
sky_id = cursor.lastrowid
cursor.execute("INSERT INTO worlds (world_name, image) VALUES ('Infernal Crater', 'images/background/world/volcano.jpg)")
volcano_id = cursor.lastrowid
cursor.execute("INSERT INTO worlds (world_name, image) VALUES ('Galactic Enigma', 'images/background/world/space.jpg)")
space_id = cursor.lastrowid

# cats

# main world theme
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Velvet', 'Sultan of Soft', '1', 'Filler', 'fact', 'images/sprites/velvet.jpg')")
velvet_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Marble', 'Trailblazer of Tile', '1', 'Filler', 'fact', 'images/sprites/marble.jpg')")
marble_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Metro', '', '1', 'Filler', 'fact', 'images/sprites/metro.jpg')")
metro_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Flora', 'Sultan of Soft', '1', 'Filler', 'fact', 'images/sprites/flora.jpg')")
flora_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Sylvan', 'Sentinel of the Forest', '1', 'Filler', 'fact', 'images/sprites/sylvan.jpg')")
sylvan_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Sandy', 'Sultan of Soft', '1', 'Filler', 'fact', 'images/sprites/sandy.jpg')")
sandy_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Marina', 'Explorer of the Deep', '1', 'Filler', 'fact', 'images/sprites/marina.jpg')")
marina_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Blizzard', 'Sultan of Soft', '1', 'Filler', 'fact', 'images/sprites/blizzard.jpg')")
blizzard_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Zephyr', 'Guardian of the Skies', '1', 'Filler', 'fact', 'images/sprites/zephyr.jpg')")
zephyr_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Ember', 'Sultan of Soft', '1', 'Filler', 'fact', 'images/sprites/ember.jpg')")
ember_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Nova', 'Sultan of Soft', '1', 'Filler', 'fact', 'images/sprites/nova.jpg')")
nova_id = cursor.lastrowid

# alternate world theme
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Willow', '', '1', 'Filler', 'fact', 'images/sprites/willow.jpg')")
willow_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Mistral', 'Wind Whisperer', '1', 'Filler', 'fact', 'images/sprites/mistral.jpg')")
mistral_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Marlin', 'Sultan of Soft', '1', 'Filler', 'fact', 'images/sprites/marlin.jpg')")
marlin_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Obsidian', 'Sultan of Soft', '1', 'Filler', 'fact', 'images/sprites/obsidian.jpg')")
obsidian_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Quake', 'Sultan of Soft', '1', 'Filler', 'fact', 'images/sprites/quake.jpg')")
quake_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Cosmos', 'Sultan of Soft', '1', 'Filler', 'fact', 'images/sprites/cosmos.jpg')")
cosmos_id = cursor.lastrowid

# alternate skill
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Shadow', 'Master of Illusion', '1', 'Filler', 'fact', 'images/sprites/shadow.jpg')")
shadow_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Havoc', 'Harbinger of Chaos', '1', 'Filler', 'fact', 'images/sprites/havoc.jpg')")
havoc_id = cursor.lastrowid

# other
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('?', 'The Sunlight Basker', '1', 'Filler', 'fact', 'images/sprites/notsure.jpg')")
notsure_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Luna', 'The Dreamcatcher', '1', 'Filler', 'fact', 'images/sprites/luna.jpg')")
luna_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Mischief', 'The Playful Prankster', '1', 'Filler', 'fact', 'images/sprites/mischief.jpg')")
mischief_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Trill', 'The Voice of Serenity', '1', 'Filler', 'fact', 'images/sprites/trill.jpg')")
trill_id = cursor.lastrowid
cursor.execute("INSERT INTO cats (cat_name, title, speed, background, fun_fact, image) VALUES ('Chunk', 'Philosopher of the Ruins', '1', 'Filler', 'fact', 'images/sprites/chunk.jpg')")
chunk_id = cursor.lastrowid

# predators
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Rex', 'The Carpet Conqueror', 'Dog', '1', 'images/sprites/rex.jpg')")
rex_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Buster', 'The Timber Tamer', 'Dog', '1', 'images/sprites/buster.jpg')")
buster_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Spike', 'The Tile Terror', 'Dog', '1', 'images/sprites/spike.jpg')")
spike_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Duke', 'The Mighty', 'Dog', '1', 'images/sprites/duke.jpg')")
duke_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Rusty', 'The ', 'Dog', '1', 'images/sprites/rusty.jpg')")
rusty_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Rufus', 'The Free', 'Dog', '1', 'images/sprites/rufus.jpg')")
rufus_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Scythe', 'The Cutthroat', 'Fox', '1', 'images/sprites/scythe.jpg')")
scythe_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Quickscar', '', 'Wolf', '1', 'images/sprites/quickscar.jpg')")
quickscar_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Slyy', 'The Nimble Assassin', 'Fox', '1', 'images/sprites/slyy.jpg')")
slyy_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Spirit', 'Master of Evasion', 'Wolf', '1', 'images/sprites/spirit.jpg')")
spirit_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Scruff', 'Hunter of the Sand', 'Dog', '1', 'images/sprites/scruff.jpg')")
scruff_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Aquila', 'The Shoreline Sovereign', 'Osprey', '1', 'images/sprites/aquila.jpg')")
aquila_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Leviathan', 'The Coastal Behemoth', 'Large Fish', '1', 'images/sprites/leviathan.jpg')")
leviathan_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Typhara', 'The Ocean\'s Wrath', 'Shark', '1', 'images/sprites/typhara.jpg')")
typhara_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Silvertooth', 'The Alpha Wolf', 'Wolf', '1', 'images/sprites/silvertooth.jpg')")
silvertooth_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Nyx', '', 'Fox', '1', 'images/sprites/nyx.jpg')")
nyx_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Bullet', 'The Silent Release', 'Owl', '1', 'images/sprites/bullet.jpg')")
bullet_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Zlush', 'The Frozen Titan', 'Yeti', '1', 'images/sprites/zlush.jpg')")
zlush_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Talon', 'The Deadly Missile', 'Hawk', '1', 'images/sprites/talon.jpg')")
talon_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Nimbus', 'The Skyward Ruler', 'Eagle', '1', 'images/sprites/nimbus.jpg')")
nimbus_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Tempest', 'The Stormcaster', 'Griffin', '1', 'images/sprites/tempest.jpg')")
tempest_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Doomflyer', 'The Rocky Blade', 'Vulture', '1', 'images/sprites/doomflyer.jpg')")
doomflyer_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Glisz', 'The Lizard King', 'Large Lizard', '1', 'images/sprites/glisz.jpg')")
glisz_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Ignis', 'The Lava Lord', 'Lava Monster', '1', 'images/sprites/ignis.jpg')")
ignis_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Umbra', 'The Stellar Nomad', 'Large Alien', '1', 'images/sprites/umbra.jpg')")
umbra_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Zaraq', '', 'Large Alien', '1', 'images/sprites/zaraq.jpg')")
zaraq_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Xenon', 'The Interstellar', 'Large Alien', '1', 'images/sprites/xenon.jpg')")
xenon_id = cursor.lastrowid
cursor.execute("INSERT INTO predators (predator_name, title, species, speed, image) VALUES ('Vortex', 'The Cosmic Abyss', 'Black Hole', '1', 'images/sprites/vortex.jpg')")
vortex_id = cursor.lastrowid


# prey
cursor.execute("INSERT INTO prey (prey_name, prey_speed, prey_image) VALUES (?,?,?)", ("Mouse", "1", "images/sprites/mouse.jpg"))
mouse_id = cursor.lastrowid
cursor.execute("INSERT INTO prey (prey_name, prey_speed, prey_image) VALUES (?,?,?)", ("Rat", "1", "images/sprites/rat.jpg"))
rat_id = cursor.lastrowid
cursor.execute("INSERT INTO prey (prey_name, prey_speed, prey_image) VALUES (?,?,?)", ("Mole", "1", "images/sprites/mole.jpg"))
mole_id = cursor.lastrowid
cursor.execute("INSERT INTO prey (prey_name, prey_speed, prey_image) VALUES (?,?,?)", ("Rabbit", "1", "images/sprites/rabbit.jpg"))
rabbit_id = cursor.lastrowid
cursor.execute("INSERT INTO prey (prey_name, prey_speed, prey_image) VALUES (?,?,?)", ("Squirrel", "1", "images/sprites/squirrel.jpg"))
squirrel_id = cursor.lastrowid
cursor.execute("INSERT INTO prey (prey_name, prey_speed, prey_image) VALUES (?,?,?)", ("Lizard", "1", "images/sprites/lizard.jpg"))
lizard_id = cursor.lastrowid
cursor.execute("INSERT INTO prey (prey_name, prey_speed, prey_image) VALUES (?,?,?)", ("Shrew", "1", "images/sprites/shrew.jpg"))
shrew_id = cursor.lastrowid
cursor.execute("INSERT INTO prey (prey_name, prey_speed, prey_image) VALUES (?,?,?)", ("Fish", "1", "images/sprites/fish.jpg"))
fish_id = cursor.lastrowid
cursor.execute("INSERT INTO prey (prey_name, prey_speed, prey_image) VALUES (?,?,?)", ("Chipmunk", "1", "images/sprites/chipmunk.jpg"))
chipmunk_id = cursor.lastrowid
cursor.execute("INSERT INTO prey (prey_name, prey_speed, prey_image) VALUES (?,?,?)", ("Lemming", "1", "images/sprites/lemming.jpg"))
lemming_id = cursor.lastrowid
cursor.execute("INSERT INTO prey (prey_name, prey_speed, prey_image) VALUES (?,?,?)", ("Bird", "1", "images/sprites/bird.jpg"))
bird_id = cursor.lastrowid
cursor.execute("INSERT INTO prey (prey_name, prey_speed, prey_image) VALUES (?,?,?)", ("Small Alien", "1", "images/sprites/small_alien.jpg"))
small_alien_id = cursor.lastrowid

# level_prey

# carpet
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 1-1', carpet_id, 0, -1, 1, 'images/background/level/carpet_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, velvet_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 1-2', carpet_id, 0, -1, 1, 'images/background/level/carpet_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, velvet_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 1-3', carpet_id, 0, -1, 1, 'images/background/level/carpet_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, velvet_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 1-4', carpet_id, 0, -1, 2, 'images/background/level/carpet_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, velvet_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 1-5', carpet_id, 0, -1, 2, 'images/background/level/carpet_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, velvet_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 1-6', carpet_id, 1, -1, 1, 'images/background/level/carpet_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, velvet_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 1-7', carpet_id, 0, -1, 2, 'images/background/level/carpet_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, velvet_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 1-8', carpet_id, 0, rex_id, 0, 'images/background/level/carpet_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, velvet_id, 100))

# hard floor
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 2-1', hard_id, 0, -1, 2, 'images/background/level/hard_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marble_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 2-2', hard_id, 1, -1, 2, 'images/background/level/hard_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marble_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 2-3', hard_id, 0, -1, 2, 'images/background/level/hard_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marble_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 2-4', hard_id, 0, -1, 2, 'images/background/level/hard_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marble_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 2-5', hard_id, 1, -1, 3, 'images/background/level/hard_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marble_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 2-6', hard_id, 0, buster_id, 0, 'images/background/level/hard_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marble_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 2-7', hard_id, 0, -1, 2, 'images/background/level/hard_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marble_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 2-8', hard_id, 1, -1, 2, 'images/background/level/hard_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marble_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 2-9', hard_id, 0, -1, 2, 'images/background/level/hard_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marble_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 2-10', hard_id, 0, spike_id, 0, 'images/background/level/hard_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marble_id, 100))

# city
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 3-1', city_id, 1, -1, 2, 'images/background/level/city_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, metro_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 3-2', city_id, 0, -1, 3, 'images/background/level/city_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rat_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, metro_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 3-3', city_id, 1, -1, 2, 'images/background/level/city_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rat_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, metro_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 3-4', city_id, 0, -1, 3, 'images/background/level/city_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rat_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, metro_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 3-5', city_id, 1, -1, 3, 'images/background/level/city_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rat_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, metro_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 3-6', city_id, 0, duke_id, 0, 'images/background/level/city_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, metro_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 3-7', city_id, 0, -1, 2, 'images/background/level/city_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rat_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, metro_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 3-8', city_id, 1, -1, 3, 'images/background/level/city_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rat_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, metro_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 3-9', city_id, 0, -1, 3, 'images/background/level/city_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rat_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, metro_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 3-10', city_id, 1, rusty_id, 0, 'images/background/level/city_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, metro_id, 100))

# grass
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 4-1', grass_id, 0, -1, 3, 'images/background/level/grass_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, flora_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 4-2', grass_id, 0, -1, 3, 'images/background/level/grass_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mole_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, flora_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 4-3', grass_id, 1, -1, 3, 'images/background/level/grass_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mole_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, flora_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 4-4', grass_id, 0, rufus_id, 0, 'images/background/level/grass_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, flora_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 4-5', grass_id, 0, -1, 3, 'images/background/level/grass_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rabbit_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, flora_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 4-6', grass_id, 0, -1, 3, 'images/background/level/grass_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rabbit_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, flora_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 4-7', grass_id, 0, -1, 3, 'images/background/level/grass_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rabbit_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, flora_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 4-8', grass_id, 0, scythe_id, 0, 'images/background/level/grass_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, flora_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 4-9', grass_id, 0, -1, 3, 'images/background/level/grass_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mole_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rabbit_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, flora_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 4-10', grass_id, 1, -1, 4, 'images/background/level/grass_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mole_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rabbit_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, flora_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 4-11', grass_id, 0, quickscar_id, 0, 'images/background/level/grass_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, flora_id, 100))

# forest
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 5-1', forest_id, 0, -1, 4, 'images/background/level/forest_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, squirrel_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sylvan_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 5-2', forest_id, 0, -1, 4, 'images/background/level/forest_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, squirrel_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sylvan_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 5-3', forest_id, 1, -1, 3, 'images/background/level/forest_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, squirrel_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sylvan_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 5-4', forest_id, 0, -1, 3, 'images/background/level/forest_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, squirrel_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, lizard_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sylvan_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 5-5', forest_id, 0, -1, 3, 'images/background/level/forest_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, squirrel_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, lizard_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sylvan_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 5-6', forest_id, 0, -1, 4, 'images/background/level/forest_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, squirrel_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, lizard_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sylvan_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 5-7', forest_id, 0, slyy_id, 0, 'images/background/level/forest_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sylvan_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 5-8', forest_id, 1, -1, 3, 'images/background/level/forest_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, shrew_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, squirrel_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, lizard_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sylvan_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 5-9', forest_id, 0, -1, 4, 'images/background/level/forest_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, shrew_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, squirrel_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, lizard_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sylvan_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 5-10', forest_id, 1, spirit_id, 0, 'images/background/level/forest_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sylvan_id, 100))

# beach
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 6-1', beach_id, 0, -1, 3, 'images/background/level/beach_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, bird_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sandy_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 6-2', beach_id, 0, -1, 4, 'images/background/level/beach_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, bird_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sandy_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 6-3', beach_id, 1, -1, 3, 'images/background/level/beach_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, bird_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sandy_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 6-4', beach_id, 0, -1, 4, 'images/background/level/beach_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, bird_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sandy_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 6-5', beach_id, 0, -1, 4, 'images/background/level/beach_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, bird_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, lizard_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sandy_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 6-6', beach_id, 0, -1, 4, 'images/background/level/beach_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, bird_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, lizard_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sandy_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 6-7', beach_id, 0, -1, 4, 'images/background/level/beach_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, bird_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sandy_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 6-8', beach_id, 1, -1, 3, 'images/background/level/beach_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, bird_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sandy_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 6-9', beach_id, 0, scruff_id, 0, 'images/background/level/beach_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sandy_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 6-10', beach_id, 0, -1, 1, 'images/background/level/beach_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, fish_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sandy_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 6-11', beach_id, 1, -1, 2, 'images/background/level/beach_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, fish_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sandy_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 6-12', beach_id, 0, leviathan_id, 0, 'images/background/level/beach_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, sandy_id, 100))

# ocean
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 7-1', ocean_id, 0, -1, 2, 'images/background/level/ocean_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, fish_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marina_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 7-2', ocean_id, 0, -1, 2, 'images/background/level/ocean_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, fish_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marina_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 7-3', ocean_id, 1, -1, 1, 'images/background/level/ocean_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, fish_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marina_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 7-4', ocean_id, 0, -1, 2, 'images/background/level/ocean_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, fish_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marina_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 7-5', ocean_id, 1, -1, 2, 'images/background/level/ocean_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, fish_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marina_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 7-6', ocean_id, 0, -1, 2, 'images/background/level/ocean_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, fish_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marina_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 7-7', ocean_id, 1, typhara_id, 0, 'images/background/level/ocean_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, marina_id, 100))

# snow
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-1', snow_id, 0, -1, 4, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-2', snow_id, 0, -1, 4, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, lemming_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-3', snow_id, 0, -1, 4, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, lemming_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-4', snow_id, 0, -1, 4, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, lemming_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rabbit_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-5', snow_id, 0, silvertooth_id, 0, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-6', snow_id, 0, -1, 4, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, chipmunk_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-7', snow_id, 0, -1, 4, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, chipmunk_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rabbit_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-8', snow_id, 0, -1, 4, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, chipmunk_id))
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rabbit_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-9', snow_id, 0, nyx_id, 0, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-10', snow_id, 0, -1, 4, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rabbit_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-11', snow_id, 0, -1, 4, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rabbit_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-12', snow_id, 0, -1, 4, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, rabbit_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-13', snow_id, 0, bullet_id, 0, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-14', snow_id, 0, -1, 4, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-15', snow_id, 0, -1, 4, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-16', snow_id, 0, -1, 4, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 8-17', snow_id, 0, zlush_id, 0, 'images/background/level/snow_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, blizzard_id, 100))

# sky
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 9-1', sky_id, 0, -1, 'images/background/level/sky_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, zephyr_id, 100))

# volcano
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 10-1', volcano_id, 0, -1,'images/background/level/volcano_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, ember_id, 100))

# space
cursor.execute("INSERT INTO levels (level_name, world_id, dark_level, predator_id, prey_count, image) VALUES (?,?,?,?,?,?)", ('Level 11-1', space_id, 1, -1, 'images/background/level/space_level.jpg'))
curr_level = cursor.lastrowid
cursor.execute("INSERT INTO level_prey (level_id, prey_id) VALUES (?,?)", (curr_level, mouse_id))
cursor.execute("INSERT INTO level_cat (level_id, cat_id) VALUES (?,?)", (curr_level, nova_id, 100))
