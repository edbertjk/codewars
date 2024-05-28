def domain_name(url):
    replaces = url.replace("http://", "").replace("https://", "").replace("www.", "")
    domain = replaces.split(".")
    return domain[0]

print(domain_name("https://dwada.com"))