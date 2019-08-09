from datetime import datetime
from flask import url_for, render_template, flash
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
    Add department to db
    :return:
    """
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(
            department_name = form.name.data,
            description = form.data.data
        )
        db.session.add(department)
        db.session.commit()

        flash('New department was added!')
        return redirect(url_for('main.home'))
    return render_template('department/create_department.html',
                           title='create_department',
                           form=form,
                           legend='New department'
                           )

@bp.route('/booking/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def view_department(booking_id):
    
    department = Department.query.get(booking_id)

    return render_template('booking/booking.html', booking=booking)



@bp.route('/booking/delete/<int:booking_id>', methods=['GET', 'POST'])
def department_list():
    pass


@bp.route('/booking/list/<int:room_id>', methods=['GET', 'POST'])
def edit_department():
    pass


@bp.route('/booking/list/<int:user_id>', methods=['GET', 'POST'])
def delete_department():
    pass


@bp.context_processor
def inject_now():
    return {'now': datetime.utcnow()}
