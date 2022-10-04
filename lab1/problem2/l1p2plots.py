import numpy as npimport matplotlib.pyplot as pltfilename = "transZout.out"data = np.loadtxt(filename)z0 = np.where(data[:,0] == 0)z11 = np.where(data[:,0] == 11)z30 = np.where(data[:,0] == 30)z50 = np.where(data[:,0] == 50)fig = plt.figure()ax = fig.add_subplot(1, 1, 1)plt.plot(np.transpose(data[z0,1]), np.transpose(data[z0,2]), label='z = 0 km')plt.plot(np.transpose(data[z11,1]), np.transpose(data[z11,2]), label='z = 11 km')plt.plot(np.transpose(data[z30,1]), np.transpose(data[z30,2]), label='z = 30 km')plt.plot(np.transpose(data[z50,1]), np.transpose(data[z50,2]), label='z = 50 km')plt.legend()plt.xlabel('Wavelangth (nm)')plt.ylabel('Direct Transmittance')plt.title('Direct Transmittance Lowtran\nSource: solar, rte_solver: disort, effects from aerosols')