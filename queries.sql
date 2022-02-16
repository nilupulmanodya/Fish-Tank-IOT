/*queries for create tables for prediction db and sensor db
all tables consits both dbs without FishFeeder table
*/


CREATE TABLE ph (
 id int NOT NULL AUTO_INCREMENT,
 value float NOT NULL,
 time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY (id)
);

/*not consists in sensor db*/
CREATE TABLE FishFeeder (
 id int NOT NULL AUTO_INCREMENT,
 value float NOT NULL,
 time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY (id)
);

CREATE TABLE Humidity (
 id int NOT NULL AUTO_INCREMENT,
 value float NOT NULL,
 time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY (id)
);

CREATE TABLE LightIntensity (
 id int NOT NULL AUTO_INCREMENT,
 value float NOT NULL,
 time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY (id)
);

CREATE TABLE temperature (
 id int NOT NULL AUTO_INCREMENT,
 value float NOT NULL,
 time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY (id)
);


CREATE TABLE turbidity (
 id int NOT NULL AUTO_INCREMENT,
 value float NOT NULL,
 time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY (id)
);
