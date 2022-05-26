from shortener_app.database import SessionLocal

db = SessionLocal()
from shortener_app.models import URL

print(vars(db.query(URL.all())))