# dead simple PID class in python demo
# docs for simple_pid here: https://simple-pid.readthedocs.io/en/latest/simple_pid.html
# reference material that informs this class:
# http://brettbeauregard.com/blog/2011/04/improving-the-beginners-pid-introduction/

from simple_pid import PID
import matplotlib.pyplot as plt

# example initialization of the controller
# pid = PID(1, 0.1, 0.05, setpoint=1, sample_time=0.01, output_limits=(None, None), auto_mode=True, proportional_on_measurement=False)

# initialize a PID controller to run at 100 Hz
pid = PID(1, 0.1, 0.05, setpoint=1, sample_time=0.01, output_limits=(None, None))

# initialize the system to be controlled
sys_state = 1

while True:
    # compute new ouput from the PID according to the systems current value
    ctrl_output = pid(sys_state)

    # obtain the control output from each term for debugging and tuning purposes
    p, i, d = pid.components

    # feed the PID output to the system and get its current value
    sys_state = 1 # system state would be updated here by the control output