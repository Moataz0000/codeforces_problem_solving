s_url = input().strip()

query = s_url.split("?", 1)[1]
pairs = query.split("&")

for pair in pairs:
    key, value = pair.split("=")
    print(f"{key}: {value}")
