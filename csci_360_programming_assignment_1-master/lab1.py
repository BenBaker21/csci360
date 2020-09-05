# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from collections import deque

def breadth_first_search(stack):
    queue = deque()
    bfs_flip_sequence = []
    nodes_visited_bfs = []
    bfs_result = []
    #Need to add this state to the queue, FIFO
    #Each state consists of a stack and a flip-sequence
    queue.append((stack, bfs_flip_sequence))
    
    #Flagging the current state as visited
    nodes_visited_bfs.append(stack)

    
    while queue:
        #Getting the state at the front of the queue for FIFO search
        myNode = queue.popleft()
        
        if myNode[0].check_ordered():
            bfs_result = myNode[1]
        
        #Looping through all the books in the stack
        for i in range(1, myNode[0].num_books + 1):
        
            copy_stack = myNode[0].copy()
            copy_stack.flip_stack(i)
            
            copy_flip_sequence = myNode[1].copy()
            copy_flip_sequence.append(i)
            
            if copy_stack not in nodes_visited_bfs:
                #Adding the neighbor to the queue and flagging it as visited
                nodes_visited_bfs.append(copy_stack)
                queue.append((copy_stack, copy_flip_sequence))
                                
    return bfs_result
    # ---------------------------- #



def depth_first_search(stack): 
    myStack = []
    dfs_result = []
    dfs_flip_sequence = []
    nodes_visited_dfs = []
    
    myStack.append((stack, dfs_flip_sequence))
    
    while(len(myStack)):
        
        if(stack.check_ordered()):
            last_myStack = myStack.pop()
            dfs_result = copy_myStack[1]
            break
    
        last_myStack = myStack.pop()
        
        if last_myStack[0] not in nodes_visited_dfs:
            #Flagging the current state as visited
            nodes_visited_dfs.append(last_myStack[0])
        
        for i in range(1, last_myStack[0].num_books + 1):
            last_myStack[0].flip_stack(i)
            last_myStack[1].append(i)
            if last_myStack[0] not in nodes_visited_dfs:
                myStack.append((stack, dfs_flip_sequence))
    
    return dfs_result
    # ---------------------------- #
    
    
    
    
    
