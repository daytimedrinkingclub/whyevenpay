from flask import current_app

def get_tools(offset=0, limit=10):
    response = current_app.supabase.table('Tool').select('*, ToolCategory(name, meta)').range(offset, offset + limit - 1).execute()
    return response.data

def get_total_tools_count():
    response = current_app.supabase.table('Tool').select('count', count='exact').execute()
    return response.count

def get_all_tools():
    response = current_app.supabase.table('Tool').select('*, ToolCategory(name, meta)').execute()
    return response.data

def get_tool_by_id(tool_id):
    response = current_app.supabase.table('Tool').select('*, ToolCategory(name, meta)').eq('id', tool_id).execute()
    return response.data[0] if response.data else None

def create_tool_submission(submission_data):
    """
    Create a new ToolSubmission from submission data and save it to the database.
    """
    new_submission = {
        'name': submission_data['name'],
        'description': submission_data['description'],
        'website': submission_data['website'],
        'category': submission_data['category'],
        'free_features': submission_data['free_features'],
        'paid_features': submission_data['paid_features'],
        'why_pay': submission_data['why_pay'],
        'why_not_pay': submission_data['why_not_pay'],
        'when_to_pay': submission_data['when_to_pay'],
        'submitted_by': submission_data['submitted_by'],
        'is_published': submission_data['is_published'],
        'logo_public_url': submission_data['logo_public_url']
    }
    response = current_app.supabase.table('ToolSubmission').insert(new_submission).execute()
    return response.data[0] if response.data else None

def get_categories():
    response = current_app.supabase.table('ToolCategory').select('*').execute()
    return response.data
