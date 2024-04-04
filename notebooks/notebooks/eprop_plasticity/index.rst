

.. _sphx_glr_auto_examples_eprop_plasticity:

E-prop plasticity examples
==========================


.. image:: ../../../../pynest/examples/eprop_plasticity/eprop_supervised_regression_schematic_sine-waves.png

Eligibility propagation (e-prop) [1]_ is a three-factor learning rule for spiking neural networks
that approximates backpropagation through time. The original TensorFlow implementation of e-prop
was demonstrated, among others, on a supervised regression task to generate temporal patterns and a
supervised classification task to accumulate evidence [2]_. Here, you find tutorials on how to
reproduce these two tasks as well as two more advanced regression tasks using the NEST implementation
of e-prop [3]_ and how to visualize the simulation recordings.

References
----------

.. [1] Bellec G, Scherr F, Subramoney F, Hajek E, Salaj D, Legenstein R,
       Maass W (2020). A solution to the learning dilemma for recurrent
       networks of spiking neurons. Nature Communications, 11:3625.
       https://doi.org/10.1038/s41467-020-17236-y

.. [2] https://github.com/IGITUGraz/eligibility_propagation/blob/master/Figure_3_and_S7_e_prop_tutorials/

.. [3] Korcsak-Gorzo A, Stapmanns J, Espinoza Valverde JA, Dahmen D,
       van Albada SJ, Bolten M, Diesmann M. Event-based implementation of
       eligibility propagation (in preparation)



.. raw:: html

    <div class="sphx-glr-thumbnails">


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Training a regression model using supervised e-prop plasticity to generate sine waves">

.. only:: html

  .. image:: /auto_examples/eprop_plasticity/images/thumb/sphx_glr_eprop_supervised_regression_sine-waves_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_eprop_plasticity_eprop_supervised_regression_sine-waves.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Tutorial on learning to generate sine waves with e-prop</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Training a regression model using supervised e-prop plasticity to generate an infinite loop">

.. only:: html

  .. image:: /auto_examples/eprop_plasticity/images/thumb/sphx_glr_eprop_supervised_regression_infinite-loop_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_eprop_plasticity_eprop_supervised_regression_infinite-loop.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Tutorial on learning to generate an infinite loop with e-prop</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Training a regression model using supervised e-prop plasticity to generate handwritten text">

.. only:: html

  .. image:: /auto_examples/eprop_plasticity/images/thumb/sphx_glr_eprop_supervised_regression_handwriting_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_eprop_plasticity_eprop_supervised_regression_handwriting.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Tutorial on learning to generate handwritten text with e-prop</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Training a classification model using supervised e-prop plasticity to accumulate evidence.">

.. only:: html

  .. image:: /auto_examples/eprop_plasticity/images/thumb/sphx_glr_eprop_supervised_classification_evidence-accumulation_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_eprop_plasticity_eprop_supervised_classification_evidence-accumulation.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Tutorial on learning to accumulate evidence with e-prop</div>
    </div>


.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/eprop_plasticity/eprop_supervised_regression_sine-waves
   /auto_examples/eprop_plasticity/eprop_supervised_regression_infinite-loop
   /auto_examples/eprop_plasticity/eprop_supervised_regression_handwriting
   /auto_examples/eprop_plasticity/eprop_supervised_classification_evidence-accumulation

