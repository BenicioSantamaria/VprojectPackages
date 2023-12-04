def PassChecker(Password):
    Pass = input("Input the password: ") 
    if Pass == Password:
        return True
    else:
        if Pass != Password:
            return False
