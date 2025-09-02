# Flash Storage

## NOR flash 

1. CPU has access to each byte one by one 
2. CPU can execute code directly from NOR flash 

- NOR flash because each cell has one end connected directly to ground and the other end to the bit line.
- When one of the word lines are connected and brought high, the corresponding storage transistor acts to
  pull the output bit line low.

## NAND flash

1. External device like a rotating storage.
2. Code execution only possible after moving contents to ram

- Floating gate transistors that are connected in series and only if all the word lines are pulled high the bit line 
  is pulled low

## Linux MTD partitions

- Define areas for different purposes.
- No partition table in block devices. 
- Partitions are defined in the kernel
