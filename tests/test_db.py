from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='dummy',
        password='s3cret!',
        email='dummy@user.com'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'dummy'))

    assert user.username == 'dummy'
