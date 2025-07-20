# IEEE 754 Half-Precision Floating Point Unit (FPU) Design and Verification

This project implements and verifies a Half-Precision (16-bit) Floating Point Unit (FPU) compliant with the IEEE 754 standard. Functional simulation is performed using a Python-based testbench that generates randomized and edge-case test vectors. The system compares the output from Verilog simulation with Python reference results to evaluate the arithmetic accuracy of the hardware logic.

## Tools and Technologies

- Verilog HDL – Hardware description of IEEE 754 FPU logic  
- Python + NumPy – Test vector generation and reference calculation  
- Icarus Verilog / ModelSim – Simulation environment  
- IEEE 754 – Half-precision binary16 floating-point standard  

## Project Files

- `tb_fp16.v` – Verilog testbench reading from and writing to text files  
- `fp16.py` – Python script for automated test generation and result checking  
- `input.txt` – Input operands and operation codes for simulation  
- `output.txt` – Verilog-generated output values  
- `results.txt` – Comparison log showing match/mismatch status  

## Key Highlights

- Implements IEEE 754 half-precision operations: Add, Subtract, Multiply, Divide  
- Verifies arithmetic logic through Python-based simulation  
- Supports large-scale automated testing using NumPy  
- Detects mismatches due to rounding, subnormals, overflows, and invalid operations  
- Simple file-based interface for simulation across any HDL simulator  
- Can be extended to support pipelined FPU cores or 32-bit/64-bit operations  

**Note:** For the complete report, simulation results, and detailed module implementation, please reach out via email.

## Author

Madhusudan Kannan  
[LinkedIn](https://www.linkedin.com/in/madhusudan-kannan)  
maddyoff.04@gmail.com
