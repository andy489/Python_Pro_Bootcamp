import csv
from datetime import datetime

from extensions import db
from models import User, BlogPost, Comment

def seed_database():
    with open('data/users.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user = User(
                id=row['id'],
                email=row['email'],
                password=row['password'],
                name=row['name'],
            )
            db.session.add(user)

    with open('data/blog_posts.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            post = BlogPost(
                id=row['id'],
                author_id=row['author_id'],
                title=row['title'],
                subtitle=row['subtitle'],
                date=row['date'],
                body=row['body'],
                img_url=row['img_url']
            )
            db.session.add(post)

    with open('data/comments.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            comment = Comment(
                id=row['id'],
                author_id=row['author_id'],
                post_id=row['post_id'],
                text=row['text'],
                posted_time=datetime.strptime(row['posted_time'], '%Y-%m-%d %H:%M:%S.%f'),
            )
            db.session.add(comment)

    db.session.commit()
    print("Database seeded successfully!")
