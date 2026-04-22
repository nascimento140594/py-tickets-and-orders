def clean(self) -> None:
    rows = self.movie_session.cinema_hall.rows
    seats = self.movie_session.cinema_hall.seats_in_row

    if not 1 <= self.row <= rows:
        raise ValidationError(
            {
                "row": [
                    (
                        "row number must be in available range: "
                        f"(1, rows): (1, {rows})"
                    )
                ]
            }
        )

    if not 1 <= self.seat <= seats:
        raise ValidationError(
            {
                "seat": [
                    (
                        "seat number must be in available range: "
                        f"(1, seats_in_row): (1, {seats})"
                    )
                ]
            }
        )
