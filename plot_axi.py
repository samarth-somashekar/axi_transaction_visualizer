import matplotlib.pyplot as plt
from parser import parse_axi_log

# Read parsed data
channels = parse_axi_log("sample_axi_log.txt")

# Define vertical positions for each channel
channel_order = ["AW", "W", "B", "AR", "R"]
channel_ypos = {ch: 10 + i * 15 for i, ch in enumerate(channel_order)}

# Prepare data for plotting
fig, ax = plt.subplots(figsize=(10, 5))

for ch in channel_order:
    events = channels.get(ch, [])
    bar_segments = []
    for i, (timestamp, line) in enumerate(events):
        bar_segments.append((timestamp, 2))  # width = 2ns block

    ax.broken_barh(bar_segments, (channel_ypos[ch], 10), facecolors='tab:blue')
    ax.text(0, channel_ypos[ch] + 5, ch, va='center', ha='right', fontsize=10)

# Axis settings
ax.set_xlabel("Time (ns)")
ax.set_ylabel("AXI Channels")
ax.set_title("AXI Transaction Timeline")
ax.set_yticks([])
ax.set_ylim(0, 100)
ax.grid(True)

plt.tight_layout()
plt.show()
