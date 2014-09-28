Types of Events
===============

## Input  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Button  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Textbox  
## Keyboard  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Key Up  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Key Down  
## Mouse  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Click  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Drag  
## Timer  

Quiz
====

Question 1
----------

What happens if you press a key and click the mouse at exactly the same time?

### Answer

One of the event handlers executes and the other waits in the event queue until the first handler finishes.

### Explanation

You can't control the order that the system inserts events into the event queue and only one event handler executes at a time.  