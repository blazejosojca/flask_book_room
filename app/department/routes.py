from datetime import datetime
from flask import url_for, render_template, flash, request
from flask_login import current_user, login_required

from werkzeug.utils import redirect

from app import db
from app.models import Department
from app.department import bp
from app.department.forms import DepartmentForm


@bp.route('/department/new', methods=['POST', 'GET'])
@login_required
def create_department():
    """
    Add department to db.
    """
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(
            department_name=form.name.data,
            description=form.data.data
        )
        db.session.add(department)
        db.session.commit()

        flash('New department was added!')
        return redirect(url_for('main.home'))
    return render_template('department/create_department.html',
                           title='Add new department',
                           form=form,
                           legend='New department'
                           )


@bp.route('/department/<int:department_id>', methods=['GET', 'POST'])
@login_required
def department_details(department_id):
    department = Department.query.get(department_id)
    return render_template('department/department.html',
                           title='Department details',
                           department=department,
                           legend='Department')


@bp.route('/department/list', methods=['GET', 'POST'])
def department_list():
    departments = Department.query.all()
    return render_template('department/list_departments.html',
                           departments=departments,
                           title='Departments list',
                           legend='List of departments'
                           )


@bp.route('/department/edit/<int:department_id>', methods=['GET', 'POST'])
def edit_department(department_id):
    department = Department.query.get_or_404(department_id)
    form = DepartmentForm()
    if form.validate_on_submit():
        department.department_name = form.department_name.data
        department.description = form.description.data
        db.session.commit()
    elif request.method == 'GET':
        department.department_name = form.department_name
        department.description = form.description
    return render_template('department/edit_department.html',
                           title='Edit department info',
                           form=form,
                           legend='Edit department')


@bp.route('/booking/list/<int:user_id>', methods=['GET', 'POST'])
def delete_department():
    pass


@bp.context_processor
def inject_now():
    return {'now': datetime.utcnow()}
