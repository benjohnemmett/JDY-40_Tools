# JDY-40 Hub and Node Test
The hub JDY-40 is connected to a computer running multicast_hub.py. Probably through a When the user inputs the remote node name on the command line, the hub sends a message to that node.

Each JDY-40 node is connected to an Arduino device running JDY_40_multicast_node.ino. The JDY_40_multicast_node.ino file must be modified to give each node a unique name. When the hub sends a message with a "destination" field that matches one of the nodes, that node will reply with it's data. 
