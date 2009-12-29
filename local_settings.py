# -*- coding: utf-8 -*-

import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

LOCAL = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'postgresql_psycopg2' # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'db_principal'          # Or path to database file if using sqlite3.
DATABASE_USER = 'nana'                  # Not used with sqlite3.
DATABASE_PASSWORD = 'nana'              # Not used with sqlite3.
DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = '5432'                  # Set to empty string for default. Not used with sqlite3.
