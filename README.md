# README

This file contains the instructions to run the code for the midterm along with the explanation of the code. The codebase has taken inspiration from the solutions that I have submitted in assignment 1 and 2.

## Execution

### 1

```
mapred streaming -input ds8106-hw1/data -output midterm-1/ -mapper "python reservoir_sampling_mapper.py 900" -file reservoir_sampling_mapper.py -reducer "python reservoir_sampling_reducer.py" -file reservoir_sampling_reducer.py
```
