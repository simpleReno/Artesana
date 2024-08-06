import os
from pos_app.adapters.ui.gui.main_app import Main_app
from kivy.config import Config
from pos_app.adapters.database.sqlite_adapter.connection import Connection

def main():
    
    DB = Connection.create_tables()

if __name__ == '__main__':
    main()