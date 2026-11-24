#!/usr/bin/env python3
"""Create support vector machine classifiers with different kernels."""
from sklearn import svm


def get_SVM_model(name, random_state):
    """Create an untrained support vector machine classifier.

    Args:
        name: A string indicating the kernel to use. Accepted values are
            'linear' for a linear kernel, 'poly' for a polynomial kernel
            and 'rbf' for a radial basis function kernel.
        random_state: The seed used by the random number generator for
            reproducibility.

    Returns:
        model: An untrained SVC instance using the requested kernel.
    """
    return svm.SVC(kernel=name, random_state=random_state)
