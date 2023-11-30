def validate_search_parameter(parameter):
    if isinstance(parameter, str):
        if len(parameter) > 0:
            return True
    return False
