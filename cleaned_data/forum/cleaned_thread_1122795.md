# Thread Information
Title: Thread-1122795
Section: RouterOS
Thread ID: 1122795

# Discussion

## Initial Question
https://www.youtube.com/watch?v=LcNpZg8m7s0After watching the video I bought a ESP32 Cheap Yellow Display Board (CYD ESP32-2432S028R) with the idea of ​​monitoring the eth1 of my hAP ax3.After downloading the display files fromhere, I configured the display resolution and all the requested data as indicated on:https://github.com/Druvis-Timma/Mikroti ... 2_graphingIt works but there are 2 problems that I can't solve even after many attempts:1. The interface to monitor is eth1 which has id 0, if I configure "const int graph_interface = 0" esp32 show me only a black screen;interfaces.png2. If the transfer speed is high the bar is not displayed, the graph becomes smaller but does not show the colored bar;Has anyone had the same experience and knows how to help me?Thanks ---

## Response 1
1. The interface to monitor is eth1 which has id 0, if I configure "const int graph_interface = 0" esp32 show me only a black screen;Index numbers (e.g. 0, 1, ...) ... are only valid after executingprintcommand ... and are valid only until another print command is executed (even if in different configuration branch). So command would properly be written asconst in graph_interface = [ find name=ether1 ]or something like that .... depending on how exactlygraph_interfaceis then used.2. If the transfer speed is high the bar is not displayed, the graph becomes smaller but does not show the colored bar;I'd say that this has nothing to do with ROS ... it has something to do with the display itself and/or how custom code (run by ROS never the less) drives display. ---

## Response 2
So command would properly be written as const in graph_interface = [ find name=ether1 ]Thanks for your help, unfortunately it doesn't work... I give up for now.Only Druvis can help me ---

## Response 3
1. The interface to monitor is eth1 which has id 0, if I configure "const int graph_interface = 0" esp32 show me only a black screen;interfaces.pngMy mistake, using API the correct interface id is 1 and not 0.There is always the problem of the graph not being drawn if the traffic is more than about 100 Mbps. ---