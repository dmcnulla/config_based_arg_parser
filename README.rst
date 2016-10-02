My First Stupid Python Package
==============================
This is supposed to read a yaml file to figure out what the command line arguments are:

.. code-block:: yaml

    { prog: Program, description: Description, epilog: Epilog,
      arguments: {
         argOne: {
           required: True,
           help: Get current Jmeter test plan path.
         },
         argTwo: {
           required: False,
           help: Thsi param is not required.
         }
      }
    }
