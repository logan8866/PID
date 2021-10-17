from PID import PID_controller

if __name__ == "__main__":
    
    pid = PID_controller(1.25,120,0,0.1,6)
    pid.set_Impuls(1)
    pid.start_controll()
    pid.diagramm()
