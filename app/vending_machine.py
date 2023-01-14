from app.schema import *
from flask import Blueprint, request, jsonify, redirect, url_for, flash

vending_machine = Blueprint('vending_machine', __name__)


@vending_machine.route("/add_vendings/", methods=["GET", "POST"])
def add_vending_machine():
    args = request.args
    if args:
        session = Session()
        new_vend = Vending_machine(args["location"])
        session.add(new_vend)
        session.commit()
        session.close()

    return redirect(url_for("vending_machine.view_vending_machine"))


@vending_machine.route("/vendings/", methods=["GET"])
def view_vending_machine():
    session = Session()
    queries = session.query(Vending_machine).all()
    session.close()
    if not queries:
        return '', 204  # return 204 NO CONTENT if the table is empty
    vendings = []
    for query in queries:
        vending = {'id': query.id, 'location': query.location}
        vendings.append(vending)

    return jsonify(vendings)
