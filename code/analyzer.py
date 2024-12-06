from collections import defaultdict
from datetime import datetime


def analyze_upload_php_shell(logs):
    upload_php_shell_logs = [
        log for log in logs
        if "upload" in log["url"].lower() and "php" in log["url"].lower()
           and log["method"] == "POST"
           and log["status"] == "200"
    ]
    return upload_php_shell_logs


def analyze_execute_php_shell(logs):
    return [
        log for log in logs if "exec" in log["url"].lower() and "php" in log["url"].lower()
        and log["status"] == "200"
        and log["method"] == "GET"
    ]


def analyze_gacor_planting(logs):
    return [
        log for log in logs
        if "gacor" in log["url"].lower()
        and log["status"] in ["200", "201"]
        and log["method"] in ["POST", "PUT"]
    ]


def analyze_most_access(logs):
    ip_counts = {}

    for log in logs:
        if log["status"] in ["200", "201"]:
            ip_counts[log["ip"]] = ip_counts.get(log["ip"], 0) + 1

    if not ip_counts:
        return None

    most_access_ip = max(ip_counts, key=ip_counts.get)

    return {"ip": most_access_ip, "count": ip_counts[most_access_ip]}


def analyze_bruteforce_attempts(logs):
    brute_force_logs = [
        log for log in logs if
        (log["status"] in ["404", "403"]) and
        (log["method"] == "POST") and
        ("failed" in log["url"].lower() or "login" in log["url"].lower() or "bruteforce" in log["url"].lower())
    ]

    grouped_logs = defaultdict(list)

    for log in brute_force_logs:
        grouped_logs[log["ip"]].append(log)

    result = []

    for ip, logs in grouped_logs.items():
        total_attempts = len(logs)
        status = logs[0]["status"]
        method = logs[0]["method"]
        url = logs[0]["url"]

        timestamps = [datetime.strptime(log["date"], "%d/%b/%Y:%H:%M:%S") for log in logs]
        start_time = min(timestamps)
        end_time = max(timestamps)

        result.append({
            "ip": ip,
            "status": status,
            "method": method,
            "url": url,
            "total_attempts": total_attempts,
            "start_time": start_time.strftime("%d/%b/%Y:%H:%M:%S"),
            "end_time": end_time.strftime("%d/%b/%Y:%H:%M:%S")
        })

    return result


def analyze_sensitive_file_downloads(logs):
    sensitive_extensions = [".sql", ".db", ".backup", ".csv", ".xlsx", ".zip"]

    sensitive_logs = []
    for log in logs:
        # Ensure that the 'url' key exists and is a string
        if "url" in log and isinstance(log["url"], str):
            if log["method"] == "GET" and log["status"] == "200":
                if any(log["url"].lower().endswith(ext) for ext in sensitive_extensions):
                    sensitive_logs.append(log)

    return sensitive_logs
