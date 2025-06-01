def login(username=None, password=None, remember=False, is_admin=False):
    """Enhanced login with dashboard and validation"""
    # Validate credentials
    if not username or not password:
        return {'status': 'error', 'message': 'Missing credentials'}
    
    if len(password) < 8:
        return {'status': 'error', 'message': 'Password too short'}
    
    # Handle admin login
    if is_admin:
        return {
            'status': 'success',
            'message': 'Admin login successful',
            'remember_me': remember,
            'dashboard': 'admin_dashboard',
            'stats': get_user_statistics()
        }
    
    # Regular user login
    return {
        'status': 'success',
        'message': 'Login successful',
        'remember_me': remember,
        'dashboard': 'user_dashboard'
    }

def get_user_statistics():
    """Get user activity statistics"""
    return {
        'active_users': 100,
        'total_logins': 500,
        'avg_session': '30 minutes'
    }
