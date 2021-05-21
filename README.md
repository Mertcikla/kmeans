# Image compression with k-means clustering

Compress color palette by combining RGB values that are close to each other. For RGB8 this is equivalent to having 2^8 = 256 clusters. 

[Slides](https://github.com/Mertcikla/kmeans/blob/a291a1bfd05f058865d888dc4d456a6bff74fb89/docs/k_means.pdf)

|Original   |Compressed with k=4  |
|--|--|
|<img src="https://github.com/Mertcikla/kmeans/blob/a291a1bfd05f058865d888dc4d456a6bff74fb89/kitten.jpg" alt="drawing" width="250"/>  |<img src="https://github.com/Mertcikla/kmeans/blob/a291a1bfd05f058865d888dc4d456a6bff74fb89/compressed_kitten_4.png" alt="drawing" width="250"/>|


| Original  |  Compressed with k=10 |
|--|--|
| <img src="https://github.com/Mertcikla/kmeans/blob/a291a1bfd05f058865d888dc4d456a6bff74fb89/images/flower.jpg" alt="drawing" width="250"/>  | <img src="https://github.com/Mertcikla/kmeans/blob/a291a1bfd05f058865d888dc4d456a6bff74fb89/images/flower_compressed_10.jpg" alt="drawing" width="250"/>  |


*Originally this code was written in Matlab which I lost access. Reproducing with the Python implementation here should result similar results.*
