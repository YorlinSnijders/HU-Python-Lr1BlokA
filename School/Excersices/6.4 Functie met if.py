oudwachtwoord = input("Oud wachtwoord: ")
nieuwwachtwoord = input("Nieuw wachtwoord: ")


def new_password(oudwachtwoord, nieuwwachtwoord):
    if nieuwwachtwoord != oudwachtwoord and len(nieuwwachtwoord) >=6:
        return  True
    return False

print(new_password(oudwachtwoord,nieuwwachtwoord))
