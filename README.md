# BalanceBot

### Dynamics Derivations

Below are links to videos walking through the derivation of the equations of motion for the canonical inverted pendulum on a cart system. The equations of motion consist of two nonlinear differential equations. The derivations are a little bit involved, especially using Newtonian mechanics. Lagrangian approach is much easier but requires higher level math.

1. Newtonian: https://www.youtube.com/watch?v=5qJY-ZaKSic
2. Lagrangian: https://www.youtube.com/watch?v=7Tvo8jXlPuk

### Motor Specification

We plan on a 350 gram robot with the center of mass no more than 6 inches (~15 centimeters) from the motor shaft. Brushed DC motors or stepper motors are both options with stepper motors having the advantage of open loop operation (assuming they're chosen correctly based on load, and load inertia), whereas brushed motors will have the advantage of more efficient operation and simpler specification given the knows for our robot right now.

This [ECN article](https://www.ecnmag.com/blog/2015/09/dc-motors-vs-stepper-motors-motion-control-applications) provides a good synopsis of the pros and cons of each motor architecture.

[This](https://www.robotshop.com/en/pololu-12v-301-gear-motor-64-cpr-encoder.html) Polulu 12V gear motor from RobotShop satisfies our torque requirement and includes a quadrature encoder for position sensing. [This](https://www.robotshop.com/en/cytron-10a-5-30v-dual-channel-dc-motor-driver.html) dual motor driver will drive both motors on our robot with plenty of wattage overhead.

