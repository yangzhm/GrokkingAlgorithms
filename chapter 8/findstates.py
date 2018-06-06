
"""
假设你办了个广播节目，要让全美50个州的听众都收听得到。为
此，你需要决定在哪些广播台播出。在每个广播台播出都需要支付费
用，因此你力图在尽可能少的广播台播出。
"""
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
statesneeded = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])


def findStates(states_needed):
    select_stations = []

    while states_needed:
        best_station = None
        covered_states = set()

        for station, station_states in stations.items():
            covered = station_states & states_needed
            if len(covered) > len(covered_states):
                best_station = station
                covered_states = station_states

        select_stations.append(best_station)
        states_needed = states_needed - covered_states

    return select_stations

print(findStates(statesneeded))