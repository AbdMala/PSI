# Project_Reusable Laconic PSI

To run the protocol on terminal, give this line on your terminal -> **python3 Run_Protocol**

In our code we have four classes Run_Protocol, Receiver, Sender and utils. Run_Protocol contains crs string, public key
and private key. Furthermore, in this class we will have instances of the receiver and sender, after that we will check
if there are an intersection or not. In the Receiver class with the receiver set Sr we compute hashing h and Ri <- Ext()
. In the Sender class with the sender set Ss we compute s, f and R. In the utils class we have some help methods to find
the generator g and Instead of explicitly listing all the primes pi in crs, we will describe them implicitly via a
pseudorandom function (PRF). For this purpose, we need a PRF which maps into the set of primes of a certain size