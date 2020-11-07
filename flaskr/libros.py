import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('libros', __name__, url_prefix='/libros')



@bp.route('/insertar', methods=('LISTAR', 'INSERTAR'))
def register():
    if request.method == 'INSERTAR':
        nombre = request.form['Nombre']
        editorial = request.form['Editorial']
        db = get_db()
        error = None

        if not nombre:
            error = 'Se requiere el nombre'
        elif not editorial:
            error = 'Se requiere la editorial'
        elif db.execute(
            'SELECT id FROM libro WHERE nombre = ?', (nombre,)
        ).fetchone() is not None:
            error = 'El libro "{}" ya existe en la bilbioteca'.format(nombre)

        if error is None:
            db.execute(
                'INSERT INTO libro (nombre, editorial) VALUES (?,?)',
                (nombre, editorial)
            )
            db.commit()
            return redirect(url_for('libros.busqueda'))

        flash(error)

    return render_template('libros/insertar.html')



@bp.route('/busqueda', methods=('GET', 'POST'))
def busqueda():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM libro WHERE nombre = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'No se encuentran resultados'

        if error is None:
            db.execute(
                'SELECT id FROM libro WHERE nombre = ?', (nombre,)
            ).fetchone()
            

        flash(error)

    return render_template('libros/busqueda.html')