import os
from pos_app.adapters.ui.gui.main_app import Main_app
from kivy.config import Config
from pos_app.adapters.database.psql_adapter.connection import engine, get_db

def main():
    
    db = get_db()
    
    
    

if __name__ == '__main__':
    main()