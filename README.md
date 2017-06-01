# Undergrad Thesis - Framework to Implement Iterative Algorithms on Distributed Systems

## Abstract
In this thesis, I build a framework for implementing iterative algorithms by abstracting the code for node communication. This thesis explains the building of said framework using a distributed algorithm and introduces the tools and methods used. I first implemented an algorithm and tested it out on a testbed of 15 Raspberry pi’s. After the desired functionality was met, I then went on to proceed with abstracting the code so that similar iterative algorithms could reuse the parts of the code that dealt with inter-node communication and communication link setup. This work is funded in part by the National Science Foundation

## Acknowledgments 
I would like to thank all those people who have provided their valuable time and generous help in helping me finish my senior thesis. My deepest gratitude is to my adviser, Prof. Nitin Vaidya. I have been fortunate to have an adviser who gave me constant guidance and resources during the entirety of my research experience. His elucidation of tough subject matter at different stages of my research helped me finish this thesis. I would specially like to thank my research partner, Jihui Yang, for his expertise and help. He was the ideal partner and helped me understand the convoluted aspects of socket programming with ease. I am deeply grateful to him for pushing me into trying out new aspects of programming; I am a significantly better programmer because of it. His company throughout the project was cherished and memorable. 

## Table of Contents
- [Introduction](#introduction)
- [Previous Work](#previous-work)
- [Implementation](#implementation)
  - [Neighbor_list.txt](#neighbour-list)
  - [Comm_socket.py](#Comm_socket)
  - [Iterative_algo.py](#iterative_algo)
  - [Upload.py](#upload)
  - [Run.py](#run)
  - [Testbed](#Testbed)
- [Conclusion](#conclusion)  
- [Installation and Configuration](#installation-and-configuration)
- [References](#references)

## Introduction

In the research area of distributed systems, most of the time, algorithms are specifically developed to determine the behavior of a node - an independent unit that processes work - within a network of such nodes. These nodes are only aware of properties pertaining to itself and its neighbors. Each node has the ability to communicate with its neighbors through some form of message passing system (i.e. broadcast or unicast). Therefore, consider a set of interconnected nodes with some initial value such that after running the algorithm for several rounds, they all are left with the same value. Algorithms that execute certain blocks of code repeatedly are called iterative algorithms.  Also consensus is defined as when each node possessing an initial value, follows a distributed strategy to agree on the same value by calculating some function of these initial values. In this thesis we use iterative algorithms to obtain average consensus among the nodes. The purpose of this project is to build and study the behavior of these algorithms, such as those described in [\[1\]](#approx-consensus)[\[2\]](#dual-averaging)[\[3\]](#lili1)[\[4\]](#lili2)[\[5\]](#lili2).

The goal of the thesis was to quicken the setup of a network of nodes to study how an algorithm behaves. Often, valuable time is spent on setting up the testbed to run the algorithm on and also finding a means for communication between them. Cutting down on this time, we can help to get to the actual algorithm testing stage much quicker. This framework provides a way for the user to quicken development of such algorithms by abstracting the communication block of the code and testing the algorithm on a network of nodes by remotely uploading the data. 

We implement the program in Python for its general ease and use and abstraction. In the interest of speed and minimizing communication overhead, a shared memory approach was chosen to pass messages between the different threads that represented individual nodes. For the nodes themselves we use [Raspberry pi’s](https://www.raspberrypi.org/) with a 150 Mbps wireless USB network adapter [TL-WN727N](http://www.tp-link.com/us/download/TL-WN727N.html).

## Previous Work
In order to further improve the setup time of iterative algorithms, there has been quite a lot of work in the research community. A system [6]() to simulate a theoretical network of nodes to study how an algorithm behaves was developed. Real-world constraints like network delay and faulty nodes were not a concern for said project. Therefore, to be more real-world friendly we build upon this idea by configuring a testbed and testing different topological scenarios. As far as consensus (and average consensus) problems go, it has received extensive notice from the research community. The applicability to topics such as modeling of flocking behavior in biological, multi-agent systems, and physical systems [1](), [2]() makes it an extensively researched topic.  

## Implementation

In this thesis I implement the algorithm described in [5] to test out the framework. As described in there, the algorithm helps to address the problem of achieving average consensus over lossy links. By average consensus, we mean to say that each node will end up with a value which is the average of the all the initial node values. By lossy links, we mean that communication channels between the nodes might be prone to packet loss. We achieve this lossy communication by using broadcast. In Figure 1, we can see the general topology of the testbed. The arrows represent the direction of communication; i.e. a recipient arrow means that a node can only receive information along those channels. Thus, we can see that every node can only send/receive information to/from one other adjacent neighbor node. Each node also receives data from the host. Thus, we simulate topological constraints through this cyclic nature of communication, thereby implementing a ring based routing system between the Raspberry pi’s using a neighbor list. 

![High_level_network_topology](Documentation/High_level_network_topology.jpg)

Figure 2 shows the sub files present in each of the node and the host. We split up the implementation on the node side into 3 files. Neighbor_list.txt contains the neighbor list of each node. Comm_socket.py consists of the socket programming and node communication methods and finally Iterative_algo.py consists of the iterative algorithm we are implementing. On the host side, we have two files Upload.py uploads the files remotely to the nodes and compiles them inline. Run.py sends the start signal to begin the algorithm.

![Code_components](Documentation/Code_components.jpg)

### Neighbour_list.txt

This file consists basis for the ring based routing algorithm to work. Essentially, this file governs which neighbors to talk to and which neighbors to listen to. In Figure 3, we have the list for node with IP address 192.168.12.1. There is an oddity in the fact that the node itself appears in both categories, but this is due to the specificities of the algorithm [5] we are implementing.


