import trip_leader
import json

def main():
    l=['Jane Doe', 'John Smith']
    l=json.dumps(l)
    # print(trip_leader.create_leader(1, "John Doe", 2022, 4, 5, 3, l, "Lead", "Promotion", "None", "Lead", "None", "Promotion"))
    # print(trip_leader.get_leader_by_name("John Doe"))
    # print(trip_leader.delete_leader_by_ufid(1))
    # print(trip_leader.get_leader_by_name("John Doe"))


if __name__ == "__main__":
    main()