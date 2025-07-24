import numpy as np
import random

def fl_to_fp(f):
    return np.float16(f).view(np.uint16)

def gen_inputs():
    while True:
        f = np.float16(random.uniform(0, 500))
        if np.isfinite(f):
            return f

def gen_test_cases():
    opc = random.randint(0, 4)  
    if opc == 0:
        a = random.randint(-128, 127)
        b = 0.0
        out = np.float16(a)  
        return a, fl_to_fp(b), opc, fl_to_fp(out), out
    else:
        a = gen_inputs()
        b = gen_inputs()
        a_fp = np.float16(a)
        b_fp = np.float16(b)

        a_f32 = np.float32(a_fp)
        b_f32 = np.float32(b_fp)

        if opc == 1:
            out = np.float16(a_f32 + b_f32)
        elif opc == 2:
            out = np.float16(a_f32 - b_f32)
        elif opc == 3:
            out = np.float16(a_f32 * b_f32)
        else:
            out = np.float16(a_f32 / b_f32)

        return fl_to_fp(a_fp), fl_to_fp(b_fp), opc, fl_to_fp(out), out

N = 10000
py_results = []

with open(r"File Directory", "w") as f:
    for i in range(N):
        a_bin, b_bin, opc, expected_bin, expected_val = gen_test_cases()
        if opc == 0:
            a_bin = format(a_bin & 0xFF, '08b')
            f.write(f"{a_bin} {b_bin:08b} {opc:03b}\n")
        else:
            f.write(f"{a_bin:016b} {b_bin:016b} {opc:03b}\n")
        py_results.append(expected_bin)

with open(r"File Directory", "w") as f:
    for results in py_results:
        f.write(f"{results:016b}\n")
