import random
from matriz import matriz_extras_empleado_mes

def existe_registro(registros, e, m, d):
    return any([r[0] == e and r[1] == m and r[2] == d for r in registros])

def agregar_registro(registros, e, m, d, h_trab, h_extra):
    if not existe_registro(registros, e, m, d):
        registros.append([e, m, d, h_trab, h_extra])

def horas_extras_del_dia(h_trab, jornada_normal, extra_max):
    e = h_trab - jornada_normal
    if e < 0:
        e = 0
    if e > extra_max:
        e = extra_max
    return e

def generar_registros(max_emps, dias_mes, jornada_max, jornada_normal, extra_max):
    regs = []
    cant = random.randint(1, max_emps)
    empleados = sorted(random.sample(range(1, max_emps + 1), k=cant))
    for e in empleados:
        cant_meses = random.randint(1, 12)
        meses = sorted(random.sample(range(1, 13), k=cant_meses))
        for m in meses:
            cant_dias = random.randint(1, dias_mes)
            dias = sorted(random.sample(range(1, dias_mes + 1), k=cant_dias))
            for d in dias:
                h_trab = random.randint(0, jornada_max)
                h_extra = horas_extras_del_dia(h_trab, jornada_normal, extra_max)
                agregar_registro(regs, e, m, d, h_trab, h_extra)
    return regs

def imprimir_matriz(M, titulo):
    print("\n" + titulo + ":")
    if not M:
        print("[matriz vacía]")
        return
    cols = len(M[0])
    anchos = [0] * cols
    for r in range(len(M)):
        for c in range(cols):
            w = len(str(M[r][c]))
            if w > anchos[c]:
                anchos[c] = w
    for r in range(len(M)):
        fila_str = " ".join([str(M[r][c]).rjust(anchos[c]) for c in range(cols)])
        print(fila_str)

def totales_por_mes_desde_matriz(M):
    if not M or len(M) == 1:
        return [[m, 0] for m in range(1, 13)]
    totales = []
    c = 1
    while c <= 12:
        suma = 0
        r = 1
        while r < len(M):
            suma += M[r][c]
            r += 1
        totales.append([M[0][c], suma])
        c += 1
    return totales

def meses_max_extras(M):
    tpm = totales_por_mes_desde_matriz(M)
    valores = [par[1] for par in tpm]
    maxv = max(valores) if len(valores) > 0 else 0
    meses = [tpm[i][0] for i in range(len(tpm)) if tpm[i][1] == maxv]
    return [maxv, meses]

def totales_extras_por_empleado(regs, emps):
    totales = [[e, 0] for e in emps]
    i = 0
    while i < len(regs):
        e = regs[i][0]
        h_extra = regs[i][4]
        if e in emps:
            idx = emps.index(e)
            totales[idx][1] += h_extra
        i += 1
    return totales

def empleados_min_max_extras(regs, emps):
    totales = totales_extras_por_empleado(regs, emps)
    if len(totales) == 0:
        return [0, []], [0, []]
    horas = [par[1] for par in totales]
    minv = min(horas)
    maxv = max(horas)
    mins = [[totales[i][0], totales[i][1]] for i in range(len(totales)) if totales[i][1] == minv]
    maxs = [[totales[i][0], totales[i][1]] for i in range(len(totales)) if totales[i][1] == maxv]
    mins_orden = mins[:]
    mins_orden.sort(key=lambda x: x[0])
    maxs_orden = maxs[:]
    maxs_orden.sort(key=lambda x: x[0])
    return [minv, mins_orden], [maxv, maxs_orden]

def promedios_extras_por_empleado(regs, emps):
    totales = [[e, 0] for e in emps]
    cuentas = [[e, 0] for e in emps]
    i = 0
    while i < len(regs):
        e = regs[i][0]
        h_extra = regs[i][4]
        if e in emps:
            idx = emps.index(e)
            totales[idx][1] += h_extra
            cuentas[idx][1] += 1
        i += 1
    res = []
    j = 0
    while j < len(emps):
        e = emps[j]
        total = totales[j][1]
        cant = cuentas[j][1]
        prom = total / cant if cant > 0 else 0
        res.append([e, round(prom, 2)])
        j += 1
    r2 = res[:]
    r2.sort(key=lambda x: x[0])
    return r2

def porcentajes_extras_por_empleado(regs, emps):
    totales = [[e, 0] for e in emps]
    i = 0
    while i < len(regs):
        e = regs[i][0]
        h_extra = regs[i][4]
        if e in emps:
            idx = emps.index(e)
            totales[idx][1] += h_extra
        i += 1
    total_global = sum([par[1] for par in totales])
    res = []
    j = 0
    while j < len(totales):
        e = totales[j][0]
        t = totales[j][1]
        pct = (t * 100.0 / total_global) if total_global > 0 else 0.0
        res.append([e, round(pct, 2)])
        j += 1
    r2 = res[:]
    r2.sort(key=lambda x: x[0])
    return r2

def main():
    apertura = 10
    cierre = 22
    jornada_normal = 8
    extra_max = 4
    ventana = cierre - apertura
    jornada_max = jornada_normal + extra_max
    if jornada_max > ventana:
        jornada_max = ventana
    max_emps = 5
    emps_all = [i for i in range(1, max_emps + 1)]
    registros = generar_registros(
        max_emps=max_emps,
        dias_mes=28,
        jornada_max=jornada_max,
        jornada_normal=jornada_normal,
        extra_max=extra_max
    )
    M = matriz_extras_empleado_mes(registros, emps_all)
    imprimir_matriz(M, "1) Matriz de Horas Extras [Filas=Empleados, Columnas=Mes]")
    total_max, meses = meses_max_extras(M)
    print("\n2) Mes(es) con mayor registro de Horas Extras:")
    if len(meses) == 0:
        print("   - Sin datos")
    else:
        print("   - Total extras:", total_max, "hora(s)")
        print("   - Mes:", ", ".join([str(m) for m in meses]))
    (minv, mins), (maxv, maxs) = empleados_min_max_extras(registros, emps_all)
    print("\n3) Empleado(s) que menos horas extras trabajó:")
    if len(mins) == 0:
        print("   - Sin datos")
    else:
        print("   - Total extras:", minv, "hora(s)")
        print("   - Empleado(s): " + ", ".join(["E" + str(p[0]) for p in mins]))
    print("\n4) Empleado(s) que más horas extras trabajó:")
    if len(maxs) == 0:
        print("   - Sin datos")
    else:
        print("   - Total extras:", maxv, "hora(s)")
        print("   - Empleado(s): " + ", ".join(["E" + str(p[0]) for p in maxs]))
    proms = promedios_extras_por_empleado(registros, emps_all)
    pcts = porcentajes_extras_por_empleado(registros, emps_all)
    print("\nPromedio de horas extras por empleado:")
    k = 0
    while k < len(proms):
        print("   E" + str(proms[k][0]) + ": " + str(proms[k][1]))
        k += 1
    print("\nPorcentaje de horas extras por empleado:")
    k = 0
    while k < len(pcts):
        print("   E" + str(pcts[k][0]) + ": " + str(pcts[k][1]) + "%")
        k += 1

if __name__ == "__main__":
    main()
