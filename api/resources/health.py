from flask_restful import Resource


class Health(Resource):
    def __init__(self, db):
        self.db = db

    def get(self):
        try:
            self.db.engine.execute('SELECT 1+1')
            return {"data": "Working"}, 200
        except Exception as e:
            return {"errors": [{"title": "Error", "details": str(e)}]}, 500
