from flask import Blueprint, render_template, abort, flash, redirect, url_for, current_app
from app.forms import ToolSubmissionForm
from app.data_service import create_tool_submission, get_all_tool_submissions, get_tool_submission_by_id
from config import Config

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    try:
        tools = get_all_tool_submissions()
        return render_template('index.html', title='Home', tools=tools)
    except Exception as e:
        current_app.logger.error(f"Error fetching tools: {str(e)}")
        flash('An error occurred while fetching tools. Please try again later.', 'error')
        return render_template('index.html', title='Home', tools=[])

@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/tool/<int:tool_id>')
def tool_details(tool_id):
    try:
        tool = get_tool_submission_by_id(tool_id)
        if not tool:
            abort(404)
        return render_template('tool_details.html', title=tool['name'], tool=tool)
    except Exception as e:
        current_app.logger.error(f"Error fetching tool details: {str(e)}")
        flash('An error occurred while fetching tool details. Please try again later.', 'error')
        return redirect(url_for('main.index'))

@main.route('/submission', methods=['GET', 'POST'])
def submit_tool():
    form = ToolSubmissionForm()
    if form.validate_on_submit():
        try:
            new_tool = {
                'name': form.name.data,
                'description': form.description.data,
                'website': form.website.data,
                'category': form.category.data,
                'free_features': form.free_features.data,
                'paid_features': form.paid_features.data,
                'why_pay': form.why_pay.data
            }
            created_tool = create_tool_submission(new_tool)
            if created_tool:
                flash('Your tool submission has been received. Thank you!', 'success')
                return redirect(url_for('main.index'))
            else:
                flash('An error occurred while submitting your tool. Please try again.', 'error')
        except Exception as e:
            current_app.logger.error(f"Error submitting tool: {str(e)}")
            flash('An error occurred while submitting your tool. Please try again.', 'error')
    return render_template('submission.html', title='Submit Tool', form=form)