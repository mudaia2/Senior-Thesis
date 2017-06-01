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
		
