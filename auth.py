def check_role(user, allowed_roles):
    if user.get("role") not in allowed_roles:
        return False
    return True
