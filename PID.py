import numpy as np
import matplotlib.pyplot as plt

class PID_controller:

    def __init__(self,Kp,Ti,Td,T,u_0=0):
        self.Kp= Kp
        self.Ti = Ti
        self.Td = Td
        self.T = T
        self.u_out = []
        self.e_k = 0
        self.e_k_1 = 0
        self.t_all = []
        self.e_add = 0
        self.u_0 = u_0
        self.u = u_0

    def set_Impuls(self,e_k):
        self.u = self.u + e_k

    def start_controll(self):
        t = 0
        while(t<15*self.T):
            t += self.T
            self.t_all.append(t)
            self.e_k = self.u_0-self.u
            self.e_add += self.e_k
            self.u = self.Kp*(self.e_k + self.T/self.Ti*self.e_add + self.Td/self.T*(self.e_k-self.e_k_1))+self.u
            print(self.u)
            self.u_out.append(self.u)
            self.e_k_1 = self.e_k
    
    def diagramm(self):
        t = np.array(self.t_all)
        u = np.array(self.u_out)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(t,u)
        ax.scatter(t,u,c = "r")
        ax.set_xlabel("time")
        ax.set_ylabel("out")
        ax.set_xlim(0,15*self.T)
        ax.set_ylim(5.5,6.5)
        plt.show()

