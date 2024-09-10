from flask import current_app
from config import Config

def create_tool_submission(form_data):
    """
    Create a new Tool from form data and save it to the database.
    """
    supabase = Config.supabase
    new_tool = {
        'name': form_data['name'],
        'link': form_data['website'],
        'description': form_data['description'],
        'why_pay': form_data['why_pay'],
        'when_pay': form_data.get('when_to_pay', ''),
        'why_not_pay': form_data.get('why_not_pay', '')
    }
    response = supabase.table('Tool').insert(new_tool).execute()
    return response.data[0] if response.data else None

def get_all_tool_submissions():
    """
    Retrieve all Tool entries from the database.
    """
    supabase = Config.supabase
    response = supabase.table('Tool').select('*').execute()
    return response.data

def get_tool_submission_by_id(submission_id):
    """
    Retrieve a specific Tool by its ID.
    """
    supabase = Config.supabase
    response = supabase.table('Tool').select('*').eq('id', submission_id).execute()
    return response.data[0] if response.data else None

def update_tool_submission(submission_id, form_data):
    """
    Update an existing Tool with new form data.
    """
    supabase = Config.supabase
    updated_data = {
        'name': form_data['name'],
        'link': form_data['website'],
        'description': form_data['description'],
        'why_pay': form_data['why_pay'],
        'when_pay': form_data.get('when_to_pay', ''),
        'why_not_pay': form_data.get('why_not_pay', ''),
        'updated_at': 'now()'
    }
    response = supabase.table('Tool').update(updated_data).eq('id', submission_id).execute()
    return response.data[0] if response.data else None

def delete_tool_submission(submission_id):
    """
    Delete a Tool from the database.
    """
    supabase = Config.supabase
    response = supabase.table('Tool').delete().eq('id', submission_id).execute()
    return response.data[0] if response.data else None
