import numpy as np
import random
def fl_to_fp(f):
    return np.float16(f).view(np.uint16)
def gen_inputs():
    while True:
        f=np.float16(random.uniform(0,1000))
        if np.isfinite(f):
            return f
def gen_test_cases():
    opc=random.randint(0,4)
    if opc==0:
        a=random.randint(-500,500)
        b=0.0
        out=np.float16(a)
    else:
        a=gen_inputs()
        b=gen_inputs()
        if opc==1:
            out=np.float16(a+b)
        elif opc==2:
            out=np.float16(a-b)
        elif opc==3:
            out=np.float16(a*b)
        else:
            out=np.float16(a/b)
    return fl_to_fp(a),fl_to_fp(b),opc,fl_to_fp(out),out
N=1000
py_results=[]
with open(r"File Directory","w") as f:
    for i in range(N):
        a_bin, b_bin, opc, expected_bin, expected_val = gen_test_cases()
        f.write(f"{a_bin:016b} {b_bin:016b} {opc:03b}\n")
        py_results.append(expected_bin)
with open(r"File Directory","w") as f:
    for results in py_results:
        f.write(f"{results: 016b}\n")     
