import random
from faker import Faker
from sqlalchemy import create_engine, text
from app.core.config import get_app_settings
from app.models.domain.users import UserInDB
from app.models.domain.items import Item
from app.models.domain.comments import Comment


# Initialize Faker and create lists to hold the objects
fake = Faker()
users = []
items = []
comments = []

# Generate fake data for 100 users, 100 items and 100 comments
for i in range(100):
    username = fake.user_name()
    email = fake.email()
    password = fake.password()
    bio = fake.paragraph()
    image = fake.image_url()
    users.append(UserInDB(username=username, email=email, bio=bio, image=image))

for i in range(100):
    slug = fake.slug()
    title = fake.sentence()
    description = fake.paragraph()
    tags = [fake.word() for _ in range(3)]
    username = fake.user_name()
    email = fake.email()
    seller = users[i]
    favorited = fake.boolean()
    favorites_count = random.randint(0,100)
    image = fake.image_url()
    body = fake.text()
    items.append(Item(slug=slug, title=title, description=description, tags=tags, seller=seller, favorited=favorited, favorites_count=favorites_count, image=image, body=body))

for i in range(100):
    body = fake.text()
    seller = users[i]
    comments.append(Comment(body=body, seller=seller))

# Insert users and items into the database
# ----------------------------------------
SETTINGS = get_app_settings()
DATABASE_URL = SETTINGS.database_url

engine = create_engine(DATABASE_URL)
with engine.connect() as connection:
    for user in users:
        connection.execute(
            text(f"""
            INSERT INTO users (username, salt, email, bio, image) 
            VALUES ('{user.username}', '', '{user.email}', '{user.bio}', '{user.image}')
            """)
        )
        HASHED_PASSWORD='9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
        connection.execute(
            text(f"UPDATE users SET salt = 'test', hashed_password = '{HASHED_PASSWORD}'")
        )

    for item in items:
        connection.execute(
            text(f"""
            INSERT INTO items (slug, title, description, seller_id, image, body) 
            VALUES ('{item.slug}', '{item.title}', '{item.description}', 1, '{item.image}', '{item.body}')
            """)
        )

    for comment in comments:
        connection.execute(
            text(f"""
            INSERT INTO comments (body, seller_id, item_id) 
            VALUES ('{comment.body}', {i}, {i})
            """)
        )