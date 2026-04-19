from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, test_password):
    new_user = User(
        username='dummy',
        password=test_password,
        email='dummy@user.com'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'dummy'))

    assert user.username == 'dummy'
