ó
#â5cc           @   s   d  d l  Td  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d Z d   Z d   Z	 d   Z
 d   Z d d	  Z e d
  d S(   i˙˙˙˙(   t   *Ni   c         C   s˙   d } t  |   d d } d } xT | | k  rv t |  | d  d t |  |  } | | } | d @} | d } q# W| t  |   k  r´ | t |  t  |   d  } | d @} n  | d ?| d @} | | d ?} | } | d @} | d ?| d >d	 @B} | S(
   Ni    i   i   i   I˙˙˙˙    i   i˙˙  i   i ˙  (   t   lent   ord(   t   stringt   csumt   countTot   countt   thisValt   answer(    (    s6   /Users/sonorahalili/Documents/CSC249-HW3/ICMPpinger.pyt   checksum   s"    &


c         C   s  | } xt  rt j   } t j |  g g  g  |  } t j   | } | d g  k rZ d St j   } |  j d  \ }	 }
 |	 d d !} t j d |  \ } } } } } t d k rü | | k rü t j d  } t j d |	 d d | ! d } | | Sn  | | } | d k r	 d Sq	 Wd  S(	   Ni    s   Request timed out.i   i   i   t   bbHHhi   t   d(   t   Truet   timet   selectt   recvfromt   structt   unpackt   typet   calcsize(   t   mySockett   IDt   timeoutt   destAddrt   timeLeftt   startedSelectt	   whatReadyt   howLongInSelectt   timeReceivedt	   recPackett   addrt
   icmpHeadert   icmpTypet   codet
   myChecksumt   packetIDt   sequencet   sizeOfReplyt   timeSent(    (    s6   /Users/sonorahalili/Documents/CSC249-HW3/ICMPpinger.pyt   receiveOnePing-   s&    		!!
c         C   sÎ   d } t  j d t d | | d  } t  j d t j    } t d j t t | |    } t j	 d k r t
 |  d @} n t
 |  } t  j d t d | | d  } | | } |  j | | d f  d  S(   Ni    R
   i   R   t    t   darwini˙˙  (   R   t   packt   ICMP_ECHO_REQUESTR   R	   t   joint   mapt   chrt   syst   platformt   htonst   sendto(   R   R   R   R"   t   headert   datat   packet(    (    s6   /Users/sonorahalili/Documents/CSC249-HW3/ICMPpinger.pyt   sendOnePing]   s    "
c         C   sa   t  d  } t t t |  } t j   d @} t | |  |  t | | | |   } | j   | S(   Nt   icmpi˙˙  (	   t   getprotobynamet   sockett   AF_INETt   SOCK_RAWt   ost   getpidR6   R'   t   close(   R   R   R7   R   t   myIDt   delay(    (    s6   /Users/sonorahalili/Documents/CSC249-HW3/ICMPpinger.pyt	   doOnePing{   s    
i   c         C   sP   t  |   } d | d GHd GHx+ t rK t | |  } | GHt j d  q! W| S(   Ns   Pinging s    using Python:R(   i   (   t   gethostbynameR   RA   R   t   sleep(   t   hostR   t   destR@   (    (    s6   /Users/sonorahalili/Documents/CSC249-HW3/ICMPpinger.pyt   ping   s    	s
   google.com(   R9   R<   R/   R   R   R   t   binasciiR+   R	   R'   R6   RA   RF   (    (    (    s6   /Users/sonorahalili/Documents/CSC249-HW3/ICMPpinger.pyt   <module>   s   
			0		