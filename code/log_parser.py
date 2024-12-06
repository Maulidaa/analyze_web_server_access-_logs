def parse_log(file_path):
    with open(file_path, 'r') as file:
        logs = []
        for line in file:
            parts = line.split()
            if len(parts) < 9:
                continue

            log_entry = {
                "ip": parts[0],
                "date": parts[3][1:],  # Remove the opening bracket
                "method": parts[5][1:],  # Remove the opening quote
                "url": parts[6],
                "status": parts[8],
                "size": int(parts[9]) if parts[9].isdigit() else 0
            }
            logs.append(log_entry)
    return logs
