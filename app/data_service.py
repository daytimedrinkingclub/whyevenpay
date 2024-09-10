from flask import current_app

def get_all_tools():
    """
    Retrieve all Tool entries from the database.
    """
    response = current_app.supabase.table('Tool').select('*').execute()
    return response.data

def get_tool_by_id(tool_id):
    """
    Retrieve a specific Tool by its ID.
    """
    response = current_app.supabase.table('Tool').select('*').eq('id', tool_id).execute()
    return response.data[0] if response.data else None

def create_tool_submission(submission_data):
    """
    Create a new Tool from submission data and save it to the database.
    """
    new_tool = {
        'name': submission_data['name'],
        'link': submission_data['url'],
        'description': submission_data['description'],
        'why_pay': submission_data.get('why_pay', ''),
        'when_pay': submission_data.get('when_to_pay', ''),
        'why_not_pay': submission_data.get('why_not_pay', '')
    }
    response = current_app.supabase.table('Tool').insert(new_tool).execute()
    return response.data[0] if response.data else None

def update_tool_submission(submission_id, form_data):
    """
    Update an existing Tool with new form data.
    """
    updated_data = {
        'name': form_data['name'],
        'link': form_data['url'],
        'description': form_data['description'],
        'why_pay': form_data.get('why_pay', ''),
        'when_pay': form_data.get('when_to_pay', ''),
        'why_not_pay': form_data.get('why_not_pay', ''),
        'updated_at': 'now()'
    }
    response = current_app.supabase.table('Tool').update(updated_data).eq('id', submission_id).execute()
    return response.data[0] if response.data else None

def delete_tool_submission(submission_id):
    """
    Delete a Tool from the database.
    """
    response = current_app.supabase.table('Tool').delete().eq('id', submission_id).execute()
    return response.data[0] if response.data else None
