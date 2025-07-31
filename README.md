# AXI Transaction Visualizer

This tool parses AXI protocol transaction logs (AW, W, B, AR, R channels) and generates Gantt-style visualizations for timeline-level debugging.

![AXI Timeline](output/axi_timeline.png)

---

##  Features

- Parses logs with AWADDR, WDATA, BRESP, ARADDR, and RDATA entries
- Channel-wise transaction extraction
- Generates timeline/Gantt chart with colored bars
- Saves visualization as high-quality PNG

---

##  Sample Input Format
[10ns] AWADDR: 0x1000 | AWVALID=1 | AWREADY=1
[12ns] WDATA: 0x55 | WVALID=1 | WREADY=1
[14ns] BRESP: OKAY | BVALID=1 | BREADY=1
[18ns] ARADDR: 0x2000 | ARVALID=1 | ARREADY=1
[20ns] RDATA: 0xAA | RVALID=1 | RREADY=1


