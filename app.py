from flask import Flask, render_template, request
import os
from models.user import User
from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint

app = Flask(__name__)
app.secret_key = 'shaam'
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)


@app.route('/')
def home():
    return render_template('home.html')


app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")
app.register_blueprint(user_blueprint, url_prefix="/users")

# user = User('bob', 'pwd')

# print(user)

if __name__ == "__main__":
    app.run(debug=True)

'''
alert = Alert("86f01911ed0248e19e183c930043dd7a", 1000)
alert.save_to_mongo()


url = "https://www.johnlewis.com/apple-iphone-12-ios-6-1-inch-5g-sim-free-128gb/black/p5178119"
tag_name="p"
query = {"class": "price price--large"}

ipad = Item(url, tag_name, query)
ipad.save_to_mongo()

items_loaded =Item.all()
print(items_loaded)
print(items_loaded[0].load_price())
#print(item.load_price())
'''
