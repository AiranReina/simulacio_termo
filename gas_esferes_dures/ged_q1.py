from vpython import *
import matplotlib.pyplot as plt

# Web VPython 3.2

# Hard-sphere gas

win = 500
Natoms = 500  # number of atoms
L = 1  # container is a cube of side L
gray = color.gray(0.7)
mass = 4E-3/6E23  # helium mass
k = 1.4E-23  # Boltzmann constant
T = 300  # temperature
dt = 1E-5

animation = canvas(width=win, height=win, align='left')
animation.range = L
animation.title = 'A "hard-sphere" gas'
s = """  Theoretical and averaged speed distributions (meters/sec).
Initially all atoms have the same speed, but collisions
change the speeds of the colliding atoms. One of the atoms is
marked and leaves a trail so you can follow its path.
"""
animation.caption = s

r = 0.005
deltav = 100

gg = graph(width=win, height=0.4*win, xmax=3000, align='left',
           xtitle='speed, m/s', ytitle='Number of atoms', ymax=Natoms*deltav/1000)


# Llista de valors del radi dels àtoms
N=40
Radi_inicial=0.01
Radis=[0]*N

for i in range(N):
  Radis[i]=Radi_inicial+i*(0.1-Radi_inicial)/(N-1)
    
temps_mitja = []  #Llista de valors del temps mitjà entre col·lisions per a cada valor del radi dels àtoms
temps_mitja_teoric = []  #Llista de valors del temps mitjà teòric entre col·lisions per a cada valor del radi dels àtoms

pavg = sqrt(2 * mass * 1.5 * k * T)

# Càlcul dels valors del temps mitjà teòric en funció del radi dels àtoms
for i in Radis:
    d = 2*i  #Càlcul de la secció eficaç
    densitat_particules = Natoms / (L ** 3)  #Càlcul de la densitat de partícules
    velocitat_mitjana = pavg / mass    #Càlcul de la velocitat mitjana
    t_mitja_teoric= 2 / (sqrt(2) * pi * (densitat_particules ** 2) * (d**2) * velocitat_mitjana)
    temps_mitja_teoric.append(t_mitja_teoric)

for Ratom in Radis:
    
    d = L / 2 + Ratom
    boxbottom = curve(color=gray, radius=r)
    boxbottom.append([vector(-d, -d, -d), vector(-d, -d, d), vector(d, -d, d), vector(d, -d, -d), vector(-d, -d, -d)])
    boxtop = curve(color=gray, radius=r)
    boxtop.append([vector(-d, d, -d), vector(-d, d, d), vector(d, d, d), vector(d, d, -d), vector(-d, d, -d)])
    vert1 = curve(color=gray, radius=r)
    vert2 = curve(color=gray, radius=r)
    vert3 = curve(color=gray, radius=r)
    vert4 = curve(color=gray, radius=r)
    vert1.append([vector(-d, -d, -d), vector(-d, d, -d)])
    vert2.append([vector(-d, -d, d), vector(-d, d, d)])
    vert3.append([vector(d, -d, d), vector(d, d, d)])
    vert4.append([vector(d, -d, -d), vector(d, d, -d)])

    Atoms = []
    p = []
    apos = []

    for i in range(Natoms):
        x = L * random() - L / 2
        y = L * random() - L / 2
        z = L * random() - L / 2
        if i == 0:
            Atoms.append(sphere(pos=vector(x, y, z), radius=Ratom, color=color.cyan,
                                make_trail=True, retain=100, trail_radius=0.3 * Ratom))
        else:
            Atoms.append(sphere(pos=vector(x, y, z), radius=Ratom, color=gray))
        apos.append(vec(x, y, z))
        theta = pi * random()
        phi = 2 * pi * random()
        px = pavg * sin(theta) * cos(phi)
        py = pavg * sin(theta) * sin(phi)
        pz = pavg * cos(theta)
        p.append(vector(px, py, pz))

    nhisto = int(4500 / deltav)
    histo = [0.0] * nhisto
    histo[int(pavg / mass / deltav)] = Natoms

    accum = [[deltav * (i + 0.5), 0] for i in range(int(3000 / deltav))]
    vdist = gvbars(color=color.red, delta=deltav)

    def barx(v):
        return int(v / deltav)

    def interchange(v1, v2):
        barx1 = barx(v1)
        barx2 = barx(v2)
        if barx1 == barx2:
            return
        if barx1 >= len(histo) or barx2 >= len(histo):
            return
        histo[barx1] -= 1
        histo[barx2] += 1

    def checkCollisions():
        hitlist = []
        r2 = 2 * Ratom
        r2 *= r2
        for i in range(Natoms):
            ai = apos[i]
            for j in range(i):
                aj = apos[j]
                dr = ai - aj
                if mag2(dr) < r2:
                    hitlist.append([i, j])
        return hitlist

    temps_total_simulacio = 0  # Afegim un contador del temps total de simulació
    num_colisions = 0      # Afegim un contador del numero total de colisions
    
    nhisto = 0

    while True:
        rate(300)
        temps_total_simulacio += dt

        for i in range(len(accum)):
            accum[i][1] = (nhisto * accum[i][1] + histo[i]) / (nhisto + 1)
        if nhisto % 10 == 0:
            vdist.data = accum
        nhisto += 1

        for i in range(Natoms):
            Atoms[i].pos = apos[i] = apos[i] + (p[i] / mass) * dt

        hitlist = checkCollisions()

        for ij in hitlist:
            i, j = ij
            ptot = p[i] + p[j]
            posi = apos[i]
            posj = apos[j]
            vi = p[i] / mass
            vj = p[j] / mass
            vrel = vj - vi
            if vrel.mag2 == 0:
                continue
            rrel = posi - posj
            if rrel.mag > Ratom:
                continue

            dx = dot(rrel, vrel.hat)
            dy = cross(rrel, vrel.hat).mag
            alpha = asin(dy / (2 * Ratom))
            d = (2 * Ratom) * cos(alpha) - dx
            deltat = d / vrel.mag

            posi -= vi * deltat
            posj -= vj * deltat
            mtot = 2 * mass
            pcmi = p[i] - ptot * mass / mtot
            pcmj = p[j] - ptot * mass / mtot
            rrel = norm(rrel)
            pcmi -= 2 * pcmi.dot(rrel) * rrel
            pcmj -= 2 * pcmj.dot(rrel) * rrel
            p[i] = pcmi + ptot * mass / mtot
            p[j] = pcmj + ptot * mass / mtot
            apos[i] = posi + (p[i] / mass) * deltat
            apos[j] = posj + (p[j] / mass) * deltat
            interchange(vi.mag, p[i].mag / mass)
            interchange(vj.mag, p[j].mag / mass)

            num_colisions += 1

        for i in range(Natoms):
            loc = apos[i]
            if abs(loc.x) > L / 2:
                p[i].x *= -1
            if abs(loc.y) > L / 2:
                p[i].y *= -1
            if abs(loc.z) > L / 2:
                p[i].z *= -1

        if temps_total_simulacio >= 0.001001: #Aquest temps és el que tarda en estabilitzar-se considerablement el sistema.
            break

    temps_mitja.append(temps_total_simulacio / num_colisions)

# Gràfic tiemps mitjà vs radi de l'àtom


plt.style.use('classic')
plt.figure(facecolor='white')
plt.plot(Radis, temps_mitja, label='Simulació', color='blue')
plt.plot(Radis, temps_mitja_teoric, label='Teòric', color='red')
plt.legend()
plt.xlabel("Radi de l'àtom (m)")
plt.ylabel("Tiemps mitjà entre col·lisions (s)")
plt.grid(True)
plt.show()
