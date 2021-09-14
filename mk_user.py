from app.routes import db, User



def create_my_user(first_name, last_name, hobbies):
    db.session.add(
        User(
            first_name=first_name,
            last_name=last_name,
            hobbies=hobbies
        )
    )
    db.session.commit()


if __name__ == "__main__":
    create_my_user("Nathan", "Vik", "Vidya")
    create_my_user("John", "Doe", "Surfing")
    create_my_user("James", "Doe", "Baking")

    # Example of how to select all users:
    users = User.query.all()
    print(users)

    # example of how to select a user by their ID
    user = User.query.filter_by(id=2).first()
    print(user)


