from src.app.parking_space.infraestructure.repository import parking_space_repository

def get_all(db):
    data = parking_space_repository.get_all(db)
    return data

def get_by_id(id, db):
    data = parking_space_repository.get_by_id(id, db)
    return data

def save(item, db):
    data = parking_space_repository.save(item, db)
    return data

def delete(id, db):
    data = parking_space_repository.delete_v1(id, db)
    return data

def put(id, item, db):
    data = parking_space_repository.put(id, item, db)
    return data