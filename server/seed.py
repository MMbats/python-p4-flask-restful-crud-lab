from app import app
from models import db, Plant

with app.app_context():
    db.drop_all()
    db.create_all()

    aloe = Plant(
        name='Aloe Vera',
        image='https://example.com/aloe.jpg',
        price=12.99,
        is_in_stock=True
    )

    basil = Plant(
        name='Basil',
        image='https://example.com/basil.jpg',
        price=5.99,
        is_in_stock=True
    )

    cactus = Plant(
        name='Cactus',
        image='https://example.com/cactus.jpg',
        price=15.99,
        is_in_stock=False
    )

    db.session.add_all([aloe, basil, cactus])
    db.session.commit()