--
-- Author: Cyril GENISSON
-- Created: 08/02/2024
-- Updated: 08/02/2024
--
-- filename: myDiscord.sql
-- Description:
--
USE mydiscord;

CREATE TABLE users(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE,
    nickname VARCHAR(100) NOT NULL,
    pwd BLOB NOT NULL,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(50) NOT NULL
) ENGINE = InnoDB;

INSERT INTO users(email, nickname, pwd, firstname, lastname) VALUE ('cyril.genisson@local.lan', 'Kaman','b\'$2b$12$uo/QuFp6J6UfQWMzYwwHFurIVxTBYgyUG9PSdqiJtvykuwBp2UsnW\'', 'Cyril', 'GENISSON');

CREATE TABLE rooms(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30),
    type ENUM('Public', 'Private') DEFAULT 'Public'
) ENGINE = InnoDB;

INSERT INTO rooms(name) VALUE ('default');

CREATE TABLE default_room(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    id_user INT UNSIGNED NOT NULL,
    mes LONGTEXT NOT NULL,
    date TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT  `fk_default_room_user` FOREIGN KEY (id_user) REFERENCES users(id)
                         ON DELETE CASCADE
                         ON UPDATE CASCADE
) ENGINE = InnoDB;

CREATE TABLE default_rights(
    id INT UNSIGNED PRIMARY KEY NOT NULL,
    role ENUM ('ADMIN', 'USER') DEFAULT 'USER',
    ban BOOLEAN DEFAULT FALSE,
    CONSTRAINT `fk_default_rights_user` FOREIGN KEY (id) REFERENCES users(id)
                           ON DELETE CASCADE
                           ON UPDATE CASCADE
) ENGINE = InnoDB;

INSERT INTO default_rights(id, role, ban) VALUE (1, 'ADMIN', FALSE);

CREATE TABLE connexions(
    id_user INT UNSIGNED NOT NULL ,
    uuid_client VARCHAR(255) NOT NULL ,
    connect BOOLEAN DEFAULT FALSE,
    last_connection TIMESTAMP DEFAULT NOW(),
    CONSTRAINT `fk_connexions_user` FOREIGN KEY (id_user) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `pk_connexions` PRIMARY KEY (id_user, uuid_client)
) ENGINE = InnoDB;
