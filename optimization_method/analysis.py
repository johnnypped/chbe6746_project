import matplotlib.pyplot as plt

dist_list = []
angle_list = []

fh = open('convergence_phi.out','r')
lines = fh.readlines()

for line in lines:
    [d,a] = line.split()
    dist_list.append( float(d) )
    angle_list.append( float(a) )

fh.close()

fig , ax = plt.subplots()
ax.plot( angle_list , dist_list , '-ok')
ax.set_title( "Convergence of the Direct Search Algorithm" )
ax.set_xlabel( "Bond Angle (Degrees)" )
ax.set_ylabel( "Bond Distance (Angstroms)" )
plt.show()
