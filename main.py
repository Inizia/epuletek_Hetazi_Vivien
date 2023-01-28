import epuletek
epuletek.fajlbeolvas()

print(f"III/A, B: \n \t Az épületek szama: {epuletek.epuletek_szama()}")
print(f"III/C: \n \t Az 555 lábnál magasabb épületek száma: {epuletek.magas_epuletek()}")
print(f"III/D: \n \t A	A legöregebb épület országa: {epuletek.legoregebb()}")