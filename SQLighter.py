# -*- coding: utf-8 -*-
import sqlite3


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_work(self, user_id):
        """Получаем один элемент из БД"""
        with self.connection:
            return self.cursor.execute('SELECT work_time FROM user_data where user_id = ?',
                                       (user_id,))

    def select_rest(self, user_id):
        """Получаем один элемент из БД"""
        with self.connection:
            return self.cursor.execute('SELECT rest_time FROM user_data where user_id = ?',
                                       (user_id,))

    def new_user(self, user_id):
        with self.connection:
            self.cursor.execute('INSERT INTO user_data VALUES (?, 25, 5)', (user_id,))

    def searh_user(self):
        with self.connection:
            return self.cursor.execute('SELECT user_id FROM user_data').fetchall()

    def write_work(self, time, user_id):
        with self.connection:
            self.cursor.execute('UPDATE user_data SET work_time = ? WHERE user_id = ?', (time, user_id,))

    def write_rest(self, time, user_id):
        with self.connection:
            self.cursor.execute('UPDATE user_data SET rest_time = ? WHERE user_id = ?', (time, user_id,))

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
