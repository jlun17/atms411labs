import numpy as npimport matplotlib.pyplot as pltfilenameReptran = "vertTransReptranFine.out"filenameLowtran = "vertTransLowtran.out"dataReptran = np.loadtxt(filenameReptran)dataLowtran = np.loadtxt(filenameLowtran)fig = plt.figure()ax = fig.add_subplot(1, 1, 1)plt.plot(dataLowtran[:,0], dataLowtran[:,1], label='Direct')plt.plot(dataLowtran[:,0], dataLowtran[:,2], label='Global')plt.legend()plt.xlabel('Wavelangth (nm)')plt.ylabel('Transmittance')plt.title('Transmittance Lowtran\nSource: solar, rte_solver: disort, effects from aerosols')fig = plt.figure()ax = fig.add_subplot(1, 1, 1)plt.plot(dataReptran[:,0], dataReptran[:,1], label='Direct')plt.plot(dataReptran[:,0], dataReptran[:,2], label='Global')plt.legend()plt.xlabel('Wavelangth (nm)')plt.ylabel('Transmittance')plt.title('Transmittance Reptran (fine)\nSource: solar, rte_solver: disort, effects from aerosols')