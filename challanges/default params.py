def function(email, country = "Polska", company = "example Ltd"):
    return {
        "email " : email,
        "country ": country,
        "company " : company
    }

print(function("ola@example.com"))
print(function("kasia@example.com", "UK"))
print(function("adam@example.com", "DE", "Test Ltd"))