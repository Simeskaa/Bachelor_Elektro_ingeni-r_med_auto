import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

angle=['0', '15', '30', '45', '60'] #, '75', '90', '105', '120', '135', '150', '165', '180', '195', '210', ]
alice=[60,40,68,94,27]
bob=[81,30,75,37,46]

angles=np.linspace(0, 2 * np.pi, 24, endpoint=False)
print(angles)

angles=np.concatenate((angles,[angles[0]]))
print(angles)

angle.append(angle[0])
alice.append(alice[0])
bob.append(bob[0])

fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(polar=True)
#basic plot
ax.plot(angles,alice, 'o--', color='g', label='Alice') # plotte verdian
#fill plot
ax.fill(angles, alice, alpha=0.25, color='g') #gjær an fyldig
#Add labels
ax.set_thetagrids(angles * 180 / np.pi, angle) #velge kor mange punkt
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()


