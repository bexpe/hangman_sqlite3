#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import game_class
# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')


def connect_to_db(player):
    connection = sqlite3.connect('game.db')
    connection.row_factory = sqlite3.Row
    # acces to columns through indexes and names
    cursor = connection.cursor()  # object of cursor created
    create_main_table(cursor)
    create_sub_table(cursor)
    add_to_winners(player, cursor, connection)
    read_data_from_db(cursor)


def create_main_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS game;")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS game (
            id INTEGER PRIMARY KEY ASC,
            game_name varchar(250) NOT NULL
        )""")


def create_sub_table(cursor):
    cursor.executescript("""
        DROP TABLE IF EXISTS player;
        CREATE TABLE IF NOT EXISTS player (
            id INTEGER PRIMARY KEY ASC,
            name varchar(250) NOT NULL,
            score INTEGER NOT NULL,
            game_id INTEGER NOT NULL,
            FOREIGN KEY(game_id) REFERENCES game(id)
        )""")


def add_to_winners(player, cursor, connection):
    cursor.execute('INSERT INTO game VALUES(NULL, ?);', ('hangman',))
    cursor.execute('SELECT id FROM game WHERE game_name = ?', ('hangman',))
    game_id = cursor.fetchone()[0]
    players = (
        (None, player.name, player.score, game_id),
        (None, 'hangmanger', 1500, game_id),
        (None, 'Piotr', 5, game_id)
    )
    cursor.executemany('INSERT INTO player VALUES(?,?,?,?)', players)
    connection.commit()


def read_data_from_db(cursor):
    """Function dowloads and prints data form database."""
    cursor.execute(
        """
        SELECT player.id,name,score FROM player,game
        WHERE player.game_id=game.id ORDER BY score DESC
        """)
    players = cursor.fetchall()
    for player in players:
        print(player['score'], player['name'])
    print()
