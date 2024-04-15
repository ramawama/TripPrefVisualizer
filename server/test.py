import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir=os.path.dirname(current_dir)
database_files_dir=os.path.join(root_dir, 'database')
sys.path.append(database_files_dir)

import trip_leader

print(trip_leader.get_all_leaders())