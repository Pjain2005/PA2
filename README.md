# PA2

TEAM MEMBERS:  
    Alicia Ellis, UFID: 79954495  
    Priyanka Jain, UFID: 31478022

COMPILATION INSTRUCTIONS:  
    No compilation required. This assignment is written in Python 3.

RUN INSTRUCTIONS:  
    1. From the root, run the program with the following command:  
        python main.py <input_file>  
    
    2. The available input files are located in the "tests" directory:  
        1. tests/example.in -> Small 6-request test file to check for correctness.  
        2. tests/test1.in -> k=3, m=60. Repeating pattern with frequent anchor items.  
        3. tests/test2.in -> k=4, m=64. Rotating block with infrequent items introduced in a regular manner.  
        4. tests/test3.in -> k=5, m=64. Structured cycle with unique items nearing the end.  
        5. tests/thrash.in -> k=3, m=60. Sequence with k+1 items that causes online policies to miss all items.  
        6. tests/locality.in -> k=4, m=50. Rotating block with infrequent items introduced in a random manner.  
        7. tests/belady_anomaly.in -> k=3, m=60. Known sequence where FIFO outperforms LRU.  
    
    3. When a command (such as python main.py tests/test1.in) is executed, the results for the number of misses will be printed to the terminal.  

OUTPUT FORMAT:  
    The program prints the number of cache misses for each eviction policy in this manner:  
        FIFO  : <number_of_misses>  
        LRU   : <number_of_misses>  
        OPTFF : <number_of_misses>  

ASSUMPTIONS:  
    1. k >= 1 and m >= 1 are always given in the input file.  
    2. Items are always represented by positive integers.  
    3. Input files have no empty lines.  
    4. OPTFF requires the full request sequence in advance.  

SOLUTIONS TO WRITTEN COMPONENT:  
    Our solutions to the written component can be found in this PDF: [Responses](PA2.pdf)  
