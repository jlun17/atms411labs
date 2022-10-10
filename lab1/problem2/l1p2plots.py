import numpy as npimport matplotlib.pyplot as pltfilename = "transZout.out"data = np.loadtxt(filename)data[:,1] = data[:,1] * 10**-3 #convert nm -> umz0 = np.where(data[:,0] == 0)z11 = np.where(data[:,0] == 11)z30 = np.where(data[:,0] == 30)z50 = np.where(data[:,0] == 50)fig = plt.figure(figsize=(7,5))ax = fig.add_subplot(1, 1, 1)plt.plot(np.transpose(data[z0,1]), np.transpose(data[z0,2]), label='z = 0 km')plt.plot(np.transpose(data[z11,1]), np.transpose(data[z11,2]), label='z = 11 km')plt.plot(np.transpose(data[z30,1]), np.transpose(data[z30,2]), label='z = 30 km')plt.plot(np.transpose(data[z50,1]), np.transpose(data[z50,2]), label='z = 50 km')plt.legend(loc=4)plt.xlabel(r"Wavelength ($\mu$m)")plt.ylabel('Direct Transmittance')plt.title('Direct Transmittance \nSource: solar, rte_solver: disort, effects from aerosols')plt.tight_layout()fmt = "png"plt.savefig("transZout." + fmt, format=fmt, bbox_inches='tight')plt.show(block=False)