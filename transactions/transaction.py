from praticando.extensions import db

def init_transaction(app):
    @app.teardown_request
    def finish_transaction(exception):
        if exception is not None:
            db.session.rollback()
        elif not app.config["TESTING"]:
            db.session.commit()