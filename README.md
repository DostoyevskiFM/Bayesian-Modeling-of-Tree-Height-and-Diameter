# Bayesian-Modeling-of-Tree-Height-and-Diameter
This project uses Bayesian statistics to find out how a tree's thickness (diameter) affects its height. By using probabilities, we want to predict tree height more accurately, which helps in measuring forests and understanding nature.

Problem statement 

The aim of this project is to explore using Bayesian methods the relationship between the height of a tree of a particular species and its diameter measured at breast height. This problem is crucial in forestry for multiple reasons:

- as will be shown, height of a tree is a very important metric, though its measurement may cause practical difficulties (for higher trees foresters are required to use specialized devices, which still do not always guarantee perfect precision, apply less accurate estimation methods or climb directly onto the tree), while the measurement of the diameter is straightforward. The predictive properties of the proposed model might help further estimation of the height based on precise diameter measurements. 

- height of a tree, as useful as it can be on its own, is also essential in calculating derivative parameters such as log volume (volume of wood in an individual tree) or stand volume (in the case of a group of trees) which, in turn, make it possible to determine the forest’s resource potential. The other applications include the calculation of biomass of a tree and consequently evaluating the storage of carbon dioxide in the forest, as well as soil quality (bonitation) assessment. 

For these reasons, the subject of this project is already quite well established, with the height-diameter curve as one of the most important and practical tools in forestry. However, the readily available studies involve problems and solutions that slightly differ from the ones presented in this report (examples would be https://doi.org/10.17221/68/2023-JFS - comparison of multiple models in frequentist setting, http://dx.doi.org/10.1155/2014/683691 - comparison of Bayesian non-hierarchical models, doi:10.1093/forestry/cpr050 - mixed-effects (hierarchical) Bayesian models with breast-height age as explanatory variable, different link function).  

Finally, red spruce (Picea rubens), the species selected for modelling, is known for its remarkable wood, used for acoustic stringed instruments, and in the paper pulp industry. It is also a popular choice for a holiday tree and usual lumber.
