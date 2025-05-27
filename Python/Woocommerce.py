from woocommerce import API

wpapi = API(url="https://organizeroad.s4-tastewp.com/", consumer_key="ck_a4d5fce134da7203e81ad66db97316c363916a1c", consumer_secret="cs_852f5a6831166ef2de8e58e0b448eea98f7b525f", wpapi=True)

data = {
    "code": "10off",
    "discount_type": "percent",
    "amount": "10",
    "individual_use": True,
    "exclude_sale_items": True,
    "minimum_amount": "100.00",
    
    "usage_limit": 1
}
response = wpapi.post("coupons", data).json()
for x in response:
    print(x, response.get(x))

