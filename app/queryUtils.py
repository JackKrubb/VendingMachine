from app.schema import *

noContent204 = '', 204


def dict_helper(objlist):
    result = [item.obj_to_dict() for item in objlist]
    return result


def addObjToDB(obj):
    session = Session()
    try:
        session.add(obj)
        session.commit()
        session.close()
    except:
        session.close()

def selectObj(table_name, search_params):
    session = Session()
    obj = None
    try:
        obj = session.query(table_name).filter_by(**search_params).first()
        session.close()
    except:
        session.close()
    return obj

def selectObjList(table_name, search_params):
    session = Session()
    obj_list = None
    try:
        obj_list = session.query(table_name).filter_by(**search_params).all()
        session.close()
    except:
        session.close()
    return obj_list

def deleteObjFromDB(obj):
    if obj is not None:
        session = Session()
        try:
            session.delete(obj)
            session.commit()
            session.close()
        except:
            session.close()


def getAllFromTable(table_class):
    session = Session()
    queries = None
    try:
        queries = session.query(table_class).all()
        session.close()
    except:
        session.close()
    return queries


def areAllQueryStringPresent(query_strings, target_sets):
    return all(query_string in query_strings for query_string in target_sets)


def isExist(table_name, search_params):
    session = Session()
    result = False
    try:
        result = session.query(table_name).filter_by(**search_params).first() is not None
        session.close()
    except:
        session.close()
    return result


def updateWarehouseQuantity(product_id, quantity_in_machine, new_quantity):
    session = Session()
    product_in_warehouse = session.query(Products).filter_by(id=product_id).first()
    print(product_in_warehouse.product_quantity, new_quantity, quantity_in_machine)
    product_in_warehouse.product_quantity = int(product_in_warehouse.product_quantity) - (
            int(new_quantity) - int(quantity_in_machine))
    print(product_in_warehouse.product_quantity, new_quantity, quantity_in_machine)
    session.commit()
    session.close()


def updateDatabaseRowByID(table_class, query_strings):
    session = Session()

    current_item = session.query(table_class).filter_by(id=query_strings["id"]).first()
    for query_string in query_strings.keys():
        setattr(current_item, query_string, query_strings[query_string])
        # case for updating machine_stocks table
        if type(current_item) is MachineStock and query_string == "quantity":
            print(current_item.machine_id, current_item.product_id, query_strings["quantity"])
            updateWarehouseQuantity(current_item.machine_id, current_item.product_id, query_strings["quantity"])
    session.commit()
    session.close()
