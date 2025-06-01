def login(is_admin=False):
    """Dashboard-enabled login"""
    if is_admin:
        return {
            'status': 'success',
            'message': 'Admin login successful',
            'dashboard': 'admin_dashboard',
            'stats': get_user_statistics()
        }
    return {
        'status': 'success',
        'message': 'User login successful',
        'dashboard': 'user_dashboard'
    }

def get_user_statistics():
    """Get user activity statistics"""
    return {
        'active_users': 100,
        'total_logins': 500,
        'avg_session': '30 minutes'
    }
