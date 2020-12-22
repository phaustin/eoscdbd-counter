FROM phaustin/dashboard:dec21


WORKDIR ${HOME}

# Finally, run gunicorn.
CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8000", "counter.do_count:server"]
