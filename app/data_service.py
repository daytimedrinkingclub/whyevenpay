from flask import current_app

def get_tools(offset=0, limit=10):
    response = current_app.supabase.table('Tool').select('*, ToolCategory(name, meta)').eq('is_deleted', False).range(offset, offset + limit - 1).execute()
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
    try:
        response = current_app.supabase.table('ToolSubmission').insert(submission_data).execute()
        print(f"Supabase response: {response}")  # Add this line for debugging
        if response.data:
            return response.data[0]
        else:
            print(f"No data returned from Supabase: {response}")  # Add this line for debugging
            return None
    except Exception as e:
        print(f"Error inserting data into Supabase: {str(e)}")  # Add this line for debugging
        return None

def get_categories():
    response = current_app.supabase.table('ToolCategory').select('*').execute()
    return response.data

def update_tool(tool_id, updated_data):
    try:
        response = current_app.supabase.table('Tool').update(updated_data).eq('id', tool_id).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error updating tool in Supabase: {str(e)}")
        return None

def delete_tool(tool_id):
    try:
        response = current_app.supabase.table('Tool').update({'is_deleted': True}).eq('id', tool_id).execute()
        return True if response.data else False
    except Exception as e:
        print(f"Error soft deleting tool in Supabase: {str(e)}")
        return False
    
def restore_tool(tool_id):
    try:
        response = current_app.supabase.table('Tool').update({'is_deleted': False}).eq('id', tool_id).execute()
        return True if response.data else False
    except Exception as e:
        print(f"Error restoring tool in Supabase: {str(e)}")
        return False

def get_tool_by_slug(slug):
    try:
        response = current_app.supabase.table('Tool').select('*, ToolCategory(name, meta)').eq('slug', slug).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error fetching tool by slug from Supabase: {str(e)}")
        return None
