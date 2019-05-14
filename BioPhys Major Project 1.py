import numpy as np
import matplotlib.pyplot as plt

# α ratio of people interacting with other communities: should be from 0.0-1.0: define as 1/r where r is distance from two communities
# β risk of getting infected: if 1.0 100% of contractoin needs to be between 0.0-1.0
# γ rate of recovery of infected person
# μ death and birth rate
# N population from data

# Comm 1
β =
γ =
α = #1/r
μ =
p =

N =
S =
I =
V = #are there those vaccinated before the diease starts
End = 1000

dS = (1-p)*N*μ-μ*S-β*S*(I/N + α*I/N)
dI = β*S*(I/N) - γ*(I/N)
dR = γ*(I/N)-μ*γ
dV = p*μ - μ*V

S = N
I = 0
R = 0
V = 0
for t in range(0,End):
    S += dS
    I += dI
    R += dR
    V += dV
