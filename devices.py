def supportedDevices ():

	# Returns the list of all supported devices

	return ["ibmqx2","ibmqx4","ibmqx5","19Q-Acorn","5Q-Test"]

def getLayout (device):

	# Input:
	# 
	# * *device* - A string which specifies the device to be used.
	# 
	# Process:
	# 
	# * Look up the details of that device.
	# 
	# Output:
	# 
	# * *num* - The number of qubits in the device.
	# * *area* - A list with two entries specifying the width and height for the plot of the device. These should be in units of qubits (i.e. *area=[8,2]* for an *8x2* grid of qubits).
	# * *entangleType* - Type of entangling gate ("CX" or "CZ").
	# * *pairs* - A dictionary of pairs of qubits for which an entagling gate is possible. The key is a string which serves as the name of the pair. The value is a two element list with the qubit numbers of the two qubits in the pair. For controlled-NOTs, the control qubit is listed first.
	# * *pos* - A dictionary of positions for the qubits in the plot. Keys are qubit numbers and values are a two element list of coordinates.
	# * *example* - An example set of noisy entanglement results for use in the tutorial.
	# * *sdk* - The SDK to be used when running jobs on this device.
    # * *runs* - Data that has been obtained. As a dictionary with values of *sim* as keys.
    
    if device=="ibmqx5":
        # A 16 qubit device by IBM
        # https://github.com/QISKit/ibmqx-backend-information/tree/master/backends/ibmqx5
    
        # the positions of qubits on the device (numbers), and names of pairs (letters) for ibmqx5
        #    [1]---(A)---[2]---(B)---[3]---(C)---[4]---(D)---[5]---(E)---[6]---(F)---[7]---(G)---[8]
        #     |           |           |           |           |           |           |           |
        #    (H)         (I)         (J)         (K)         (L)         (M)         (N)         (O)
        #     |           |           |           |           |           |           |           |
        #    [0]---(P)--[15]---(Q)--[14]---(R)--[13]---(S)--[12]---(T)--[11]---(U)--[10]---(V)---[9]

        num = 16
        area = [8,2]
        entangleType = "CX"
        pairs = { 'A': [1,2], 'B': [2,3], 'C': [3,4], 'D': [5,4], 'E': [6,5], 'F': [6,7], 'G': [8,7],
                 'H': [1,0], 'I': [15,2], 'J': [3,14], 'K': [13,4], 'L': [12,5], 'M': [6,11], 'N': [7,10], 'O': [9,8],
                 'P': [15,0], 'Q': [15,14], 'R': [13,14], 'S': [12,13], 'T': [12,11], 'U': [11,10], 'V': [9,10]}
        pos = { 0: [0,0], 1: [0,1],  2: [1,1],  3: [2,1],  4: [3,1],  5: [4,1],  6: [5,1],  7: [6,1],
               8: [7,1], 9: [7,0], 10: [6,0],  11: [5,0],  12: [4,0],  13: [3,0],  14: [2,0],  15: [1,0] }
        example = [0.11, 0.09, 0.49, 0.52, 0.31, 0.89, 0.15, 0.18, 0.47, 0.43, 0.67, 0.62, 0.93, 0.29, 0.77, 0.73]
        sdk = "QISKit"
        runs = {True:{'shots':[100,1000,10000],'move':['C','R'],'maxScore':20,'samples':100},False:{'shots':[8192],'move':['C'],'maxScore':10,'samples':20}}

    
    elif device=="ibmqx2": #
        # A 5 qubit device by IBM
        # https://github.com/QISKit/ibmqx-backend-information/tree/master/backends/ibmqx2
    
        # the positions of qubits on the device (numbers), and names of pairs (letters) for ibmqx2
        #    [4]         [0]
        #     | \       / |
        #     | (D)   (B) | 
        #     |   \   /   |
        #    (F)   [2]   (A)
        #     |   /  \    |
        #     | (E)  (C)  |
        #     | /       \ |
        #    [3]         [1]
    
        num = 5
        area = [3,3]
        entangleType = "CX"
        pairs = { 'A': [0,1], 'B': [0,2], 'C': [1,2], 'D': [4,2], 'E': [3,2], 'F': [3,4] }
        pos = { 0: [1,1], 1: [1,0],  2: [0.5,0.5],  3: [0,0],  4: [0,1] }
        example = [0.11,0.09,0.49,0.52,0.31]
        sdk = "QISKit"
        runs = {True:{'shots':[100,1000,10000],'move':['C','R'],'maxScore':20,'samples':100},False:{'shots':[8192],'move':['C'],'maxScore':10,'samples':20}}
       
    elif device=="ibmqx4":
        # A 5 qubit device by IBM
        # https://github.com/QISKit/ibmqx-backend-information/tree/master/backends/ibmqx4
    
        # the positions of qubits on the device (numbers), and names of pairs (letters) for ibmqx4
        #    [4]         [0]
        #     | \       / |
        #     | (D)   (B) | 
        #     |   \   /   |
        #    (F)   [2]   (A)
        #     |   /  \    |
        #     | (E)  (C)  |
        #     | /       \ |
        #    [3]         [1]
    
        num = 5
        area = [3,3]
        entangleType = "CX"
        pairs = { 'A': [1,0], 'B': [2,0], 'C': [2,1], 'D': [2,4], 'E': [3,2], 'F': [3,4] }
        pos = { 0: [1,1], 1: [1,0],  2: [0.5,0.5],  3: [0,0],  4: [0,1] }
        example = [0.11,0.09,0.49,0.52,0.31]
        sdk = "QISKit"
        runs = {True:{'shots':[100,1000,10000],'move':['C','R'],'maxScore':20,'samples':100},False:{'shots':[8192],'move':['C'],'maxScore':10,'samples':20}}

    elif device=="QS1_1":
        # A 20 qubit device by IBM
        # https://quantumexperience.ng.bluemix.net/qx/devices
    
        num = 20
        area = [7,7]
        entangleType = "CX"
        pairs = { 'a': [0,1], 'b': [1,2], 'c': [3,4],
                 'd': [0,5], 'e': [1,6], 'f': [2,7], 'g': [3,8], 'h': [3,9], 'i': [4,8], 'j': [4,9],
                 'k': [5,6], 'l': [6,7], 'm': [8,9],
                 'n': [5,10], 'o': [5,11], 'p': [6,10], 'q': [6,11], 'r': [7,12], 's': [7,13], 't': [8,12], 'u': [8,13], 'v': [9,14],
                 'w': [10,11], 'x': [11,12], 'y': [12,13], 'z': [13,14],
                 'A': [10,15], 'B': [11,16], 'C': [11,17], 'D': [12,16], 'E': [12,17], 'F': [13,18], 'G': [13,19], 'H': [14,18], 'I': [14,19],
                 'J': [15,16], 'K': [16,17], 'L': [17,18], 'M': [18,19]}
        pos = { 0: [0,3], 1: [1,4], 2: [2,4], 3: [3,4], 4: [4,4],
                5: [-1,2.5], 6: [1,2.5], 7: [2,2.5], 8: [3.5,2], 9: [5,2],
               10: [-1,0.5], 11: [1,1], 12: [2,1], 13: [3,1], 14: [5,1],
               15: [0,0], 16: [0.5,-1], 17: [2,-1], 18: [3,0], 19: [5,-1] }
        example = [.32, .33, .92, .82, .11, .16, .15, .91, .12, .84, .52, .43, .78, .19, .47, .52, .78, .42, .48, .18]
        #          0    1    2    3    4    5     6   7    8    9    10   11   12   13   14   15   16   17   18   19
        sdk = "QISKit"
        runs = {True:{'shots':[100,1000,10000],'move':['C','R'],'maxScore':20,'samples':100},False:{'shots':[8192],'move':['C'],'maxScore':10,'samples':20}}
        
    elif device=="19Q-Acorn":
        # A device by Rigetti with 20 qubits, but since one is isolated it is effectively 19
        # https://arxiv.org/abs/1712.05771
        # http://pyquil.readthedocs.io/en/latest/qpu_overview.html#acorn-qpu-properties
    
        num = 20
        area = [10,4]
        entangleType = "CZ"
        pairs = { 'A': [0,5], 'B': [0,6], 'C': [1,6], 'D': [1,7], 'E': [2,7], 'F': [2,8], 'G': [4,9],
                  'H': [5,10], 'I': [6,11], 'J': [7,12], 'K': [8,13], 'L': [9,14],
                  'M': [10,15], 'N': [10,16], 'O': [11,16], 'P': [11,17], 'Q': [12,17], 'R': [12,18], 'S': [13,18], 'T': [13,19], 'U': [14,19] }
        pos = { 0: [1,3], 1: [3,3], 2: [5,3], 4: [9,3],
                5: [0,2], 6: [2,2], 7: [4,2], 8: [6,2], 9: [8,2],
               10: [1,1], 11: [3,1], 12: [5,1], 13: [7,1], 14: [9,1],
               15: [0,0], 16: [2,0], 17: [4,0], 18: [6,0], 19: [8,0] }
        example = [.32, .48, .58, None,.15, .52, .33, .47, .59, .17, .51, .76, .89, .23, .65, .02, .78, .91, .25, .64]
        #          0    1    2    3    4    5     6   7    8    9    10   11   12   13   14   15   16   17   18   19
        sdk = "Forest"
        runs = {True:{'shots':[100,1000,10000],'move':['C','R'],'maxScore':20,'samples':100},False:{'shots':[10000],'move':['C','R'],'maxScore':5,'samples':20}}
        
    else:
        
        print("\nWarning: This is not a known device.\n")
    
    return num, area, entangleType, pairs, pos, example, sdk, runs
