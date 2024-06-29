if reps%2 == 1:
        # This is for the work time, which are all uniform in odd'th rep places
        time_counter(work_secs)
    elif reps == 8:
        time_counter(long_break_secs)
        # I don't know whether this should be in the final code but adding just in case
        # I could instead do reps = (reps + 1) % 8 above during increment but meh
    else:
        time_counter(short_break_secs)