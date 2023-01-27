from app.database.schema import *

'''
this file contains utilities functions for CRUD operation in the database
'''

no_content_204 = '', 204
bad_request_400 = '', 400

'''
this function create a list of dictionaries from a list of objects, queried from the database
objlist - list of objects which was queried from the database
return - a list of dictionaries in which each dictionary is create using obj_to_dict method
'''


def dict_helper(objlist):
    result = [item.obj_to_dict() for item in objlist]
    return result


def add_obj_to_db(obj):
    if obj is not None:
        session = Session()
        try:
            session.add(obj)
            session.commit()
            session.close()
        except:
            session.close()


def select_obj(table_name, search_params):
    session = Session()
    obj = None
    try:
        obj = session.query(table_name).filter_by(**search_params).first()
        session.close()
    except:
        session.close()
    return obj


def select_obj_list(table_name, search_params):
    session = Session()
    obj_list = None
    try:
        obj_list = session.query(table_name).filter_by(**search_params).all()
        session.close()
    except:
        session.close()
    return obj_list


def delete_obj_from_db(obj):
    if obj is not None:
        session = Session()
        try:
            session.delete(obj)
            session.commit()
            session.close()
        except:
            session.close()


def get_all_from_table(table_class):
    session = Session()
    queries = None
    try:
        queries = session.query(table_class).all()
        session.close()
    except:
        session.close()
    return queries


def are_all_query_string_present(query_strings, target_sets):
    return all(query_string in query_strings for query_string in target_sets)


def is_exist(table_name, search_params):
    session = Session()
    result = False
    try:
        result = session.query(table_name).filter_by(**search_params).first() is not None
        session.close()
    except:
        session.close()
    return result


'''
this function updates the product table according to the changes of a product quantity changes in the machine_stock table
product_id - the primary key of the product we wish to update its quantity
quantity_in_machine - the quantity of the product in a vending machine
new_quantity - the new quantity of the product in the machine
return quantity_validation which tells if the update is success or not if success the return 
        the number of that product else return none
'''


def update_warehouse_quantity(product_id, quantity_in_machine, new_quantity):
    session = Session()
    quantity_validation = None
    try:
        product_in_warehouse = session.query(Products).filter_by(id=product_id).first()
        product_in_warehouse.product_quantity = int(product_in_warehouse.product_quantity) - (
                int(new_quantity) - int(quantity_in_machine))
        if product_in_warehouse.product_quantity >= 0 and int(new_quantity) >= 0 and int(quantity_in_machine) >= 0:
            quantity_validation = product_in_warehouse.product_quantity
            session.commit()
        session.close()
    except:
        session.close()
    return quantity_validation


def update_database_row_by_id(table_class, query_strings):
    session = Session()
    current_item = session.query(table_class).filter_by(id=query_strings["id"]).first()
    if current_item is None:
        return
    for query_string in query_strings.keys():
        setattr(current_item, query_string, query_strings[query_string])
        # case for updating machine_stocks table
        # if type(current_item) is MachineStock and query_string == "quantity":
        # update_warehouse_quantity(current_item.machine_id, current_item.product_id, query_strings["quantity"])
    session.commit()
    session.close()
