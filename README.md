# -SoC-Verification-Using-SystemVerilog-
This project demonstrates the functional verification of a simplified System-on-Chip (SoC) design using **SystemVerilog**. The SoC includes an embedded processor and peripheral components, verified through simulation using **testbenches**, **assertions**, and **constrained-random verification** techniques.  
# SoC Verification Using SystemVerilog

## Overview

This project demonstrates the functional verification of a simplified System-on-Chip (SoC) design using **SystemVerilog**. The SoC includes an embedded processor and peripheral components, verified through simulation using **testbenches**, **assertions**, and **constrained-random verification** techniques.

The objective is to ensure correctness, improve coverage, and validate corner cases of the SoC functionality through a structured verification methodology.

---

## Technologies Used

- **SystemVerilog** – Testbench development, assertions (SVA), constrained-random generation
- **Verilog** – RTL description of the SoC
- **ModelSim / QuestaSim** – Simulation and waveform analysis
- **Functional Coverage** – Track verification completeness
- **Assertions** – Real-time protocol and behavior checking
- **Constrained-Random Testing** – Stress test corner cases

---

## Project Structure

---

## Key Features

- ✅ **Self-checking testbench** using SystemVerilog
- ✅ **Functional coverage** tracking of SoC features
- ✅ **SystemVerilog Assertions (SVA)** for protocol verification
- ✅ **Constrained-random stimulus generation**
- ✅ **Waveform analysis** for debugging and validation

---

## Getting Started

### Prerequisites

- [ModelSim](https://eda.sw.siemens.com/en-US/ic/modelsim/) or equivalent SystemVerilog simulator
- Basic knowledge of Verilog and SystemVerilog

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SoC_Verification.git
   cd SoC_Verification
2.Open ModelSim and compile:
  vlog rtl/*.v
  vlog tb/*.sv

