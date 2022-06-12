notes for saturday:

1. view inventory works, might want to display it in a way that is not an object.__dict__

2. view customer rentals: code works, seems to show when a 4.sx film is rented and when a 5.sx film is returned. does not display 3.add member, but there is a larger error with that fucntion

3. add customer works logically. it displays good messages, but it does not update the rental member list accurately and it does not change the inventory numbers correctly. it peerforms all these actions, but they are not saved in the memory as an action that was taken (good be somethiong about the csv file resetting each time?might not need to worry about it)

4. rent a video functionaly works. i can rent a video to a SX account (#4) and it will remove a copy from inventory, and will display it under my rentals. i need to expand this functionality to the other 3 account types (maybe need to reorder soem logic or perhaps implement a method internaly somehow)

5. return a video works, was able to sucessfully return a video and it was removed from users rentals and the inventory was updated.

6. exits the function

other:
double check rubric and readme for style and display.
double check notes
clean up folder to push to git
check for logic in naming conventions