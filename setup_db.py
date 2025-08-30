import sqlite3

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    vendor TEXT,
    price REAL,
    link TEXT
)
''')

products = [
    ("iPhone 14", "Amazon", 79999, "https://www.amazon.in/Apple-iPhone-14-256GB-Midnight/dp/B0BDJ6N5D6/ref=sr_1_1_sspa?crid=1MNTR0P4NVU6P&dib=eyJ2IjoiMSJ9.EishLESB7ljanJGMrIR_9hIsYDsx0faoc165csM2TnN8S_xG6IpNjegG3lWXZcvrkhKvaPGOIHKTLhr7j1yBKwa207MGVmItkm9nVhBbFvB9mNvyinCGEJ5iQHMrRcwPVTAUom-bxBPnXVyFKx_o-Eqjlf0aJcLR0Hp-luuL8rYDFw0umoeZWwMbV_lVlHgdgVBuyKfJtnBaQ3crTbqkUYomdA5SYliUJ_finQe1JZo.ujQSrrbH2Yr0w7tx7-nZ7dVFsmGZE0_OxfEMBbRo5TA&dib_tag=se&keywords=iPhone+14&qid=1756523410&sprefix=iphone+14%2Caps%2C252&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"),
    ("iPhone 14", "Flipkart", 78999, "https://www.flipkart.com/apple-iphone-14-midnight-256-gb/p/itmdb32e3c997112?pid=MOBGHWFH4H3MMRAA&lid=LSTMOBGHWFH4H3MMRAAQSJTKY&marketplace=FLIPKART&q=iphone+14&store=tyy%2F4io&srno=s_1_7&otracker=search&otracker1=search&fm=organic&iid=f646d980-a0e9-4906-9d9e-346488c9c5ec.MOBGHWFH4H3MMRAA.SEARCH&ppt=hp&ppn=homepage&ssid=3mmo62qlkw0000001756523462466&qH=860f3715b8db08cd"),
    ("iPhone 14", "Reliance Digital", 80500, "https://www.reliancedigital.in/product/apple-iphone-14-256-gb-midnight-l7ucg1?internal_source=search_collection"),
    ("Samsung Galaxy S23", "Amazon", 74999, "https://www.amazon.in/Samsung-Galaxy-Ultra-Phantom-Storage/dp/B0BT9FDZ8N/ref=sr_1_5?crid=1MT644RZ5S045&dib=eyJ2IjoiMSJ9.NOaWhI2-0UiCXvgeAuLpJG_OymiwYiGmxVmhVwTzsQ4pTNQgu7eVd3m_7tLJ1UqAczeUr3kTuz4WTWUQ4SIYwc9VbUyEWRIBExFM2ilMQRMOjYyDSDvteK8fTpWSjrOZwfQwZvRjw1TZRb7PSbyiA33caB4vdRusKMLkPUV4Ljj1EUysTT7-hTWtqGhnfzSjNVgEdwj5xQaGMIdrkm0yNPNc2Pfc7824TfwDudfd1GE.dkf8DL9we7nSZcO7_tozE_8k7OoScLldesONh9IgQ3c&dib_tag=se&keywords=galaxy%2Bs23&qid=1756524405&sprefix=galaxys23%2Caps%2C202&sr=8-5&th=1"),
    ("Samsung Galaxy S23", "Croma", 73999, "https://www.croma.com/samsung-galaxy-s23-ultra-5g-12gb-ram-256gb-phantom-black-/p/275155")
]

cursor.executemany("INSERT INTO products (name, vendor, price, link) VALUES (?, ?, ?, ?)", products)
conn.commit()
conn.close()
print("Database setup complete.")
