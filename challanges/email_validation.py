

def validateEmail(email):
    monkeyIndes = email.find("@")
    if monkeyIndes < 0: return False

    dotIndeks = email.find(".")
    if dotIndeks == -1: return False
    if dotIndeks < monkeyIndes: return False

    return True

email1 = "asia@example.com"
email2 = "karol@domena"
email3 = "user.com"

print(validateEmail(email1))
print(validateEmail(email2))
print(validateEmail(email3))


def validateEmail2(email):
    monkeyIndes = email.find("@")
    if monkeyIndes < 0: return False

    dotIndeks = email.rfind(".")
    if dotIndeks == -1: return False
    if dotIndeks < monkeyIndes: return False

    return True


email1 = "asia@example.com"
email2 = "karol@domena"
email3 = "user.com"
email4 = "kasai.kowalska@gmail.com"


print(validateEmail2(email1))
print(validateEmail2(email2))
print(validateEmail2(email3))
print(validateEmail2(email4))