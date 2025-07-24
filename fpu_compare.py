# File paths
py_file = r""
verilog_file = r""
testcase_file = r""
edge_file = r""
log_file = r""

with open(py_file, "r") as f:
    py_outputs = [line.strip() for line in f]
  
with open(verilog_file, "r") as f:
    ver_outputs = [line.strip() for line in f]

with open(testcase_file, "r") as f:
    test_vectors = [line.strip().split() for line in f]

with open(edge_file, "r") as f:
    edge_cases = [line.strip() for line in f]

total = len(py_outputs)
mismatches = 0

def format_line(i, a, b, opc, py, ver, edge):
    return (
        f"Testcase {i+1:<5}:  "
        f"A={a:<16}  B={b:<16}  Opcode={opc:<4}  "
        f"Expected={py:<16}  Actual={ver:<16}  Edge_Case={edge}"
    )

with open(log_file, "w") as f:
    for i, (py, ver) in enumerate(zip(py_outputs, ver_outputs)):
        py_val = int(py, 2)
        ver_val = int(ver, 2)

        a, b, opcode = test_vectors[i]
        edge = edge_cases[i]

        if abs(py_val - ver_val) > 5:
            mismatches += 1

        f.write(format_line(i, a, b, opcode, py, ver, edge) + "\n")

    passed = total - mismatches
    print('Total Test Cases Passes:',passed)
    f.write(f"\nTotal Test Cases Passed: {passed}/{total}\n")
