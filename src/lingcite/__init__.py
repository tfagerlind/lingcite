import os
import sys

print("Hello")

# This is extremely ugly and should be fixed eventually. The rationale to
# introduce it was to avoid changing existing legacy code before automatic
# testing was established.
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
