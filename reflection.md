## **General:**

This assignment was completed by Sonora Halili as part of the coursework for CSC 249. I refered to my textbook, class notes, as well as python docs and materials provided in this assignment to complete it. 


**How I went about solving this problem:**



1) For a start, I studied the document that Jordan sent on the slack channel on the ICMP header composition. This handout helped inform my understanding of the code in the `sendOnePing()` method. 

    *  This line contains information about the echo request components. `header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)` 
    * Header is type 8, code 0, checksum myChecksum, id ID, sequence 1
    * I also studied the python struct and this is the definition I found: "Python struct module is capable of performing the conversions between the Python values and C structs, which are represented as Python Strings."
    * In `sendOnePing()`, `struct.pack()` is used. This method "packs a list of values into a String representation of the specified type".
    * This means that I should use its reverse function, `struct.unpack()` to interpret into its original representation.
    * Another method of Python struct is  `struct.calcsize()`, which returns the size of the string representation. 
    



2) Then, I studied the existing code in `receiveOnePing()`: 
    
    * In echo reply, we should fetch the following information: type, code, checksum, packetID, sequence
    * From the handout, we know that in the echo reply both the type and code components are 0 and that ID and Sequence # are used to match echo request with echo reply.



3) Therefore, the first step will be to extract the ICMP header from the IP header. 
    * The ICMP header starts in bit 160 and ends in bit 191. Translated to bytes, this means 20 to 28. 

4) Then, uncpack the packet received and extracting all the information from it. Calculate the size of the echo reply and extract the time it was sent. Return the difference. 


## What worked for me:
`ICMPpinger.py` and `ICMPtraceroute.py` have lots of commonalities. Therefore, my advice for someone doing this assignment in the future would be:
1) Skim the code; no need to understand every bit of it yet
2) Do some research on ICMP headers and how they work 
3) Heavily refer to already-provided code on the pinger to fill in the blanks for traceroute (I personally did this and it simplified traceroute so much for me)
4) If you are getting permission errors when you run your code on the terminal, start your command with `sudo`. 


## What I would've done differently: 
1) I would not have spent so much time tryingto understand every line of code; instead, I would've "zoomed out" to see the bigger picture 
2) I would have looked up the errors I was initially getting instead of running the code again hoping that it was magically fixed
3) I would've used my time a little better. 

## Part 1: `ping` Results
**Results upon trying pinger on 4 different hosts:**

*Europe:* `www.casa-museumedeirosealmeida.pt`

        ('RTT: ', 0.10922813415527344)
        ('RTT: ', 0.11876583099365234)
        ('RTT: ', 0.12487387657165527)
        ('RTT: ', 0.14005303382873535)
        ('RTT: ', 0.23219799995422363)
        ('RTT: ', 0.15179681777954102)
        ('RTT: ', 0.10836386680603027)
        ('RTT: ', 0.10701608657836914)
        ('RTT: ', 0.11514091491699219)


*Asia:* `https://en.baochinhphu.vn/`

        ('RTT: ', 0.39681196212768555)
        ('RTT: ', 0.24023818969726562)
        ('RTT: ', 0.24398088455200195)
        ('RTT: ', 0.2672710418701172)
        ('RTT: ', 0.2541391849517822)
        ('RTT: ', 0.2678568363189697)
        ('RTT: ', 0.25041985511779785)
        ('RTT: ', 0.25598716735839844)
        ('RTT: ', 0.25560712814331055)
        ('RTT: ', 0.2429039478302002)
        ('RTT: ', 0.2702181339263916)
        ('RTT: ', 0.24834394454956055)

*North America:* `facebook.com`

        ('RTT: ', 0.012544870376586914)
        ('RTT: ', 0.03463482856750488)
        ('RTT: ', 0.06809806823730469)
        ('RTT: ', 0.027975082397460938)
        ('RTT: ', 0.0473480224609375)
        ('RTT: ', 0.06676506996154785)
        ('RTT: ', 0.01777791976928711)
        ('RTT: ', 0.049302101135253906)
        ('RTT: ', 0.05202603340148926)
        ('RTT: ', 0.04668092727661133)
        ('RTT: ', 0.043836116790771484)
        ('RTT: ', 0.047930002212524414)
        ('RTT: ', 0.06890201568603516)

*Africa:* `https://statehouse.gov.ng/`

        ('RTT: ', 0.2182300090789795)
        ('RTT: ', 0.23429489135742188)
        ('RTT: ', 0.19131016731262207)
        ('RTT: ', 0.36115503311157227)
        ('RTT: ', 0.2647700309753418)
        ('RTT: ', 0.21948695182800293)
        ('RTT: ', 0.22829508781433105)
        ('RTT: ', 0.18986201286315918)
        ('RTT: ', 0.19879794120788574)
        ('RTT: ', 0.21749591827392578)
        ('RTT: ', 0.23298978805541992)

## Part 2: `traceroute` Results

**Results upon trying traceroute on 4 different hosts:**

*Europe:* `www.casa-museumedeirosealmeida.pt`

        1 rtt=10 ms 131.229.239.254
        2 rtt=40 ms 131.229.11.105
        3 rtt=23 ms 131.229.10.104
        4 rtt=4 ms 134.241.249.33
        5 rtt=5 ms 69.16.1.33
        6 rtt=10 ms 69.16.0.9
        7 rtt=9 ms 38.104.218.13
        8 rtt=10 ms 154.54.41.129
        9 rtt=20 ms 154.54.46.34
        10 rtt=22 ms 154.54.40.110
        11 rtt=133 ms 154.54.85.246
        12 rtt=102 ms 154.54.61.106
        13 rtt=231 ms 154.54.61.213
        14 rtt=120 ms 149.6.144.210
        15 rtt=109 ms 94.46.128.56
        16 rtt=158 ms 94.46.128.204

*Asia:* `https://en.baochinhphu.vn/`

        1 rtt=16 ms 131.229.239.254
        2 rtt=20 ms 131.229.11.105
        3 rtt=22 ms 131.229.10.104
        4 rtt=4 ms 134.241.249.33
        5 rtt=6 ms 69.16.1.33
        6 rtt=5 ms 18.2.136.89
        7 rtt=7 ms 64.57.20.18
        8 rtt=69 ms 163.253.1.21
        9 rtt=223 ms 163.253.2.144
        10 rtt=73 ms 163.253.1.211
        11 rtt=70 ms 163.253.1.206
        12 rtt=71 ms 163.253.2.29
        13 rtt=68 ms 163.253.1.250
        14 rtt=106 ms 163.253.1.169
        15 rtt=71 ms 163.253.1.114
        16 rtt=69 ms 163.253.1.197

*North America:* `www.facebook.com`

        1 rtt=16 ms 131.229.239.254
        2 rtt=39 ms 131.229.11.105
        3 rtt=18 ms 131.229.10.104
        4 rtt=4 ms 134.241.249.33
        5 rtt=6 ms 69.16.1.33
        6 rtt=5 ms 18.2.136.89
        7 rtt=18 ms 192.5.89.42
        8 rtt=13 ms 18.2.145.22
        9 rtt=13 ms 157.240.47.25
        10 rtt=13 ms 157.240.38.247


*Africa:* `https://statehouse.gov.ng/`

        1 rtt=67 ms 131.229.239.254
        2 rtt=137 ms 131.229.11.105
        3 rtt=93 ms 131.229.10.104
        4 rtt=4 ms 134.241.249.33
        5 rtt=4 ms 69.16.1.33
        6 rtt=5 ms 18.2.136.89
        7 rtt=14 ms 192.5.89.57
        8 rtt=8 ms 206.53.143.4
