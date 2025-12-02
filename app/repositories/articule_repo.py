from asyncpg import Connection


class ArticuleRepository():
    def __init__(self, conn: Connection, queries_loader):
        self.conn = conn
        self.queries = queries_loader
    
