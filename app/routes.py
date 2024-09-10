from flask import Blueprint, render_template, flash, redirect, url_for, jsonify, request
from app.forms import ToolSubmissionForm
from app.data_service import get_tools, get_tool_by_id, create_tool_submission, get_total_tools_count

bp = Blueprint('main', __name__)

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

@bp.route('/tool/<int:tool_id>')
def tool_details(tool_id):
    tool = get_tool_by_id(tool_id)
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