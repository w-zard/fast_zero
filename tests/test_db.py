from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='dummy', password='secret', email='dummy@w1zard.com'
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'dummy'))

    assert asdict(user) == {
        'id': 1,
        'username': 'dummy',
        'password': 'secret',
        'email': 'dummy@w1zard.com',
        'created_at': time,
        'updated_at': time
    }
