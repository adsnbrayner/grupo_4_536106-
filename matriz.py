def matriz_extras_empleado_mes(regs, emps):
    regs_orden = regs[:]
    regs_orden.sort(key=lambda r: [r[0], r[1], r[2]])
    header = [0] + [m for m in range(1, 13)]
    if len(emps) == 0:
        return [header]
    filas = len(emps) + 1
    cols = 13
    M = [[0 for _ in range(cols)] for __ in range(filas)]
    for c in range(1, 13):
        M[0][c] = c
    for i in range(len(emps)):
        M[i + 1][0] = emps[i]
    for r in regs_orden:
        e = r[0]
        m = r[1]
        h_extra = r[4]
        if e in emps:
            fila = emps.index(e) + 1
            col = m
            M[fila][col] += h_extra
    return M
