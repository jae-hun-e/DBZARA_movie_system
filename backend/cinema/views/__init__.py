from .list import (
    CinemaListView
)

from .api import (
    CinemaListAPIView, CinemaDetailAPIView, ScheduleCinemaAPIView, ScheduleMovieAPIView,
    ScheduleAPIView
)

cinemas = CinemaListView.as_view()

cinema_api_list_view = CinemaListAPIView.as_view()
cinema_api_detail_view = CinemaDetailAPIView.as_view()
schedule_cinema_api_view = ScheduleCinemaAPIView.as_view()
schedule_movie_api_view = ScheduleMovieAPIView.as_view()
schedule_api_view = ScheduleAPIView.as_view()

