# LiFi-using-RaspPi
Original code used to transmit a message from a Raspberry Pi to another Pi using Light Fidelity.

Aim of the project was to use existing and popular microcontrollers to use light to transmit data over an unguided medium. The hope in using a popular solution may yield previous work from which we could build. However, not many solutions were found. One solution that we ran with was using a photocell to charge a capacitor. By timing the capacitor charge time, we could optain a relative measure of the amount of light charging the photocell. Too late in the class project timing did we realize that by using a different microcontroller that has a built-in Analog to Digital Converter we could have obtained instanteous values from a photocell, or even another LED being used as a receiver.

Both transmitter and receiver code are in Python. A dictionary was used to define symbols used to minimize transmission size. The transmitter and receiver were positioned within an inch, but in the open in a brightly lit room. Due to the amount of time required to discharge the capacitor, and the fact that we used an average over multiple reads to attempt to minimize errors, our bit rate was only around 5bps.

Video of the project can be seen here: https://youtu.be/BWuD7X9XvEY

