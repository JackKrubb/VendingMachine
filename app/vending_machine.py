from app.schema import *
from flask import Blueprint, request, jsonify, redirect, url_for, flash

"""
This file contains CRUD operation regarding vending_machine table
all endpoints are redirected back to /vendings/ which return JSON object of the data in the vending_machines table
"""

vending_machine = Blueprint('vending_machine', __name__)


# add new machine to vending machine table
@vending_machine.route("/add_vendings/", methods=["GET", "POST"])
def add_vending_machine():
    args = request.args
    # making sure that all query string needed are presented
    if args and all(k in args for k in ("location", "name", "code")):
        session = Session()
        # noinspection PyTypeChecker
        new_vend = Vending_machine(args["name"], args["code"], args["location"])
        try:
            session.add(new_vend)
            session.commit()
        except:
            session.close()
        session.close()
    return redirect(url_for("vending_machine.view_vending_machine"))


# view all vending machines in the table
@vending_machine.route("/vendings/", methods=["GET"])
def view_vending_machine():
    session = Session()
    queries = session.query(Vending_machine).all()
    session.close()
    if not queries:
        return '', 204  # return 204 NO CONTENT if the table is empty
    vendings = []
    for query in queries:
        vending = {'id': query.id, 'name': query.machine_name, 'machine_code': query.machine_code,
                   'location': query.machine_location, 'start_service_at': query.installed_at}
        vendings.append(vending)
    return jsonify(vendings)


# edit an instance of vending machine
@vending_machine.route("/edit_vendings/", methods=["GET", "POST"])
def edit_vending_machine():
    args = request.args
    # check if the target machine exist in the database
    if args and "id" in args:
        session = Session()
        # update everything according to presented query string
        old_vending_info = session.query(Vending_machine).filter_by(id=args["id"]).first()
        if "location" in args:
            old_vending_info.machine_location = args["location"]
        if "name" in args:
            old_vending_info.machine_name = args["name"]
        if "code" in args:
            old_vending_info.machine_code = args["code"]
        try:
            session.commit()
        except:
            session.close()
        session.close()
    return redirect(url_for("vending_machine.view_vending_machine"))


# delete a vending machine from the table
@vending_machine.route('/delete_vendings/', methods=["GET", "POST", "DELETE"])
def delete_vending_machine():
    args = request.args
    if args and "id" in args:
        session = Session()
        unwanted_vending_machine = session.query(Vending_machine).filter_by(id=args["id"]).first()
        try:
            session.delete(unwanted_vending_machine)
            session.commit()
        except:
            session.close()
        session.close()
    return redirect(url_for("vending_machine.view_vending_machine"))
