def solution(queries):
    returned_data = []
    query_data = {}
    timestamp_data = {}
    backups = {}
    backups_total_backups = {}

    def set_query(query):
        employee, field, value = query[1:]
        query_data[employee] = query_data.get(employee, {})
        query_data[employee][field] = value
        returned_data.append("")

    def get_query(query):
        employee, field = query[1:]
        if not query_data.get(employee, {}) or field not in query_data[employee]:
            returned_data.append("")
        else:
            returned_data.append(query_data[employee][field])

    def delete_query(query):
        employee, field = query[1:]
        if not query_data.get(employee, {}) or field not in query_data[employee]:
            returned_data.append("false")
        else:
            query_data[employee].pop(field)
            returned_data.append("true")

    def scan_query(query):
        employee = query[1]
        if not query_data.get(employee, {}):
            returned_data.append("")
        else:
            fields = []
            for field, value in query_data[employee].items():
                fields.append(f"{field}({value})")
            fields.sort()
            returned_data.append(", ".join(fields))

    def scan_by_prefix_query(query):
        employee, prefix = query[1:]
        if not query_data.get(employee, {}):
            returned_data.append("")
        else:
            fields = []
            n = len(prefix)
            for field, value in query_data[employee].items():
                if field[:n] == prefix:
                    fields.append(field)
            fields.sort()
            final_fields = []
            for field in fields:
                final_fields.append(f"{field}({query_data[employee][field]})")
            returned_data.append(", ".join(final_fields))

    def set_at_query(query):
        employee, field, value, timestamp = query[1:]
        query_data[employee] = query_data.get(employee, {})
        query_data[employee][field] = value
        returned_data.append("")

        timestamp_data[employee] = timestamp_data.get(employee, {})
        timestamp_data[employee][field] = [int(timestamp)]

    def set_at_with_ttl_query(query):
        employee, field, value, timestamp, ttl = query[1:]
        query_data[employee] = query_data.get(employee, {})
        query_data[employee][field] = value
        returned_data.append("")
        timestamp_data[employee] = timestamp_data.get(employee, {})
        timestamp_data[employee][field] = [int(timestamp), int(timestamp) + int(ttl)]

    def get_at_query(query):
        employee, field, timestamp = query[1:]
        if not query_data.get(employee, {}) or field not in query_data[employee]:
            returned_data.append("")
        else:
            if len(timestamp_data[employee][field]) == 1 and timestamp_data[employee][field][0] <= int(timestamp):
                returned_data.append(query_data[employee][field])
            elif timestamp_data[employee][field][0] <= int(timestamp) < timestamp_data[employee][field][1]:
                returned_data.append(query_data[employee][field])
            else:
                returned_data.append("")

    def scan_by_prefix_at_query(query):
        employee, prefix, timestamp = query[1:]
        if not query_data.get(employee, {}):
            returned_data.append("")
        else:
            fields = []
            n = len(prefix)
            for field, value in query_data[employee].items():
                if field[:n] == prefix:
                    if len(timestamp_data[employee][field]) == 1 and timestamp_data[employee][field][0] <= int(
                            timestamp):
                        fields.append(field)
                    elif timestamp_data[employee][field][0] <= int(timestamp) < timestamp_data[employee][field][1]:
                        fields.append(field)
            fields.sort()
            final_fields = []
            for field in fields:
                final_fields.append(f"{field}({query_data[employee][field]})")
            returned_data.append(", ".join(final_fields))

    def delete_at_query(query):
        employee, field, timestamp = query[1:]
        if not query_data.get(employee, {}) or field not in query_data[employee]:
            returned_data.append("false")
        else:
            if len(timestamp_data[employee][field]) == 1 and timestamp_data[employee][field][0] <= int(timestamp):
                query_data[employee].pop(field)
                returned_data.append("true")
            elif timestamp_data[employee][field][0] <= int(timestamp) < timestamp_data[employee][field][1]:
                query_data[employee].pop(field)
                returned_data.append("true")
            else:
                returned_data.append("false")

    def scan_at(query):
        employee, timestamp = query[1:]
        if not query_data.get(employee, {}):
            returned_data.append("")
        else:
            fields = []
            for field, value in query_data[employee].items():
                if len(timestamp_data[employee][field]) == 1 and timestamp_data[employee][field][0] <= int(timestamp):
                    fields.append(f"{field}({value})")
                elif timestamp_data[employee][field][0] <= int(timestamp) < timestamp_data[employee][field][1]:
                    fields.append(f"{field}({value})")
            fields.sort()
            returned_data.append(", ".join(fields))

    def backup_query(query):
        timestamp = int(query[1])
        backup_data = {}
        backup_timestamps = {}
        total_backups = 0

        for employee in query_data:
            for field, value in query_data[employee].items():
                if field in timestamp_data[employee]:
                    ts_info = timestamp_data[employee][field]
                    if len(ts_info) == 1:
                        if ts_info[0] <= timestamp:
                            backup_data[employee] = backup_data.get(employee, {})
                            backup_data[employee][field] = value
                            backup_timestamps[employee] = backup_timestamps.get(employee, {})
                            backup_timestamps[employee][field] = ts_info
                            total_backups += 1
                    elif ts_info[0] <= timestamp < ts_info[1]:
                        remaining_ttl = ts_info[1] - timestamp
                        backup_data[employee] = backup_data.get(employee, {})
                        backup_data[employee][field] = value
                        backup_timestamps[employee] = backup_timestamps.get(employee, {})
                        backup_timestamps[employee][field] = [ts_info[0], remaining_ttl]
                        total_backups += 1

        backups[timestamp] = (backup_data, backup_timestamps)
        backups_total_backups[timestamp] = total_backups
        returned_data.append(str(total_backups))

    def restore(query):
        timestamp = int(query[1])
        timestamp_to_restore = int(query[2])
        backup_times = sorted(backups.keys(), reverse=True)

        for time in backup_times:
            if time <= timestamp_to_restore:
                backup_data, backup_timestamps = backups[time]
                query_data.clear()
                timestamp_data.clear()

                for employee in backup_data:
                    query_data[employee] = backup_data[employee]
                for employee in backup_timestamps:
                    timestamp_data[employee] = timestamp_data.get(employee, {})
                    for field, ts_info in backup_timestamps[employee].items():
                        if len(ts_info) == 1:
                            timestamp_data[employee][field] = ts_info
                        else:
                            initial_timestamp, remaining_ttl = ts_info
                            new_expiry = timestamp + remaining_ttl
                            timestamp_data[employee][field] = [timestamp, new_expiry]
                break

        returned_data.append("")

    for query in queries:
        key = query[0]
        if key == "SET":
            set_query(query)
        elif key == "GET":
            get_query(query)
        elif key == "DELETE":
            delete_query(query)
        elif key == "SCAN":
            scan_query(query)
        elif key == "SCAN_BY_PREFIX":
            scan_by_prefix_query(query)
        elif key == "SET_AT":
            set_at_query(query)
        elif key == "SET_AT_WITH_TTL":
            set_at_with_ttl_query(query)
        elif key == "GET_AT":
            get_at_query(query)
        elif key == "SCAN_BY_PREFIX_AT":
            scan_by_prefix_at_query(query)
        elif key == "DELETE_AT":
            delete_at_query(query)
        elif key == "SCAN_AT":
            scan_at(query)
        elif key == "BACKUP":
            backup_query(query)
        elif key == "RESTORE":
            restore(query)

    print(returned_data)
    return returned_data


print(solution([
    ["SET_AT_WITH_TTL", "A", "B", "C", "1", "10"],
    ["BACKUP", "3"],
    ["SET_AT", "A", "D", "E", "4"],
    ["BACKUP", "5"],
    ["DELETE_AT", "A", "B", "8"],
    ["BACKUP", "9"],
    ["RESTORE", "10", "7"],
    ["BACKUP", "11"],
    ["SCAN_AT", "A", "15"],
    ["SCAN_AT", "A", "16"],
]) == ["", "1", "", "1", "true", "1", "", "1", "B(C), D(E)", "D(E)"])

# could not get the final part of part 4, so this question is not entirely correct, every function besides backup_query and restore worked as expected
