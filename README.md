## A simple comparision between docker tagging tools :

This script consists of a quick speed comparision of three methods to tag docker images on a remote docker registry. These tools are `crane`, `buildx imagetools` and the normal `docker` pull/push routine. These were the results of my latest test : 

```
Crane execution time : 6384.608030319214 ms
Imagetools execution time : 4960.407018661499 ms
Docker execution time : 577369.0140247345 ms
````
