def getEmailParts(email):
    monkeyIndeks = email.find("@")
    if monkeyIndeks == -1: return None

    dotIndeks = email.rfind(".")
    if dotIndeks == -1: return None

    user = email[0:monkeyIndeks]
    domainName = email[monkeyIndeks+1: dotIndeks]
    domainExt = email[dotIndeks+1:len(email)]

    return {
        "user": user,
        "domainName" : domainName,
        "domainExt" : domainExt
    }


print(getEmailParts("ola@domena.com"))