# auiabsbhhhhhtlircpuimldoioeppppppp.py

A Python interpreter/compiler for the esoteric programming language: **AMONGUSISABIGSUSSYBAKAHAHAHAHAHATHISLANGUAGEISREALLYCOOLPLEASEUSEITMYLIFEDEPENDSONITORELSEPLSPLSPLSPLSPLSPLSPLSkahyghdfhmILLDIEIFYOUDONTUSEITSOPLEASEUSEITALSODONATETOMYGOFUNDMEBECAUSEIMGONNADIEBECAUSEYOUWONTUSETHISLANGUAGEURTHEIMPOSTORANDTHATISSUSIMGOINGTOCALLAMEETINGONYOUYOUVENTEDYOUSUSSYBAKA**.

See the [esolang page](https://esolangs.org/wiki/AMONGUSISABIGSUSSYBAKAHAHAHAHAHATHISLANGUAGEISREALLYCOOLPLEASEUSEITMYLIFEDEPENDSONITORELSEPLSPLSPLSPLSPLSPLSPLSkahyghdfhm) for more information

## Installation

You can install the package locally using pip:

```bash
pip install .
```

Or, if you build a wheel:

```bash
pip install dist/auiabsbhhhhhtlircpuimldoioeppppppp_py-*.whl
```

## Usage

The script provides a command-line interface named `auiabsbhhhhhtlircpuimldoioeppppppp`.

**Run a file:**

```bash
auiabsbhhhhhtlircpuimldoioeppppppp <your_program.auiabsbhhhhhtlircpuimldoioeppppppp>
```

**Compile a file to Python:**

This will create `<your_program.auiabsbhhhhhtlircpuimldoioeppppppp>-compiled.py`.

```bash
auiabsbhhhhhtlircpuimldoioeppppppp <your_program.auiabsbhhhhhtlircpuimldoioeppppppp> --compile
# or
auiabsbhhhhhtlircpuimldoioeppppppp <your_program.auiabsbhhhhhtlircpuimldoioeppppppp> -c
```

**Compile to a specific output file:**

```bash
auiabsbhhhhhtlircpuimldoioeppppppp <your_program.auiabsbhhhhhtlircpuimldoioeppppppp> -c --outfile <output_name.py>
```

**Interactive Mode:**
```
$ auiabsbhhhhhtlircpuimldoioeppppppp
```
Run commands line by line.

```bash
Interactive auiabsbhhhhhtlircpuimldoioeppppppp
>>> guys i can vouch crewmate is 10
>>> crewmate goes up
>>> crewmate can vouch go and tell them come on
```

## Language Reference

The language operates on variables (players) which hold integer values. Variable names must consist of lowercase letters and underscores (`[a-z_]+`). Commands are case-insensitive. Comments start with `//`.

| Command                                                     | Description                                                                 | Python Equivalent                     |
| :---------------------------------------------------------- | :-------------------------------------------------------------------------- | :------------------------------------ |
| `guys i can vouch [PLAYER] is [VALUE]`                      | Assigns integer `[VALUE]` to `[PLAYER]`.                                    | `player = value`                      |
| `[PLAYER] can vouch go and tell them come on`               | Prints the ASCII character corresponding to `[PLAYER]`'s value.             | `print(chr(player))`                  |
| `[PLAYER] is just like [SUSSYPLAYER]`                       | Assigns the value of `[SUSSYPLAYER]` to `[PLAYER]`.                         | `player = sussyplayer`                |
| `if its not [PLAYER] then vote me`                          | If `[PLAYER]`'s value is not 0, execute the next line. Otherwise, skip it.  | `if player != 0:`                     |
| `idk what [PLAYER] is but its between [MIN] and [MAX]`      | Assigns `[PLAYER]` a random integer between `[MIN]` and `[MAX]` (inclusive). | `player = random.randint(min, max)` |
| `[PLAYER] was the impostor`                                 | If `[PLAYER]`'s value is not 0, terminate the program immediately.          | `if player != 0: exit()`              |
| `[PLAYER] goes up`                                          | Increments `[PLAYER]`'s value by 1.                                         | `player = player + 1`                 |
| `[PLAYER] goes down`                                        | Decrements `[PLAYER]`'s value by 1.                                         | `player = player - 1`                 |
| `[PLAYER] who are you`                                      | Reads a single character from user input and stores its ASCII value in `[PLAYER]`. | `player = ord(input(...))`            |

## Example: Print "HI"

```auiabs
// filepath: example.auiabs
// Set h_val to 72 (ASCII 'H')
guys i can vouch h_val is 72
// Print 'H'
h_val can vouch go and tell them come on

// Set i_val to 73 (ASCII 'I')
guys i can vouch i_val is 73
// Print 'I'
i_val can vouch go and tell them come on
```

**Run it:**

```bash
auiabsbhhhhhtlircpuimldoioeppppppp example.auiabsbhhhhhtlircpuimldoioeppppppp
```

**Output:**

```
HI
```

## License

This project is licensed under the MIT License - see the [LICENSE](/workspaces/auiabsbhhhhhtlircpuimldoioeppppppp.py/LICENSE) file for details.