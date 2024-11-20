

class BookRouter:
    second_db = "second"
    default_db = "default"
    second_db_models = ['book', 'author', 'order', 'product']

    def db_for_read(self, model, **hints):
        model_name = model._meta.model_name

        if model_name in self.second_db_models:
            return self.second_db
        else:
            return None

    def db_for_write(self, model, **hints):
        model_name = model._meta.model_name
        if model_name in self.second_db_models:
            return self.second_db
        else:
            return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name in self.second_db_models:
            return db == self.second_db
        else:
            return db == self.default_db
