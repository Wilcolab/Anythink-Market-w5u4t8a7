#import psycopg2
import random
from alembic import op
from faker import Faker
from app.models.domain.users import User
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
    users.append(User(username, email, bio, image))

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
    items.append(Item(slug, title, description, tags, seller, favorited, favorites_count, image, body))

for i in range(100):
    body = fake.text()
    seller = users[i]
    comments.append(Comment(body, seller))

# Insert users and items into the database
for user in users:
    op.execute(
        "INSERT INTO users (username, email, password, bio, image) VALUES (%s, %s, %s, %s, %s)",
        (user.username, user.email, user.password, user.bio, user.image)
    )

for item in items:
    op.execute(
        "INSERT INTO items (slug, title, description, tags, seller, favorited, favorites_count, image, body) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (item.slug, item.title, item.description, item.tags, item.seller.username, item.favorited, item.favorites_count, item.image, item.body)
    )

for comment in comments:
    op.execute(
        "INSERT INTO comments (body, seller) VALUES (%s, %s)",
        (comment.body. comment.seller)
    )