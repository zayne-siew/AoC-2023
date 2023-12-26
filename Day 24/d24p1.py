import sys
sys.setrecursionlimit(1000000)
ans = res = 0

with open("d24p1.txt") as f:
    s = f.read().strip()

d = []
for line in s.split("\n"):
    pos, vel = line.split(" @ ")
    pos = list(map(int, pos.split(", ")))
    vel = list(map(int, vel.split(", ")))
    d.append((pos, vel))

for i in range(len(d)):
    for j in range(i+1,len(d)):
        as_,ad = d[i]
        bs,bd = d[j]


        try:
            u = ((bs[1] - as_[1]) * bd[0] - (bs[0] - as_[0]) * bd[1]) / (bd[0] * ad[1] - bd[1] * ad[0])
            v = ((bs[1] - as_[1]) * ad[0] - (bs[0] - as_[0]) * ad[1]) / (bd[0] * ad[1] - bd[1] * ad[0])

            if u < 0 or v < 0:
                continue
            xi = bs[0] + bd[0] * v
            yi = bs[1] + bd[1] * v
            if xi >= 200000000000000 and xi <= 400000000000000 and \
               yi >= 200000000000000 and yi <= 400000000000000:
                ans += 1
        except:
            pass

print(ans)

# ox, oy, oz, mvx, mvy, mvz
# o, m

# px, py, pz, vx, vy, vz
# p, v

# o + ti * m - pi - ti * vi = 0
# o + ti * m - pi - ti * vi = 0

# ox - pxi + ti * (mvx - vxi) = 0
# oy - pyi + ti * (mvy - vyi) = 0
# oz - pzi + ti * (mvz - vzi) = 0

# ox, oy, oz, ti
import numpy as np

def get_mats(mvx, mvy, mvz):
    A = []
    b = []
    for i,((px,py,pz),(vx,vy,vz)) in enumerate(d):
        eqn = [1, 0, 0] + [0] * len(d)
        eqn[3+i] = mvx - vx
        A.append(tuple(eqn))
        b.append(px)

        eqn = [0, 1, 0] + [0] * len(d)
        eqn[3+i] = mvy - vy
        A.append(tuple(eqn))
        b.append(py)

        eqn = [0, 0, 1] + [0] * len(d)
        eqn[3+i] = mvz - vz
        A.append(tuple(eqn))
        b.append(pz)

    A = np.matrix(A)
    b = np.matrix(b).T
    return A, b

def solve_given_v(mvx, mvy, mvz, retthing=1):
    A, b = get_mats(mvx, mvy, mvz)
    return np.linalg.lstsq(A, b, rcond=None)[retthing]


vx, vy, vz = 0, 0, 0
cur_score = float(solve_given_v(vx, vy, vz))
step_size = 0.0001
lr = 1e-22
not_improve = 0
close_ctr = 0
while close_ctr < 10:
    print(f"{cur_score}, {vx:.2f} {vy:.2f} {vz:.2f}")
    dvx = float(solve_given_v(vx + step_size, vy, vz)) - cur_score
    dvy = float(solve_given_v(vx, vy + step_size, vz)) - cur_score
    dvz = float(solve_given_v(vx, vy, vz + step_size)) - cur_score

    vx -= lr * dvx
    vy -= lr * dvy
    vz -= lr * dvz

    last_score = cur_score
    cur_score = float(solve_given_v(vx, vy, vz))
    if cur_score > last_score:
        not_improve += 1

    if not_improve > 5:
        print("lowering lr")
        not_improve = 0
        lr = lr / 2

    if all(((vi + 0.5) % 1) - 0.5 < 0.001 for vi in (vx,vy,vz)):
        close_ctr += 1
    else:
        close_ctr = 0

vx = round(vx)
vy = round(vy)
vz = round(vz)

A, b = get_mats(vx,vy,vz)

res = np.linalg.solve(A[:5,:5], b[:5])
print(res[0,0] + res[1,0] + res[2,0])