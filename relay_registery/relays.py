
# from flask_restful import Resource


# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._databse = shelve.open("relays.db")
#     return db

# @app.teardown_appcontext
# def teardown_db(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

