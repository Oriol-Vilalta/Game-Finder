CREATE TABLE 'gamefinder_genre' (
    'id' serial NOT NULL PRIMARY KEY,
    'name' varchar(50) NOT NULL
);

CREATE TABLE 'gamefinder_developingcompany' (
    'id' serial NOT NULL PRIMARY KEY,
    'name' varchar(200) NOT NULL
);

CREATE TABLE 'gamefinder_platform' (
    'id' serial NOT NULL PRIMARY KEY,
    'name' varchar(200) NOT NULL,
    'developingCompany_id' integer NOT NULL REFERENCES 'gamefinder_developingcompany' ('id') ON DELETE CASCADE
);

CREATE TABLE 'gamefinder_game' (
    'id' serial NOT NULL PRIMARY KEY,
    'title' varchar(200) NOT NULL,
    'rating' numeric(2, 1) NOT NULL,
    'genre_id' integer NOT NULL REFERENCES 'gamefinder_genre' ('id') ON DELETE CASCADE,
    'platform_id' integer NOT NULL REFERENCES 'gamefinder_platform' ('id') ON DELETE CASCADE,
    'developingCompany_id' integer NOT NULL REFERENCES 'gamefinder_developingcompany' ('id') ON DELETE CASCADE
);

INSERT INTO gamefinder_genre(name) values('ACCIO');
INSERT INTO gamefinder_genre(name) values('SHOOTER');
INSERT INTO gamefinder_genre(name) values('PLATAFORMA');
INSERT INTO gamefinder_genre(name) values('MOBA');

INSERT INTO gamefinder_developingcompany(id, name) values(1, 'NINTENDO');
INSERT INTO gamefinder_developingcompany(id, name) values(2, 'UBISOFT');
INSERT INTO gamefinder_developingcompany(id, name) values(3, 'SONY');

INSERT INTO gamefinder_platform values(1, 'WII', 1);
INSERT INTO gamefinder_platform values(2, 'XBOX', 2);
INSERT INTO gamefinder_platform values(3, 'PLAY STATION 4', 3);

