# StackOverflowTagger

Auto-tagging of StackOverflow Questions

![kek](https://miro.medium.com/max/1400/1*zEi3upbdEgU2CmRVe8WBiA.jpeg)

[Presentation](https://github.com/helena128/StackOverflowTagger/raw/master/DT_NLP.pdf)

## Python notebooks with models
[Approach #1](https://github.com/helena128/StackOverflowTagger/blob/master/DT_NLP.ipynb) - keywords as tags

[Approach #2](https://github.com/helena128/StackOverflowTagger/blob/master/DT_NLP_Multiclass.ipynb) - multiclass model

## Build and run docker image with REST API
**Build image**

Preconditions:
- docker daemon is installed and started

Command:

`/bin/sh ./build.sh`

**Run container**

Preconditions:
- docker daemon is installed and started
- port 8080 is free

Command:

`/bin/sh ./run.sh`

**Stop container**

Preconditions:
- docker daemon is installed and started
- container is started

Command:

`/bin/sh ./stop.sh`
