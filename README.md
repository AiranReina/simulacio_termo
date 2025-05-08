Aquest repositori conté el material creat per Airan Reina Delgado (NIU: 1670808) i Arnau Vila Crespo (NIU: 1657695) per la realització del "Treball de Simulació" proposat pel profesorat de l'assignatura de Termodinàmica i Mecànica Estadística. El repositori conté l'arxiu enunciat_simulacions.pdf on es troben els exercicis a resoldre en el projecte, juntament amb 3 arxius Python. Aquests arxius són gas_esferes_dures.py, lennard_jones.py i monte_carlo.py, i corresponen als codis emprats per la realització dels 3 exercicis proposats, en ordre.

----------

**1. GAS ESFERES DURES**

1. Arxiu: ged_q1.py

S'ha estudiat la simulació d'un gas ideal d'heli en una caixa en contacte amb un bany tèrmic. 

S'ha afegit al codi el càlcul del temps mitjà entre col·lisions, tant de la simulació com el teòric, per diferents valors del radi atòmic i s'ha realitzat el gràfic corresponent. En compilar l'arxiu, aquest et mostra en pantalla la gràfica corresponent.

---

2. Arxiu: ged_q2.py

S'ha simulat un procés isòcor implementant un termostat d'Andersen.

S'ha implementat el termostat d'Andersen fent que les partícules redefineixin la seva velocitat quan xoquen amb les parets segons una distribució de Maxwell-Boltzmann centrada a una Temperatura del termostat. El codi realitza una simulació per cadascún dels diferents radis proposats. Aquest acaba descarregant una imatge de la pràfica generada, que és ged_isocor.png

---

3. Arxiu: ged_q3.py

S'ha simulat una expansió isoterma implementant unes parets móbils i un termostat d'Andersen.

El codi és similar al de la Q2 però ara les parets es mouen respecte una velocitat constant. El codi ha generat diverses imatges: ged_isoterm.png, ged_isoterm2.png, ged_isoterm_pV.png i ged_isoterm_pV2.png. els que tenen 2 són executats pel codi actual, que varía el volum a 2V0. Quan el volum variaba a 5V0, aquest generaba els arxius sense 2. 

----------

**2. FLUID DE LENNARD-JONES**

Arxiu: lennard_jones.py

S'ha estudiat la coexistència líquid-vapor al voltant de la temperatura crítica mitjançant una simulació d'un fluid en dues caixes que representen els dos estats possibles. S'ha determinat aproximadament la temperatura crítica mitjançant l'observació del diagrama de fases de la simulació. Finalment, s'ha determinat els valors del paràmetre d'ordre i de la constant que relaciona les densitats de cada fase i la temperatura. Per fer-ho s'ha anat trobant diferents punts d'equilibri i s'ha realitzat una regressió lineal. Els valors obtinguts no difereixen significativament dels esperats.

El codi no ha sigut modificat, és exactament el mateix que el que proposa la pàgina ón s'ha descarregat el codi

----------

**3. CREACIÓ D'UNA SIMULACIÓ DE MONTE CARLO PRÒPIA**

Arxiu: monte_carlo.py

S'ha creat una simulació d'un gas ideal d'N partícules tancat en una hipercaixa d-dimensional mitjançant tècniques Monte Carlo. 

El codi executa la simulació un número de vegades per reduir la variació i fa la mitja dels valors extrets al final. La simulació modifica les variables que defineixen el microestat (q's i p's) seguint una distribució coherent. Degut a que es considera el límit termodinàmic, se suposa que la gran majoria de partícules col·lisionen per pas de temps. Degut a que es considera T constant, es redefineix la velocitat de totes les partícules a cada pas de temps. La regla de Metrópolis accepta els nous estats posibles i els implementa. El codi empra una fórmula alternativa per calcular la capacitat calorífica a partir de valors relacionats amb l'energía. Al final, el codi mostra per pantalla les gràfiques.

----------