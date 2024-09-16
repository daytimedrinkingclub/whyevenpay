from flask import Blueprint, render_template, flash, redirect, url_for, jsonify, request, session
from app.forms import ToolSubmissionForm, AdminLoginForm
from app.data_service import get_tools, get_tool_by_slug, create_tool_submission, get_total_tools_count, get_all_tools, update_tool, delete_tool, restore_tool
import os
from functools import wraps

bp = Blueprint('main', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_authenticated'):
            return redirect(url_for('main.admin_login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
@bp.route('/index')
def index():
    tools = get_tools(offset=0, limit=30)
    total_count = get_total_tools_count()
    return render_template('index.html', title='Home', tools=tools, total_count=total_count)


@bp.route('/load_more_tools')
def load_more_tools():
    offset = int(request.args.get('offset', 0))
    limit = int(request.args.get('limit', 30))
    tools = get_tools(offset=offset, limit=limit)
    return jsonify(tools)

@bp.route('/about')
def about():
    return render_template('pages/about.html', title='About')

@bp.route('/tool/<string:tool_slug>')
def tool_details(tool_slug):
    tool = get_tool_by_slug(tool_slug)
    if not tool:
        flash('Tool not found', 'error')
        return redirect(url_for('main.index'))
    return render_template('pages/tool_details.html', title='Tool Details', tool=tool)

@bp.route('/submit-tool', methods=['GET', 'POST'])
def submit():
    form = ToolSubmissionForm()
    if form.validate_on_submit():
        try:
            submission_data = {
                'name': form.name.data,
                'description': form.description.data,
                'website': form.website.data,
                'category': form.category.data,
                'free_features': form.free_features.data,
                'paid_features': form.paid_features.data,
                'why_pay': form.why_pay.data,
                'why_not_pay': form.why_not_pay.data,
                'when_to_pay': form.when_to_pay.data,
                'submitted_by': form.submitted_by.data,
                'logo_public_url': form.logo_public_url.data
            }
            created_tool = create_tool_submission(submission_data)
            if created_tool:
                flash('Your submission has been received and is pending review!', 'success')
                return redirect(url_for('main.index'))
            else:
                flash('An error occurred while submitting your tool. Please try again.', 'error')
        except Exception as e:
            flash(f'An error occurred while submitting your tool: {str(e)}', 'error')
    
    return render_template('pages/submission.html', title='Submit Tool for Free - Why Even Pay?', form=form)

@bp.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        if form.password.data == os.environ.get('ADMIN_PASSWORD'):
            session['admin_authenticated'] = True
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.admin'))
        else:
            flash('Invalid password', 'error')
    return render_template('admin_login.html', form=form)

@bp.route('/admin')
@admin_required
def admin():
    tools = get_all_tools()
    return render_template('admin.html', title='Admin Dashboard', tools=tools)

@bp.route('/admin/edit/<string:tool_slug>', methods=['GET', 'POST'])
@admin_required
def admin_edit_tool(tool_slug):
    tool = get_tool_by_slug(tool_slug)
    if not tool:
        flash('Tool not found', 'error')
        return redirect(url_for('main.admin'))
    
    form = ToolSubmissionForm(obj=tool)
    if form.validate_on_submit():
        updated_data = {
            'name': form.name.data,
            'description': form.description.data,
            'website': form.website.data,
            'category': form.category.data,
            'free_features': form.free_features.data,
            'paid_features': form.paid_features.data,
            'why_pay': form.why_pay.data,
            'why_not_pay': form.why_not_pay.data,
            'when_to_pay': form.when_to_pay.data,
            'submitted_by': form.submitted_by.data,
            'logo_public_url': form.logo_public_url.data
        }
        updated_tool = update_tool(tool.id, updated_data)
        if updated_tool:
            flash('Tool updated successfully', 'success')
            return redirect(url_for('main.admin'))
        else:
            flash('An error occurred while updating the tool', 'error')
    
    return render_template('pages/edit_tool.html', title='Edit Tool', form=form, tool=tool)

@bp.route('/admin/delete/<tool_name>', methods=['POST'])
@admin_required
def admin_delete_tool(tool_name):
    tool = get_tool_by_slug(tool_name)
    print(f"Attempting to delete tool: {tool}")
    if not tool:
        return jsonify({'success': False, 'message': 'Tool not found'}), 404
    
    # Assuming 'tool' is a dictionary with an 'id' key
    success = delete_tool(tool['id'])
    
    if success:
        return jsonify({'success': True, 'message': 'Tool deleted successfully'})
    else:
        return jsonify({'success': False, 'message': 'Error deleting tool'}), 500
    
@bp.route('/admin/restore/<tool_slug>', methods=['POST'])
@admin_required
def admin_restore_tool(tool_slug):
    tool = get_tool_by_slug(tool_slug)
    if not tool:
        return jsonify({'success': False, 'message': 'Tool not found'}), 404

    # Update is_deleted to False
    success = restore_tool(tool['id'])

    return jsonify({'success': success})
