import re

def parse_axi_log(log_path):
    channels = {
        "AW": [],
        "W": [],
        "B": [],
        "AR": [],
        "R": []
    }

    with open(log_path, "r") as f:
        for line in f:
            timestamp_match = re.search(r"\[(\d+)ns\]", line)
            if not timestamp_match:
                continue
            time = int(timestamp_match.group(1))

            if "AWADDR" in line:
                channels["AW"].append((time, line.strip()))
            elif "WDATA" in line:
                channels["W"].append((time, line.strip()))
            elif "BRESP" in line:
                channels["B"].append((time, line.strip()))
            elif "ARADDR" in line:
                channels["AR"].append((time, line.strip()))
            elif "RDATA" in line:
                channels["R"].append((time, line.strip()))

    return channels
