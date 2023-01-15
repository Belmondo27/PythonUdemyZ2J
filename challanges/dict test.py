config = {
    "website" : "examplae.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dbPassowrd" : "12345" 
}
print(len(config))
print(config["dbType"])

for key, value in config.items():
    print("Klucz w config: ", key, " z wartością: ", value)