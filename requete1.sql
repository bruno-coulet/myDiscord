CREATE TABLE default_room(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    id_user INT UNSIGNED NOT NULL,
    mes LONGTEXT NOT NULL,
    DATE TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT  `fk_default_room_user` FOREIGN KEY (id_user) REFERENCES users(id)
                         ON DELETE CASCADE
                         ON UPDATE CASCADE`bruno-coulet_myDiscord`default_room
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