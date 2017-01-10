"""Demonstrates Python scoping."""

count = 0

def show_count():
    """Shows current count."""
    print('count = ', count)

def set_count(cnt):
    """Sets current count."""
    global count
    count = cnt
