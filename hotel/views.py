from django.db.models import Count, Q
from django.shortcuts import render
from django.utils import timezone
from django.views import View

from hotel.models import Room



class RoomsAvailabilityView(View):
    def get(self, request):
        days_ahead = 10
        rooms = Room.objects.all().select_related()
        days = {}

        for day_number in range(days_ahead):
            day = timezone.now() + timezone.timedelta(days=day_number + 1)
            days[f"day{day_number}"] = day
            # days = { "day0": "2019-09-02" }
            lookup = {
                f"day{day_number}": Count(
                    "reservations",
                    filter=Q(reservations__is_valid=True) & Q(reservations__date=day),
                )
            }
            # lookup = { "day0": Count(...) }
            rooms = rooms.annotate(**lookup)

        return render(request, "rooms.html", context={"rooms": rooms, "days": days})
