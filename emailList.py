# returns a list of email from dictionary


def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append("{}@{}".format(user, domain))
    return emails


print(email_list({"gmail.com": ["clark.kent", "diana.prince"], "yahoo.com": ["jeff.anderson","morgan.jake"]}))