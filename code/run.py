from log_parser import parse_log
from analyzer import (
    analyze_upload_php_shell,
    analyze_execute_php_shell,
    analyze_gacor_planting,
    analyze_most_access,
    analyze_bruteforce_attempts,
    analyze_sensitive_file_downloads
)
from table_formatter import format_logs_as_table
from table_saver import save_to_table
from json_saver import save_to_json

log_file_path = "../log_analyzer/access.log"  # Path to the log file

# Parse logs
logs = parse_log(log_file_path)

# Analyze specific scenarios
upload_php_shell_logs = analyze_upload_php_shell(logs)
execute_php_shell_logs = analyze_execute_php_shell(logs)
gacor_logs = analyze_gacor_planting(logs)
most_access_ip = analyze_most_access(logs)
bruteforce_logs = analyze_bruteforce_attempts(logs)
sensitive_download_logs = analyze_sensitive_file_downloads(logs)

# Display results in tables
format_logs_as_table(upload_php_shell_logs, "Upload PHP Shell Logs")
format_logs_as_table(execute_php_shell_logs, "Execute PHP Shell Logs")
format_logs_as_table(gacor_logs, "Gacor Planting Logs")
print(f"\nMost Accessed IP: {most_access_ip['ip']} with {most_access_ip['count']} accesses\n")
format_logs_as_table(bruteforce_logs, "Bruteforce Attempt Logs")
format_logs_as_table(sensitive_download_logs, "Sensitive File Download Logs")

# Save results to JSON files
save_to_json(upload_php_shell_logs, "../log_analyzer/resault/upload_php_shell_logs.json")
save_to_json(execute_php_shell_logs, "../log_analyzer/resault/execute_php_shell_logs.json")
save_to_json(gacor_logs, "../log_analyzer/resault/gacor_logs.json")
save_to_json({"ip": most_access_ip['ip'], "count": most_access_ip['count']}, "../log_analyzer/resault/most_accessed_ip.json")
save_to_json(bruteforce_logs, "../log_analyzer/resault/bruteforce_logs.json")
save_to_json(sensitive_download_logs, "../log_analyzer/resault/sensitive_download_logs.json")

# Save results to CSV tables in the `tabel` folder
save_to_table(upload_php_shell_logs, "../log_analyzer/tabel/upload_php_shell_logs.csv")
save_to_table(execute_php_shell_logs, "../log_analyzer/tabel/execute_php_shell_logs.csv")
save_to_table(gacor_logs, "../log_analyzer/tabel/gacor_logs.csv")
save_to_table([{"IP Address": most_access_ip['ip'], "Access Count": most_access_ip['count']}], "../log_analyzer/tabel/most_accessed_ip.csv")
save_to_table(bruteforce_logs, "../log_analyzer/tabel/bruteforce_logs.csv")
save_to_table(sensitive_download_logs, "../log_analyzer/tabel/sensitive_download_logs.csv")
