def password_check(password: str) -> bool:
    if len(password) < 10:
        return False
    
    k_zag = False
    k_stroch = False
    k_num = False 

    for char in password:
        if char.isupper():
            k_zag = True
        elif char.islower():
            k_stroch = True
        elif char.isdigit():
            k_num = True

    return k_stroch and k_zag and k_num



assert password_check(".........................") == False
assert password_check("Ab1............") == True