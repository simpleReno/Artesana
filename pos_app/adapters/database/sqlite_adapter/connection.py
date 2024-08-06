from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connection:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
    
    def close(self):
        self.session.close()
        self.engine.dispose()
        
    def create_tables(self):
        self.Base.metadata.create_all(self.engine)
        
