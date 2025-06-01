def login(username, password, remember=False):
    """Enhanced login with validation"""
    if not username or not password:
        return {'status': 'error', 'message': 'Missing credentials'}
    
    # Simulate validation
    if len(password) < 8:
        return {'status': 'error', 'message': 'Password too short'}
    
    return {
        'status': 'success',
        'message': 'Login successful',
        'remember_me': remember
    }
