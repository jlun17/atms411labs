import numpy as npimport matplotlib.pyplot as plt# name = "brightness_afglus."# filename = name + "out"# data = np.loadtxt(filename)# data[:,0] = data[:,0] * 10**-3# fig = plt.figure(figsize=(7,5))# ax = fig.add_subplot(1, 1, 1)# plt.plot(data[:,0], data[:,1], label='umu = 0.1')# plt.plot(data[:,0], data[:,2], label='umu = 0.2')# plt.plot(data[:,0], data[:,3], label='umu = 0.3')# plt.plot(data[:,0], data[:,4], label='umu = 0.4')# plt.plot(data[:,0], data[:,5], label='umu = 0.5')# plt.plot(data[:,0], data[:,6], label='umu = 0.6')# plt.plot(data[:,0], data[:,7], label='umu = 0.7')# plt.plot(data[:,0], data[:,8], label='umu = 0.8')# plt.plot(data[:,0], data[:,9], label='umu = 0.9')# plt.plot(data[:,0], data[:,10], label='umu = 1.0')# plt.legend(loc=1)# plt.xlabel(r"Wavelength ($\mu$m)")# plt.ylabel('Brightness Temperature (K)')# plt.title('Brightness Temperature \nSource: thermal, rte_solver: disort')# plt.tight_layout()# fmt = "png"# plt.savefig(name + fmt, format=fmt, bbox_inches='tight')# plt.show(block=False)nameus = "brightness_afglus.out"namems = "brightness_afglms.out"namemw = "brightness_afglmw.out"namess = "brightness_afglss.out"namesw = "brightness_afglsw.out"namet = "brightness_afglt.out"dataus = np.loadtxt(nameus)datams = np.loadtxt(namems)datamw = np.loadtxt(namemw)datass = np.loadtxt(namess)datasw = np.loadtxt(namesw)datat = np.loadtxt(namet)fig = plt.figure(figsize=(7,5))ax = fig.add_subplot(1, 1, 1)# plt.plot(dataus[:,0], dataus[:,1], label='us')plt.plot(datams[:,0], datams[:,1], label='ms')plt.plot(datamw[:,0], datamw[:,1], label='mw')plt.plot(datass[:,0], datass[:,1], label='ss')plt.plot(datasw[:,0], datasw[:,1], label='sw')plt.plot(datat[:,0], datat[:,1], label='t')plt.legend(loc=1)plt.xlabel(r"Wavelength ($\mu$m)")plt.ylabel('Brightness Temperature (K)')plt.title('Brightness Temperature \nSource: thermal, rte_solver: disort, umu = 0.1')