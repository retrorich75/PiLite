#!/usr/bin/env python
import arrow

from PiLiteLib import PiLiteBoard, poll_for_updates, CyclingSources


class WorldTime(object):
    def __init__(self, label, timezone):
        self.label = label
        self.timezone = timezone

    def message(self):
       now = arrow.utcnow().to(self.timezone)
       return "{} : {}".format(self.label, now.format("HH:mm:ss"))

        
def main():
    # You can customise which timezones to show by adding the appropriate City and Continent/City
    # as can be found on the following WikiPedia page http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    source = CyclingSources(WorldTime("London", "Europe/London"),
               WorldTime("Cairo", "Africa/Cairo"),
               WorldTime("Paris", "Europe/Paris"))
    sink = PiLiteBoard()
    print("ready")
    sink.write("ready  ")
    # the number 60 before /len is the number of seconds to wait before showing the next time
    poll_for_updates(source, sink, 60/len(source))


if __name__ == "__main__":
    main()
