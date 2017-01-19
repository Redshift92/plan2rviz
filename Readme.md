# plan2rviz

A simple ROS node to visualize 2D formation planning algorithms on rviz.

### Usage

launch the node:

    $ roslaunch plan2rviz plan2rviz.launch

publish JSON strings on *plan2rviz_notifier* topic with info about players you want to visualize.
Three types of players are available:

  - obstacles
  - edges
  - agents
 
Each player has a default color and shape, currently you are able to change a player color and height.

### JSON Format

    { 
        "obstacles": [ [1,1], [1,2] ], 
        "agents":    [ [2,2], [3,4,{"rgb": [0,255,0]}] ],
        "edges":     [ [[0,1,1,2], [0,1,1,2]] ]
    }

The above JSON draws on rviz:

  - obstacles with coordinates (1,1) and (1,2) and default color;
  - one agent with coordinates (2,2) and default color and a green agent with coordinates (3,4);
  - two links: one between coordinates (0,0) and (1,1) and the other one between (1,1) and (2,2).

*plan2rviz* assigns to each received player an id corresponding to its position in the received list of lists, this allows to change its coordinates with two consecutive commands:

    {
        "agents":    [ [2,3] ]
    }
  
 will move agent 0 from (2,2) to (2,3).
 
##### Edges: 

    "edges":     [ [[0,1,1,2], [0,1,1,2]] ]

creates a single edge object composed of two links between two points: x coordinates are placed in the first list, ys in the second.
Placing all links in a single edge object will allow overwriting the whole edge configuration with another single edge object.
Example:
    
    {
        "edges":     [ [[0,1,1,2], [0,1,1,2]] ] 
    }
    
followed by:
    
    {
        "edges":     [ [[0,3], [0,3]] ] 
    }
    
will substitute two links ( (0,0)->(1,1) and (1,1)->(2,2) ) with a single one ( (0,0)->(3,3) ).
On the other hand:

    {
        "edges":     [ [[0,1], [0,1]], [[1,2],[1,2]] ] 
    }

followed by:
    
    {
        "edges":     [ [[0,3], [0,3]] ] 
    }
    
will substitute only one link ( (0,0)->(1,1) ) with a new one ( (0,0)->(3,3) )
    
###### This project is licensed under the terms of the MIT license.


