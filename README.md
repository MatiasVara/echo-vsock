# echo-vsock
This is a simple echo server and client over **virtio-vsock** which is meant to measure latency. This can be used to host-to-guest but also for guest-to-guest communication. The script outputs a frequency graph that is normalized around the median of the latency. The latency is calculated as the half of the time that a packet takes to travel the two ways. The current version uses only SOCK_STREAM which is bad for latency. The SOCK_DGRAM should be used instead.

# Results
## Host to Guest communication
![HostToGuest](https://raw.githubusercontent.com/MatiasVara/echo-vsock/main/HostToGuest.png)

## Guest to Host communication
![HostToGuest](https://raw.githubusercontent.com/MatiasVara/echo-vsock/main/GuestToHost.png)

## Guest to Guest communication
![HostToGuest](https://raw.githubusercontent.com/MatiasVara/echo-vsock/main/GuestToHost.png)

# Comments
matiasevara@gmail.com