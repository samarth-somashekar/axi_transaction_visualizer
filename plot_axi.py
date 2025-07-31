import matplotlib.pyplot as plt
from parser import parse_axi_log

# Step 1: Load parsed channels
channels = parse_axi_log("sample_axi_log.txt")

# Step 2: Layout setup
channel_order = ["AW", "W", "B", "AR", "R"]
channel_ypos = {ch: 10 + i * 15 for i, ch in enumerate(channel_order)}

channel_colors = {
    "AW": "tab:blue",
    "W": "tab:orange",
    "B": "tab:green",
    "AR": "tab:red",
    "R": "tab:purple"
}

# Step 3: Create plot
fig, ax = plt.subplots(figsize=(12, 5))

for ch in channel_order:
    events = channels.get(ch, [])
    bar_segments = []
    for i, (timestamp, line) in enumerate(events):
        bar_segments.append((timestamp, 2))  # fixed width = 2ns

    ax.broken_barh(bar_segments, (channel_ypos[ch], 10), facecolors=channel_colors[ch])

    # Label each transaction with value (like 0x1000 or 0x55)
    for timestamp, line in events:
        value = line.split('|')[0].split(':')[-1].strip()
        ax.text(timestamp + 1, channel_ypos[ch] + 5, value,
                ha='center', va='center', fontsize=7, color='white')

    ax.text(0, channel_ypos[ch] + 5, ch, va='center', ha='right', fontsize=10, fontweight='bold')

# Step 4: Final touches
ax.set_xlabel("Time (ns)")
ax.set_title("AXI Transaction Timeline")
ax.set_yticks([])
ax.set_ylim(0, max(channel_ypos.values()) + 20)
ax.set_xlim(0, 40)
ax.grid(True)

# Step 5: Save + show
plt.tight_layout()
plt.savefig("axi_timeline.png", dpi=300)
plt.show()
