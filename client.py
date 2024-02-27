#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: client.py
@created: 08/02/2024

@project: myDiscord
@licence: GPLv3
"""
from db import Db
from lib import *
import uuid
# from threading import Thread


class Client:
    """
    Client class
    """
    def __init__(self):
        self.__db = Db()
        self.__state_connect = False
        self.__id_connect = None
        self.__uuid = str(uuid.uuid4())
        self.__channel_name = 'Default'
        self.rooms = []
        self.messages = []

    def get_state(self):
        """
        Returns the current state of the connected client
        :return: Bool True if the client is connected, False otherwise
        """
        return self.__state_connect

    def get_channels(self):
        """
        Returns a list of channels in the database
        :return: List of channels in the database
        """
        if self.__state_connect:
            req = "SELECT id, name, type FROM rooms"
            return self.__db.query(req)

    def change_state_connect(self):
        """
        Change the state connection of the client
        :return: None
        """
        if self.__state_connect:
            self.__state_connect = False
        else:
            self.__state_connect = True
            self.__uuid = str(uuid.uuid4())

    def get_id(self):
        """
        Returns the id of the user in the database
        :return: int id of the user in the database
        """
        return self.__id_connect

    def get_uuid(self):
        """
        returns the uuid of the client.
        :return: str uuid
        """
        return self.__uuid

    def register(self, firstname, lastname, email, password, nickname="Anonymous"):
        """
        Register a new user in the database using the provided parameters
        :param firstname: user's first
        :param lastname: user's last name
        :param email: user's email
        :param password: user's password
        :param nickname: user's nickname
        :return: None
        """
        hash_password = hash_pass(password)
        self.__db.connect()
        req = f"INSERT INTO users(firstname, lastname, email, pwd, nickname) VALUE (\'{firstname}\', \'{lastname}\', \'{email}\', \"{hash_password}\", \'{nickname}\')"
        self.__db.query(req, mod=True)
        self.__db.disconnect()

    def change_email(self, email):
        """
        Change email address of the user
        :param email: new email address of the user
        :return: None
        """
        req = f"UPDATE users SET email = \'{email}\' where id = {self.get_id()}"
        self.__db.query(req, mod=True)

    def change_password(self, password):
        """
        Change user's password
        :param password: new password
        :return: None
        """
        req = f"UPDATE users SET password = \'{hash_pass(password)}\' where id = {self.get_id()}"
        self.__db.query(req, mod=True)

    def change_nickname(self, nickname):
        """
        Change the Nickname of the user
        :param nickname: new nickname of the user
        :return: None
        """
        req = f"UPDATE users SET nickname = \'{nickname}\' where id = {self.get_id()}"
        self.__db.query(req, mod=True)

    def connect(self, email, password):
        """
        Connects to the database with the provided email and password
        :param email: email address of the user
        :param password: password of the user
        :return:  none
        """
        self.__db.connect()
        req = f"SELECT `pwd`, `id` FROM users WHERE `email` = \'{email}\'"
        response = self.__db.query(req)
        if response:
            if check_pass(password, response[0][0][2:-1]):
                self.change_state_connect()
                self.__id_connect = response[0][1]
                req = f"INSERT INTO connexions(id_user, uuid_client, connect) VALUES (\'{self.get_id()}\', \'{self.get_uuid()}\', TRUE)"
                self.__db.query(req, mod=True)
            else:
                print("Wrong password")
                self.__state_connect = False
        else:
            print("Wrong login")
            self.__state_connect = False

    def logout(self):
        """
        Logout method of the client
        :return: None
        """
        if self.get_state():
            req = f"UPDATE connexions SET connexions.connect = FALSE WHERE id_user = {self.get_id()} AND uuid_client = \'{self.get_uuid()}\'"
            self.__db.query(req, mod=True)
            self.change_state_connect()
            self.__db.disconnect()

    def create_room(self, channel):
        """
        Create a new room
        :param channel: string channel_name [Public | Private]
        :return: None
        """
        self.command("! CREATE " + channel)

    def destroy_room(self, channel):
        """
        Destroy channel room
        :param channel: string channel_name
        :return: None
        """
        self.command("! DESTROY " + channel)

    def join_room(self, channel):
        """
        Join channel room
        :param channel: string channel_name
        :return: None
        """
        self.command("! JOIN " + channel)

    def leave_room(self, channel):
        """
        Leave channel room
        :param channel: string channel name
        :return: None
        """
        self.command("! LEAVE " + channel)

    def display_rooms(self):
        """
        Display all channel rooms
        :return: List of channel rooms
        """
        return self.command("! ROOMS")

    def display_users_rooms(self):
        """
        Display all users connected
        :return: List of users
        """
        return self.command("! USERS")

    def display_msg(self, room_name):
        """
        Display all messages in channel room name
        :param room_name: string room_name
        :return: list of messages
        """
        if self.__state_connect:
            req = f"SELECT type FROM {room_name}_rooms WHERE name = '{room_name}'"
            if self.__db.query(req) == 'Public':
                req = f"SELECT * FROM {room_name}_room WHERE date = DAY(NOW())"
                self.__db.query(req)
            else:
                req = f"SELECT * FROM {room_name}"
            return self.__db.query(req)

    def command(self, action: str):
        """
        :param action: Can be
        'CREATE ROOM_NAME [PUBLIC | PRIVATE]'
        'ADD ROOM_NAME SET USERNAME [ADMIN | USER]= \'{action}\'
        'BANNER ROOM_NAME USERNAME'
        'DESTROY ROOM_NAME'
        'JOIN ROOM_NAME'
        'LEAVE ROOM_NAME'
        'ROOMS'
        'USERS'
        :return: List | None
        """
        if self.__state_connect and action[0] == '!':
            cmd = action.split(' ')
            cmd.pop(0)
            match cmd[0].lower():
                case 'create':
                    if isinstance(cmd[1], str) is False:
                        return None
                    para_1 = ("id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,\n",
                              "id_user INT UNSIGNED NOT NULL,\n",
                              "mes LONGTEXT NOT NULL,\n",
                              "date TIMESTAMP NOT NULL DEFAULT NOW(),\n",
                              f"CONSTRAINT  fk_{cmd[1]}_room_user FOREIGN KEY (id_user) REFERENCES users (id)\n",
                              "ON DELETE CASCADE\n",
                              "ON UPDATE CASCADE",
                              )
                    para_2 = ("id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,\n",
                              "role ENUM ('ADMIN', 'USER') DEFAULT 'USER',\n",
                              "ban BOOLEAN DEFAULT FALSE,\n",
                              f"CONSTRAINT fk_{cmd[1]}_rights_user FOREIGN KEY (id) REFERENCES users (id)\n",
                              "ON DELETE CASCADE\n",
                              "ON UPDATE CASCADE"
                              )
                    para_1 = ' '.join(para_1)
                    para_2 = ' '.join(para_2)
                    req = []
                    if len(cmd) == 3 and cmd[2].lower() == 'private':
                        req.append(f"INSERT INTO rooms(name, type) VALUES (\'{cmd[1]}\', 'Private');")
                    else:
                        req.append(f"INSERT INTO rooms(name, type) VALUES (\'{cmd[1]}\', 'Public');")
                    req.append(f"CREATE TABLE {cmd[1]}_room({para_1}) ENGINE = InnoDB;")
                    req.append(f"CREATE TABLE {cmd[1]}_rights({para_2}) ENGINE = InnoDB;")
                    req.append(f"INSERT INTO {cmd[1]}_rights(id, role, ban) VALUES ({self.get_id()}, 'ADMIN', FALSE);")
                    for k in req:
                        self.__db.query(k, mod=True)
                case 'join':
                    if cmd[1] in self.__db.query(f"SELECT name FROM rooms WHERE name = \'{cmd[1]}\'"):
                        self.__channel_name = cmd[1]
                case 'destroy':
                    req = f"SELECT role FROM {cmd[1]}_rights WHERE id = {self.get_id()}"
                    if self.__db.query(req)[0][0] == "ADMIN":
                        request = list([])
                        request.append(f"DROP TABLE {cmd[1]}_room;")
                        request.append(f"DROP TABLE {cmd[1]}_rights;")
                        request.append(f"DELETE FROM rooms WHERE `name` = \'{cmd[1]}\'")
                        for k in request:
                            self.__db.query(k, mod=True)
                    else:
                        print("No rights found for this action!")
                case 'rooms':
                    req = f"SELECT * FROM rooms"
                    return self.__db.query(req)
                case 'users':
                    req = f"SELECT * FROM users"
                    return self.__db.query(req)
                case _:
                    return "Invalid command"


if __name__ == "__main__":
    client = Client()
    client.register('Cyril', 'GENISSON', 'cyril.genisson@local.lan', 'PassWord1!', nickname='Kaman')
    client.connect("cyril.geisson@local.lan", "PassWor1!")
    client.create_room('')
    client.logout()
