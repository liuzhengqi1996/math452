#!/usr/bin/env python
# coding: utf-8

# # 1.3 Some popular data sets in image classification 
# 
# In this subsection, we will introduce some popular and standard data sets in image
# classification.
# 
# ```{list-table}
# :header-rows: 1
# :name: example-table
# * - dataset
#   - training(N)
#   - test(M)
#   - classes(k)
#   - channels(c)
#   - input size(d)
#  * - MNIST
#    - 60K
#    - 10K
#    - 10
#    - GRAYSCALE
#    - 28*28
#  * - CIFAR-10
#    - 50K
#    - 10K
#    - 10
#    - RGB
#    - 32*32
#  * - CIFAR-100
#    - 50K
#    - 10K
#    - 10
#    - RGB
#    - 32*32
#  * - ImageNet
#    - 1.2M
#    - 50K
#    - 1000
#    - RGB
#    - 224*224
#   ```

# ## MNIST(Modified National Institute of Standards and Technology Database) 
# 
# ### This is a database for handwritten digits
# - Training set : N = 60,000
# - Test set : M = 10,000
# - Image size : d = 28 * 28 * 1 = 784
# - Classes: k = 10
# ```{figure} ../figures/mnist2_1.png
# :name: mnist
# ```

# ## CIFAR 
# 
# ### CIFAR-10
# - Training set : N = 50,000
# - Test set : M = 10,000
# - Image size : d = 32 * 32 * 3
# - Classes: k = 10
# ```{figure} ../figures/mnist1_1.png
# :name: mnist
# ```
# 
# ### CIFAR-100
# - Training set : N = 50，000
# - Test set : M = 10，000
# - Image size : d = 32 * 32 * 3
# - Classes: k = 100
# ```{figure} ../figures/mnist1_1.png
# :name: mnist
# ```
# 

# ## ImageNet 
# 
# - All data set: N + M = 1，431，167
# - Image size : d = 224 * 224 * 3
# - Classes: k = 1，000
# ```{figure} ../figures/imagenet1_1.png
# :name: mnist
# ```
# ```{figure} ../figures/imagenet1_2.png
# :name: mt
# ```
