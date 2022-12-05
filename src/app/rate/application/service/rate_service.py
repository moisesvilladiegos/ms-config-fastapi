from src.app.rate.infraestructure.repository import rate_repository

def get_all(db):
    data = rate_repository.get_all(db)
    return data

def get_by_id(id, db):
    data = rate_repository.get_by_id(id, db)
    return data

def save(item, db):
    data = rate_repository.save(item, db)
    return data

def delete(id, db):
    data = rate_repository.delete_v1(id, db)
    return data

def put(id, item, db):
    data = rate_repository.put(id, item, db)
    return data