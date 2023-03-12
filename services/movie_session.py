from django.db.models import QuerySet
from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        cinema_hall_id: int,
        movie_id: int

) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    all_sessions = MovieSession.objects.all()

    if session_date:
        all_sessions = all_sessions.filter(show_time__date=session_date)

    return all_sessions


def get_movie_session_by_id(movie_sessions_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_sessions_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None,

) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie_session.movie_id = movie_id

    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    return movie_session.save()


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=session_id).delete()
