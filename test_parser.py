from parser import parse_axi_log

log_file = "sample_axi_log.txt"
channels = parse_axi_log(log_file)

for ch, events in channels.items():
    print(f"\n{ch} channel:")
    for t, line in events:
        print(f"  {t}ns: {line}")
