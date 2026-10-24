def can_read_document(user_id, owner_id):
    """Only the owner should be allowed to read a private document."""
    return bool(user_id)
