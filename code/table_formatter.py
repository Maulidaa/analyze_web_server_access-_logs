from prettytable import PrettyTable

def format_logs_as_table(logs, title):
    table = PrettyTable()
    table.field_names = ["IP Address", "Date", "Method", "URL", "Status", "Size"]
    for log in logs:
        date = log.get("date", "N/A")
        status = log.get("status", "N/A")
        method = log.get("method", "N/A")
        size = log.get("size", "N/A")
        url = log.get("url", "N/A")
        table.add_row([log["ip"], date, method, url, status, size])
    print(f"\n{title}\n")
    print(table)
