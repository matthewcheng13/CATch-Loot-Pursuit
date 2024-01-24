import sqlite3

conn = sqlite3.connect("game_progress.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        player_id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password_hash TEXT
    );""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        player_id INTEGER,
        world_id INTEGER,
        level_id INTEGER,
        unlocked_cats TEXT,
        unlocked_appearances TEXT,
        PRIMARY KEY (player_id, world_id, level_id),
        FOREIGN KEY (player_id) REFERENCES players(player_id)
    );""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS worlds (
        world_id INTEGER PRIMARY KEY,
        world_name TEXT,
        image TEXT
    );""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS levels (
        level_id INTEGER PRIMARY KEY,
        level_name TEXT,
        world_id INTEGER,
        dark_level INTEGER,
        predator_id INTEGER,
        prey_count INTEGER,
        image TEXT,
        FOREIGN KEY (world_id) REFERENCES worlds(world_id)
    );)""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cats (
        cat_id INTEGER PRIMARY KEY,
        cat_name TEXT,
        title TEXT,
        speed INTEGER,
        background INTEGER,
        fun_fact TEXT,
        image TEXT
    );)""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS prey (
        prey_id INTEGER PRIMARY KEY,
        prey_name TEXT,
        prey_speed INTEGER,
        prey_image TEXT
    )""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS predators (
        predator_id INTEGER PRIMARY KEY,
        predator_name TEXT,
        title TEXT,
        species TEXT,
        speed INTEGER,
        image TEXT
    )""")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS level_prey (
        level_id INTEGER,
        prey_id INTEGER,
        FOREIGN KEY (level_id) REFERENCES levels(level_id),
        FOREIGN KEY (prey_id) REFERENCES prey(prey_id),
        PRIMARY KEY (level_id, prey_id)
    )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS level_cat (
        level_id INTEGER,
        cat_id INTEGER,
        chance INTEGER,
        FOREIGN KEY (level_id) REFERENCES levels(level_id),
        FOREIGN KEY (cat_id) REFERENCES cats(cat_id),
        PRIMARY KEY (level_id, cat_id)
    )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS world_cat (
        world_id INTEGER,
        cat_id INTEGER,
        chance INTEGER,
        FOREIGN KEY (world_id) REFERENCES worlds(world_id),
        FOREIGN KEY (cat_id) REFERENCES cats(cat_id),
        PRIMARY KEY (world_id, cat_id)
    )''')