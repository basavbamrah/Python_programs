from speedtest import Speedtest

tst = Speedtest()

print(
    "Your Connection's download speed is...  ",
    str((tst.download()) / 1000000) + " Mbps",
)
print("Your Connection,s Upload Speed is... ", str((tst.upload()) / 1000000) + " Mbps")
