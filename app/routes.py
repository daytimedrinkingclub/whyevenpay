from flask import Blueprint, render_template, flash, redirect, url_for, jsonify, request
from app.forms import ToolSubmissionForm
from app.data_service import get_tools, get_tool_by_id, create_tool_submission, get_total_tools_count

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    tools = get_tools(offset=0, limit=10)
    total_count = get_total_tools_count()
    return render_template('index.html', title='Home', tools=tools, total_count=total_count)


@bp.route('/load_more_tools')
def load_more_tools():
    offset = int(request.args.get('offset', 0))
    limit = int(request.args.get('limit', 10))
    tools = get_tools(offset=offset, limit=limit)
    return jsonify(tools)

@bp.route('/about')
def about():
    return render_template('pages/about.html', title='About')

@bp.route('/tool/<int:tool_id>')
def tool_details(tool_id):
    tool = get_tool_by_id(tool_id)
    return render_template('pages/tool_details.html', title='Tool Details', tool=tool)

@bp.route('/submissions', methods=['GET', 'POST'])
def submit():
    form = ToolSubmissionForm()
    if form.validate_on_submit():
        submission_data = {
            'name': form.name.data,
            'description': form.description.data,
            'url': form.website.data,
            'category': form.category.data,
            'free_features': form.free_features.data,
            'paid_features': form.paid_features.data,
            'why_pay': form.why_pay.data
        }
        create_tool_submission(submission_data)
        flash('Your submission has been received!')
        return redirect(url_for('main.submissions'))
    return render_template('pages/submission.html', title='Submit a Tool', form=form)