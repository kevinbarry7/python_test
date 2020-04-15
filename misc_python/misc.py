def iso_8601(s):
    """
    Returns True if s is a string in ISO 8601 format, False otherwise
    
    Parameter time: The string to check
    Precondition: s is a string of length 8
    """
    # This is a hint to get you started
    # Create variable to check if the first two characters are digits
    check1 = introcs.isdigit(s[:2])
    # Create variable to check if third character is a colon
    check2 = s[2] == ':'
    
    # FINISH THIS FUNCTION
    
    # Return True if all checks pass
    #return check1 and check2 # AND...