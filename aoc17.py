def probe(trench):
    x_min, x_max, y_min, y_max = trench
    x_range = range(x_min, x_max + 1)
    y_range = range(y_min, y_max + 1)

    # vy_init = 1
    vy_init = y_min
    results_pt_one = set()
    results_pt_two = []
    while vy_init <= abs(y_min):
        vx_init = 1

        # while vx_init <= int(x_max / (2 * vy_init + 1) + vy_init) + 1: # in the case, probe reaches (x_max, 0)
        while vx_init <= x_max:
            x, y = 0, 0
            vx, vy = vx_init, vy_init

            while y > y_min and (x <= x_max or (x < x_min and vx > 0)):
                x += vx
                y += vy

                if vx > 0:
                    vx += -1
                elif vx < 0:
                    vx += 1
                vy += -1

                if x in x_range and y in y_range:
                    results_pt_two.append((vx_init, vy_init))
                    results_pt_one.add(vy_init)
                    break

            vx_init += 1

        vy_init += 1

    return results_pt_one, results_pt_two

def hightest(vy_init):
    return (1 + vy_init) * vy_init // 2

if __name__ == "__main__":
    # x_min, x_max = 56, 76
    # y_min, y_max = -162, -134

    # test
    x_min, x_max = 20, 30
    y_min, y_max = -10, -5

    trench = x_min, x_max, y_min, y_max
    result1, result2 = probe(trench)
    print(f"Part one: {hightest(max(result1))}")
    print(f"Part two: {len(result2)}")
