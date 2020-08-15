import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create = ("""CREATE TABLE IF NOT EXISTS staging_events (se_id integer IDENTITY(0,1),
                                artist VARCHAR,
                                auth VARCHAR,
                                firstName VARCHAR,
                                gender VARCHAR,
                                itemInSession INTEGER,
                                lastName VARCHAR,
                                length DECIMAL,
                                level VARCHAR,
                                location VARCHAR,
                                method VARCHAR,
                                page VARCHAR,
                                registration BIGINT,
                                sessionId INTEGER,
                                song VARCHAR,
                                status INTEGER,
                                ts BIGINT,
                                userAgent VARCHAR,
                                user_id INTEGER);
""")
            

staging_songs_table_create = ("""CREATE TABLE IF NOT EXISTS staging_songs (
                                ss_id integer IDENTITY(0,1),
                                num_songs INTEGER,
                                artist_id TEXT,
                                artist_latitude TEXT,
                                artist_longitude TEXT,
                                artist_location TEXT,
                                artist_name TEXT,
                                song_id TEXT,
                                title TEXT,
                                duration TEXT,
                                year INTEGER
                                
                            )
""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
                                songplay_id INTEGER IDENTITY(0,1), 
                                start_time BIGINT NOT NULL, 
                                user_id INTEGER NOT NULL,
                                level VARCHAR(50),
                                song_id TEXT NOT NULL,
                                artist_id TEXT NOT NULL,
                                session_id INTEGER,
                                location VARCHAR(50),
                                user_agent VARCHAR
                            )
                                                        
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
                                user_id INTEGER PRIMARY KEY,
                                first_name VARCHAR(50),
                                last_name VARCHAR(50),
                                gender TEXT,
                                level VARCHAR(50)
                            )
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
                                song_id TEXT PRIMARY KEY,
                                title TEXT,
                                artist_id TEXT NOT NULL,
                                year INTEGER,
                                duration TEXT
                            )
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
                                artist_id TEXT PRIMARY KEY,
                                artist_name TEXT,
                                location TEXT,
                                latitude TEXT,
                                longitude TEXT
                            )
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
                                start_time TIMESTAMP PRIMARY KEY,
                                hour INTEGER,
                                day INTEGER,
                                week INTEGER,
                                month INTEGER,
                                year INTEGER,
                                weekday INTEGER
                            )
""")

# STAGING TABLES

staging_events_copy = ("""
                        COPY staging_events
                        FROM {}
                        iam_role {}
                        region 'us-west-2'
                        JSON {};
                        """).format(config['S3']['LOG_DATA'], config['IAM_ROLE']['ARN'], config['S3']['LOG_JSONPATH'])

staging_songs_copy = ("""
                        COPY staging_songs
                        FROM {}
                        iam_role {}
                        region 'us-west-2'
                        JSON 'auto';
                        """).format(config['S3']['SONG_DATA'], config['IAM_ROLE']['ARN'])

# FINAL TABLES

songplay_table_insert = ("""INSERT INTO songplays (start_time,
                                                   user_id,
                                                   level,
                                                   song_id,
                                                   artist_id,
                                                   session_id,
                                                   location,
                                                   user_agent)
                                    SELECT DISTINCT se.ts AS start_time, 
                                           se.user_id,
                                           se.level,
                                           ss.song_id,
                                           ss.artist_id,
                                           se.sessionId,
                                           se.location,
                                           se.userAgent
                                    FROM staging_events se
                                    JOIN staging_songs ss
                                        ON se.song = ss.title
                                        AND se.artist = ss.artist_name
                                        WHERE se.page = 'NextSong'
                                        AND se.user_id IS NOT NULL
""")

user_table_insert = ("""INSERT INTO users (user_id,
                            first_name,
                            last_name,
                            gender,
                            level)
                            SELECT DISTINCT user_id, firstName, lastName, gender, level
                            FROM staging_events
                            WHERE user_id IS NOT NULL
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)
                            SELECT song_id,
                                   title,
                                   artist_id,
                                   year,
                                   duration
                            FROM staging_songs
                            WHERE song_id IS NOT NULL

""")

artist_table_insert = ("""INSERT INTO artists (artist_id, artist_name, location, latitude, longitude)
                            SELECT DISTINCT artist_id,
                                   artist_name,
                                   artist_location,
                                   artist_latitude,
                                   artist_longitude
                            FROM staging_songs
                            WHERE artist_id IS NOT NULL
    
""")

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                        SELECT a.start_time,
                        EXTRACT (HOUR FROM a.start_time), EXTRACT (DAY FROM a.start_time),
                        EXTRACT (WEEK FROM a.start_time), EXTRACT (MONTH FROM a.start_time),
                        EXTRACT (YEAR FROM a.start_time), EXTRACT (WEEKDAY FROM a.start_time) FROM
                        (SELECT TIMESTAMP 'epoch' + start_time/1000 *INTERVAL '1 second' as start_time FROM songplays) a;

""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
