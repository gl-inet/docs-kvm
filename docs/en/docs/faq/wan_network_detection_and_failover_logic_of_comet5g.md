# What is the WAN Network Detection and Failover logic of Comet 5G

1. The system uses ping‑based detection, sending probes to all interfaces every **3 seconds** and evaluating failover conditions every **9 seconds**.  
   
2. If all ping tests to the higher‑priority interface fail within a **9 second** period while the lower‑priority interface remains reachable, a failover is triggered after that period. No failover occurs if all interfaces are unreachable.  
   
3. Interfaces marked offline continue to receive background ping probes.  
   
4. Recovery: If the higher‑priority interface becomes ping‑reachable within **9 seconds**, the system switches back to it after that period.