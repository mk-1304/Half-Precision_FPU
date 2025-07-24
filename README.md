# IEEE 754 Half-Precision Floating Point Unit (FPU) Design and Verification

This project implements and verifies a Half-Precision (16-bit) Floating Point Unit (FPU) compliant with the IEEE 754 standard. Functional simulation is performed using a Python-based testbench that generates randomized and edge-case test vectors. The system compares the output from Verilog simulation with Python reference results to evaluate the arithmetic accuracy of the hardware logic.

## Tools and Technologies

- Verilog HDL – Hardware description of IEEE 754 FPU logic  
- Python + NumPy – Test vector generation and reference calculation  
- Icarus Verilog / ModelSim – Simulation environment  
- IEEE 754 – Half-precision binary16 floating-point standard  

## Project Files

- [FPU Testbench](FPU_testbench)
- [Testcase Generator](testcase_generator.py)
- [Results Comparison](fpu_compare.py)
- [Results](Results)
- [Verilog Result](Verilog_results.png)

## Key Highlights

- Implements IEEE 754 half-precision operations: Add, Subtract, Multiply, Divide  
- Verifies arithmetic logic through Python-based simulation  
- Supports large-scale automated testing using NumPy  
- Detects mismatches due to rounding, subnormals, overflows, and invalid operations  
- Simple file-based interface for simulation across any HDL simulator  
- Achieved 99.7% accuracy on comparision with python generated results 

**Note:** For the complete report, and detailed module implementation, please reach out via email.

## Author

Madhusudan Kannan  
[LinkedIn](https://www.linkedin.com/in/madhusudan-kannan)  
maddyoff.04@gmail.com
